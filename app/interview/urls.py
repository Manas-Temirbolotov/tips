from django.contrib import admin
from django.urls import path, include
from interview import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categorys/', views.CategoryViewSet.as_view()),
    path('api/categorys/<int:pk>/', views.CategoryViewSet.as_view()),
    path('api/questions/', views.QuestionAnswerViewSet.as_view()),
    path('api/questions/<int:pk>/', views.QuestionAnswerViewSet.as_view()),
    path('api/questions/category/<int:pk>/', views.QuestionAnswerViewSet.as_view()),

    ]