
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
import random

class RegisterView(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			# Send verification email
			verification_code = str(random.randint(100000, 999999))
			user.verification_code = verification_code
			user.save()
			send_mail(
				'Verify your email',
				f'Your verification code is: {verification_code}',
				settings.DEFAULT_FROM_EMAIL,
				[user.email],
				fail_silently=False,
			)
			return Response({'message': 'User registered. Verification email sent.'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')
		try:
			user = User.objects.get(username=username)
			if user.password == password:
				return Response({'message': 'Login successful.'})
			else:
				return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
		except User.DoesNotExist:
			return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

class VerifyEmailView(APIView):
	def post(self, request):
		username = request.data.get('username')
		code = request.data.get('code')
		try:
			user = User.objects.get(username=username)
			if user.verification_code == code:
				user.is_verified = True
				user.save()
				return Response({'message': 'Email verified.'})
			else:
				return Response({'message': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)
		except User.DoesNotExist:
			return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
class UserStatusView(APIView):
	def post(self, request):
		username = request.data.get('username')
		try:
			user = User.objects.get(username=username)
			return Response({'is_verified': user.is_verified})
		except User.DoesNotExist:
			return Response({'is_verified': False}, status=status.HTTP_404_NOT_FOUND)
