from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import glt
from .serializers import gltSerializer
from rest_framework.renderers import JSONRenderer

import os,glob
from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import base64
import time

class gltList(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self,request):
        creds = ServiceAccountCredentials.from_json_keyfile_name('/home/sunpriya/Downloads/eduwaivecommon-01cac388cb6b.json')
        client_id = creds.service_account_email
        delimiter='/'

        GOOGLE_ACCESS_STORAGE_ID='devsunpriya@eduwaivecommon.iam.gserviceaccount.com'
        current=int(time.time())
        EXPIRATION=str(current+3600)


        storage_client = storage.Client.from_service_account_json(
                '/home/sunpriya/Downloads/eduwaivecommon-01cac388cb6b.json')
        bucket = storage_client.get_bucket('eduwaivesgditium')

        blobs = bucket.list_blobs(prefix='Samples/')
        links=[]
        print('Blobs:')
        for blob in blobs:
            
            sign_string='GET\n'+"\n"+"\n"+EXPIRATION+"\n"+"/eduwaivesgditium/"+blob.name
            print(sign_string)
            signature = creds.sign_blob(sign_string)[1]
            encoded_signature = base64.b64encode(signature).decode('utf-8')\
                .replace("+","%2B").replace("/","%2F").replace("=",'%3D')
            base_url="https://storage.googleapis.com/eduwaivesgditium/"+blob.name+\
                "?GoogleAccessId=" + GOOGLE_ACCESS_STORAGE_ID + "&Expires=" +\
                     EXPIRATION + "&Signature=" + encoded_signature  
            links.append(base_url)
        return Response(links)
        

    def post(self,request):
        pass