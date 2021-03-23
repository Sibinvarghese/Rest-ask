from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import UserRegistration as UR
from .models import CustomerSupport as CS
from .serializers import RegisterSerializer,CustomerSupportSerializer
# Create your views here.

#api/Signup =>list all and Create
class UserSignup(APIView):

    def get(self,request):
        usersignup=UR.objects.all()
        serializer=RegisterSerializer(usersignup,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#api/signin  => signin
class UserSignIn(APIView):
    model=UR
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = IsAuthenticated

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#api/edit/id  =>get the current user and edit the datas
class UserDetails(APIView):
    model=UR

    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return UR.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        getdetails=self.get_object(pk)
        serializer=RegisterSerializer(getdetails)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        getdetails=self.get_object(pk)
        serializar=RegisterSerializer(getdetails,data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializar.data,status=status.HTTP_400_BAD_REQUEST)

#api/customer  =>create customer
class CustomerSupportView(APIView):
    model=CS
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get(self,request):
        support=self.model.objects.all()
        serializer=CustomerSupportSerializer(support,many=True)
        return Response(serializer.data)


    def post(self,request,formaat=None):
        serializer = CustomerSupportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#api/list  => list of all customer support request
class ListCustomerSupportRequests(APIView):
    model=CS

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get(self, request):
        support = self.model.objects.all()
        serializer = CustomerSupportSerializer(support, many=True)
        return Response(serializer.data)



