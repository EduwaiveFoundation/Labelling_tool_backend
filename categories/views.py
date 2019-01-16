from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import category
from .serializers import categorySerializer
from rest_framework.renderers import JSONRenderer
from .models import labelled_img
from .serializers import labelled_imgSerializer
# Create your views here.


class categoryList(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self,request):
        categories=category.objects.all();
        serializer=categorySerializer(categories,many=True)
        
        print(serializer.data)
        return Response(serializer.data)

    def post(self):
        pass
class labelled_imgList(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self,request):
        labelled_images=labelled_img.objects.all();
        serializer=labelled_imgSerializer(labelled_images,many=True)
        
        print(serializer.data)
        return Response(serializer.data)

    def post(self,request,data):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print (serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        