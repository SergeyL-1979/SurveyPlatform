from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response

from survey.serializers import QuestionSerializer, AnswerSerializer, CheckQuestionSerializer
from survey.models import Question


class GetQuestion(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get(self, request, format=None):
        questions = Question.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        return Response(last_point.data)

    def get_queryset(self):
        pass


class QuestionAnswer(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})

    def get_queryset(self):
        pass


class CheckQuestionViewSet(generics.ListAPIView):
    serializer_class = CheckQuestionSerializer

    def post(self, request):

        return Response({'result': 'OK'})

    def get_queryset(self):
        pass

# class Survey():
#     def __init__(self, question):
#         self.rating = question
#         self.like = 0
#         self.dislike = 0
#
#     def like(self):
#         self.rating += 1
#         self.save()
#
#     def dislike(self):
#         self.rating -= 1
#         self.save()
#
#     def get_likes(self):
#         return self.like
