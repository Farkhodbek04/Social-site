from api import serializers
from main import models

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status


class UserRegistrationAPIview(APIView):
    permission_classes = [AllowAny]

    def post(self, request): # It creates new user!
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token = Token.objects.create(user=user)
            return Response({
                'user':serializer.data,
                'token': token.key,
                'message': 'User registered successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateUserAPIview(APIView): # It updates an exiting user
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = models.User.objects.get(id=request.user.id)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SearchUsersAPIview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request): # It searches users by username
        username = request.query_params.get('username', '')

        users = models.User.objects.filter(username__icontains=username)
        serializer = serializers.UserSerializer(users, many=True)

        return Response(serializer.data)


class DeleteUserAPIview(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request): # It deletes the existing user.
        try:
            user = models.User.objects.get(id=request.user.id)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except models.User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         

class LoginUserAPIview(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            # Generate token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid username or password'}, status=400)
        

class FollowUserAPIview(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, id):
        to_user = get_object_or_404(models.User, id=id)
        relation = models.UserReletion.objects.create(from_user=request.user, to_user=to_user)
        serializer = serializers.UserRelationSerializer(relation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UnfollowAPIview(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id): # It unfollows user
        relation = get_object_or_404(models.UserReletion, to_user=id, from_user=request.user)
        relation.delete()
        return Response({'message': 'Unfollowed successfully'}, status=200)
    

class CreateChatAPIview(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        ...
    


