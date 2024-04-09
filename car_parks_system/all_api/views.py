from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarParkModel, CustomUser
from .serializer import CarParkSerializer, CustomUserSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

def index(request):
    return render(request,"index.html")

@api_view(['GET'])
def all_car_parks_api(request):
    car_parks = CarParkModel.objects.all()
    serializer = CarParkSerializer(car_parks,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def user_login_api(request):
    print(type(request))
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = None
        
        if "@" in username:
            try:
                user = CustomUser.objects.get(email = username)
            except ObjectDoesNotExist:
                pass
        
        # Phone number example: (555) 444-3333x+90
        if "+" in username:
            try:
                user = CustomUser.objects.get(phone_number = username)
            except ObjectDoesNotExist:
                pass
            
        if not user:
            user = authenticate(username = username, password = password)

        if user:
            login(request,user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)    
        
@api_view(['POST'])
def user_register_api(request):
    if request.method == "POST":
        serializer = CustomUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout_api(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
