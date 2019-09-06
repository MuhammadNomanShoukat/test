"""basic_signup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import SignUpCreateGenericView,Get_Data,SignUpUpdateGenericView,LoginAPIView

# ==================================== signup-api urls ================================================
urlpatterns = [
    # this url using to create or signup for user
    path('user-create/',SignUpCreateGenericView.as_view()),

    # this url updating a user
    path('user-update/<int:id>/',SignUpUpdateGenericView.as_view()),

    # this url displaying all data it based on user authentication admin can see the data no other users
    path('data/',Get_Data.as_view()),

    # this url using for login a user and return all details about user
    path('user-login/',LoginAPIView.as_view()),

    # this url for api authentication built-in function to access linke login,logout etc
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),

]
