from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import SignUpModel
from django.contrib.auth.admin import User
from .serializers import SignUpSerializer,LoginSerializer_Data
from rest_framework import generics,mixins
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login


# ================================================== Generic CreateAPIView class =====================================
class SignUpCreateGenericView(generics.CreateAPIView):
    queryset = SignUpModel.objects.all()
    serializer_class = SignUpSerializer

    # this function getting the data and generating token and also returning back user or token
    def post(self, request, *args, **kwargs):

        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token,create = Token.objects.get_or_create(user=user)
            context = {
                'User-name :': str(token.user),
                'Token :':str(token.key),
            }
            return Response(context, status=200)

# ========================== Generic UpdateAPIView class base on mixins ============================================
class SignUpUpdateGenericView(generics.UpdateAPIView,
                              mixins.UpdateModelMixin,
                              mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              ):
    queryset = SignUpModel
    serializer_class = SignUpSerializer
    lookup_field = "id"

    # this function returning all data or selected data "ID" base
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    # this function inserting new data or creating new user
    def post(self,request,id=None):
        return self.create(request)

    # this function updating existing with "ID"
    def put(self,request,id=None):
        return self.update(request,id)

    # this function delete existing user with "ID"
    def delete(self,request,id=None):
        return self.destroy(request,id)


# =========================================== LoginAPIView Class =============================================
class LoginAPIView(APIView):

    # this function using to validate the user and getting the user detail along username and returning back all data
    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer_Data(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request,user)
        token,created = Token.objects.get_or_create(user=user)
        all_data = SignUpModel.objects.get(username=token.user)

        context = {
            'username :':all_data.username,
            'first_name :':all_data.first_name,
            'last_name :':all_data.last_name,
            'email :':all_data.email,
            'password :':all_data.password,
            'semester :':all_data.semester,
            'cgpa :':all_data.cgpa,
            'uni :':all_data.uni,
            'phone :':all_data.phone,
            'address :':all_data.address,
            "token key :": token.key,
        }

        return Response(context,status=200)


# ==================================APIView class showing all data=============================
class Get_Data(APIView):

    #                         Authentication and Permission classes below
    # ==============================================================================================
    permission_classes = [IsAuthenticated,IsAdminUser]
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # ==============================================================================================

    # this showing all the user data is user is authenticate
    def get(self,request):
        data = SignUpModel.objects.all()
        serializer = SignUpSerializer(data,many=True)
        return Response(serializer.data,status=200)





