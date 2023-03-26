from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from .models import Users
from .serial import UserSerial
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.decorators import permission_classes,authentication_classes


class CRUD(APIView):
    authentication_classes=[TokenAuthentication];
    permission_classes=[IsAuthenticated];
    def get(self,req,id=None):

        if id:
            try:
                user=Users.objects.get(pk=id)
                Jsonuser=UserSerial(user)
                return Response({'user':Jsonuser.data},status=status.HTTP_202_ACCEPTED)
            except:
                return Response({'msg':"user doesn't exists"},status=status.HTTP_400_BAD_REQUEST);
        else:
            try:
                users=Users.objects.all();
                DickUsrs=UserSerial(users,many=True)
                print(DickUsrs.data)
                return Response({'users':DickUsrs.data},status=status.HTTP_202_ACCEPTED);
            except:
                return Response({'msg':'No Data To Show'},status=status.HTTP_404_NOT_FOUND)

    def post(self,req):
        print(req.data)
        #converting json into the  python model object
        data=UserSerial(data=req.data)
        try:
            if data.is_valid():
                user=data.save();
                print('Newly Created User Id',user.id)
                #selecting the user
                USER=Users.objects.get(pk=user.id)
                #converting the model instance into the dictornary object.
                DickUser=UserSerial(USER);
                return Response({'msg':'Created','user':DickUser.data},status=status.HTTP_201_CREATED)

            else:
                raise serializers.ValidationError(data.errors)

        except serializers.ValidationError as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,req,id):

       print('Http Delete Method Has Been Called Deleting the user of id .............', id)
       DELUSERNAME={"username":Users.objects.get(pk=id).name}
       Users.objects.get(pk=id).delete();
       return Response({'msg':f'Deleted {DELUSERNAME}'},status=status.HTTP_202_ACCEPTED)

    def put(self,req,id=None):
        if id:
            try:
                user=Users.objects.get(pk=id)
                user_s=UserSerial(data=req.data,instance=user)
                if user_s.is_valid():
                    user.name=req.data['name']
                    user.crush=req.data['crush']
                    user.phone=req.data['phone']
                    user.save();
                    return Response({'msg':'sucessfully updated! '},status=status.HTTP_200_OK)
                else:
                    print(user_s.error_messages);
            except:
                pass;
        else:
            try:
                user_id=req.data['id']
                print('Here');
                print(type(req.data))
                print(req.data['name'],req.data['crush'],req.data['phone']);
                user=Users.objects.get(pk=user_id)
                user_s=UserSerial(data={"name":req.data['name'],"crush":req.data['crush'],"phone":req.data['phone']}, instance=user)
                #instance parameter tells serializer that this data is only for updation not for creating an object.
                if user_s.is_valid():
                    print('Is Valid')
                    user.name=req.data['name']
                    user.crush=req.data['crush']
                    user.phone=req.data['phone']
                    user.save();
                    return Response({'msg':'sucessfully updated! '},status=status.HTTP_200_OK)
                else:
                    print(user_s.error_messages);
            except:
                pass;

        return Response({'error':"data format should be in this format *If url include id params eg- api/3/* '{'name':'name','crush':'crush','phone':9435423423'} *Otherwise include id key value in body data* "},status=status.HTTP_404_NOT_FOUND)