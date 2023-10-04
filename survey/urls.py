from django.urls import path

from survey import views

urlpatterns = [
    path('', views.GetQuestion.as_view()),
    path('answer/', views.QuestionAnswer.as_view()),
]
