from django.urls import path

from survey import views

urlpatterns_survey = [
    path('notes/', views.GetQuestion.as_view()),
    path('answer/', views.QuestionAnswer.as_view()),
    path('check/', views.CheckQuestionViewSet.as_view()),
]
