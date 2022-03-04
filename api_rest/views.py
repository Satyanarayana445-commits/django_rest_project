from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins
# from rest_framework.authentication import sessionAuthentication,basicAuthentication
# from rest_framework.permissions import IsAuthenticated
import os
current_file_path = os.path.dirname(__file__)



print('path_1',current_file_path)
class GenericView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    def get(self,request,id=None):
        return self.list(request)
    def post(self,request,id=None):
        return self.create(request)
    def put(self,request,id=None):
        return self.update(request,id)
    def delete(self,request,id=None):
        return self.destroy(request,id)

# Create your views here.
class ArticleAPIView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = 401)

@api_view(['GET','PUT','DELETE'])
def article_update(request,pk):
    article = Article.objects.get(pk=pk)
    serializer = ArticleSerializer(article)
    if request.method == "PUT":
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        print('hiii')
        article.delete()
        return JsonResponse({"message":"Successfully deleted"},status = 401)
    return Response(serializer.data)


class ArticleDetails(APIView):
    def get_object(self,pk):
        return Article.objects.get(pk=pk)

    def get(self,request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk):
        article = self.get_object(pk)
        article.delete()
        return JsonResponse({"message":"successfully deleted"})