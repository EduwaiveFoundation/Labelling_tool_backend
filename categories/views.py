from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import category
from .serializers import categorySerializer
from rest_framework.renderers import JSONRenderer
from .models import labelled_img
from .serializers import labelled_imgSerializer
import os,glob
# Create your views here.


class categoryList(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self,request):
        categories=category.objects.all();
        serializer=categorySerializer(categories,many=True)
        
        print(serializer.data)
        return Response(serializer.data)

    def post(self,request):
        for data in request.data:
            serializer = categorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print (serializer.data)
            else:
                return Response(serializer.errors, status=400)
        return Response({"response":"Sucess"}, status=201)
        

class labelled_imgList(APIView):
    renderer_classes = (JSONRenderer, )
    def get_files(self,directory):
        dir_ = list(map(lambda x: x if not x.startswith('.') else '', os.listdir(directory)))
        if '' in dir_:
            dir_.remove('')
        return {d:glob.glob('{}/{}/*.jpg'.format(directory, d)) for d in dir_}
            
    def get(self,request):
        labelled_images=labelled_img.objects.all();
        serializer=labelled_imgSerializer(labelled_images,many=True)
        dir=self.get_files("/home/sunpriya/Desktop/output")
        print(serializer.data)
        return Response({'labell':serializer.data,
                            'directory_paths':dir})

