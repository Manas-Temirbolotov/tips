from django.shortcuts import render
from rest_framework import views
from rest_framework import viewsets
from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

    # def get(self, request, *args, **kwargs):
    #     question = QuestionAnswer.objects.get(id=kwargs.get('question_id'))
    #     status = Status.objects.get(slug=kwargs.get('slug'))
    #     news_status = NewsStatus.objects.create(
    #         status=status,
    #         news =news,
    #         author=request.user.author
    #     )
    #     return Response ({'message': 'Status added'}, status=201)
