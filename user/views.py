from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


# Create your views here.
 


class CustomUserCreate(APIView):
    permission_classes =[AllowAny]

    def post(self,request,format='json'):
        serializer =CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            newuser =serializer.save()
            # print('user:', user)
            if newuser:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class BlacklistTokenView(APIView):
        def post(self,request):
            try:
                token =RefreshToken(request.data.get('refresh'))
                token.blacklist()
                return Response('Success', status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)




class CustomUserLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                            context ={'request':
                                            request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created =Token.objects.get_or_create(user=user)

        return Response({
            'token':token.key,
            '_id':user.pk,
            'email': user.email,
            'user_name': user.user_name,
        })



# Create your views here.
