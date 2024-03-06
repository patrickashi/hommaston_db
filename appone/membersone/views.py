from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FormData
from .serializers import FormDataSerializer
from django.core.mail import send_mail
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "membersone/home.html", {} )

@api_view(['POST', 'OPTIONS'])
def form_submission(request):
    if request.method == 'POST':
        serializer = FormDataSerializer(data=request.data)
        if serializer.is_valid():
            cleaned_data = serializer.validated_data
            email = cleaned_data.get('email')
            print("Name:", cleaned_data.get('firstname'))
            print("Email:", cleaned_data.get('email'))
            print("Message:", cleaned_data.get('message'))
            
            serializer.save()
            send_mail(
                'Form Submission Received',
                f"You have received a new form submission.\n\nMessage: {cleaned_data['message']} \n email: {cleaned_data['email']}",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            # Send email confirmation to user
            send_mail(
                'Message Received',
                'Thank you for contacting us. Your message has been received successfully.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'OPTIONS':
        # Handle OPTIONS request by returning appropriate CORS headers
        response = Response({'detail': 'Allow: POST, OPTIONS'}, status=status.HTTP_200_OK)
        response['Access-Control-Allow-Origin'] = '*'  # Set appropriate origin if required
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    else:
        # For other HTTP methods like GET, return a method not allowed response
        return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)