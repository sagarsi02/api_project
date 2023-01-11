from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import generics, status


class createuser(APIView):

    def post(request, *args, **kwargs):
        try:
            body = request.request.data

            if body.get('username', ''):
                username = body['username']
                email = body['email']
                password = body['password']
                c_password = body['c_password']
            

                if password == c_password:
                    if User.objects.filter(email=email).exists():
                        response = {"Warning": f"Already Register"}
                        return Response(response, status=status.HTTP_202_ACCEPTED)
                    elif User.objects.filter(username=username).exists():
                        response = {"Warning": f"username is already taken"}
                        return Response(response, status=status.HTTP_202_ACCEPTED)
                    else:
                        usr = User.objects.create_user(username=username, email=email, password=password)
                        usr.save();
                        response = {"Success": f"Successfully Registered"}
                        return Response(response, status=status.HTTP_200_OK)
                        
                else:
                    response = {"Error": f"Password do not Matche"}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except:
            response = {"Error": f"Invalid Credentials"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class login(APIView):
    def post(request, *args, **kwargs):

        try:
            body = request.request.data

            if body.get('username', ''):
                username = body['username']
                password = body['password']
                
                user = auth.authenticate(username=username, password=password)
                
                if user is not None:
                    auth.login(request.request, user)
                    response = {"Success": f"Logged in"}
                    return Response(response, status=status.HTTP_202_ACCEPTED)
                else:
                    response = {"Error": f"User Not Exist"}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            return HttpResponse('Invalid Credentials')

class logout(APIView):
    def post(request):
        auth.logout(request)
        response = {"Success": f"Logout Successfully"}
        return Response(response, status=status.HTTP_202_ACCEPTED)
