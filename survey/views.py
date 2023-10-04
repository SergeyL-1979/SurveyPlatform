from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from survey.serializers import QuestionSerializer, AnswerSerializer
from survey.models import Question


class GetQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer

    def get(self, request, format=None):
        questions = Question.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        return Response(last_point.data)

    def get_queryset(self):
        pass


class QuestionAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})

    def get_queryset(self):
        pass
