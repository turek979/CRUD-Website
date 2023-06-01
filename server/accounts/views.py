from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def user_registration(request):
    data = {}
    try:
        email = request.data.get('email')
        username = request.data.get('email')
        password = request.data.get('password')
        if not (email and username and password):
            raise ValueError("Email, username and password are required.")
        user = User.objects.create_user(username=username, email=email, password=password)
        token = Token.objects.create(user=user).key
        data = {'message': 'User created successfully.', 'token': token}
    except Exception as e:
        data = {'error': str(e)}
    return Response(data)


@api_view(['POST'])
def user_login(request):
    username = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    else:
        return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
