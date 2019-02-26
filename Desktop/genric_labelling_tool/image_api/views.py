from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import glt
from .serializers import gltSerializer
from rest_framework.renderers import JSONRenderer
import os,glob
from google.cloud import storage
import base64
from config import *
from utils import *
#import env variables from config

class gltList(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self,request):
        global num
        storage_client = storage.Client.from_service_account_json(
                'eduwaivecommon-01cac388cb6b.json')
        bucket = storage_client.get_bucket('eduwaivesgditium')
        inp_params=request.data.keys()
        if 'client' not in inp_params:
            return Response({"status":"Invalid Client"})


        blobs = bucket.list_blobs(prefix='Samples/')
        sorted_blobs = sorted(blobs, key=lambda x: x.updated, reverse=True)
        if 'limit' in inp_params:
            num=request.data['limit']

        #if 'to' in inp_params and 'from' in inp_params:
        try:
            sorted_blobs=[blob for blob in sorted_blobs if str(blob.updated).split(" ")[0] >= request.data['from']\
                and str(blob.updated).split(" ")[0] <= request.data['to']]
            links=urls(sorted_blobs,num)
            status='200 OK'
        except:
            
        #elif 'to' not in inp_params:
            try:
                sorted_blobs=[blob for blob in sorted_blobs if str(blob.updated).split(" ")[0]>=request.data['from']]
                links=urls(sorted_blobs,num)
                status='Inavlid Request'
            except:
                #elif 'from' not in inp_params:
                try:
                    sorted_blobs=[blob for blob in sorted_blobs if str(blob.updated).split(" ")[0]<=request.data['to']]
                    sorted_blobs=sorted_blobs[:-num]
                    links=urls(sorted_blobs,num)
                    status='Inavlid Request'
                except:
                    links=urls(sorted_blobs,num)
                    status='Inavlid Request'

        return Response({'status':status,'Data':links})
        

    def post(self,request):
        pass