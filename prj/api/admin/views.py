from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    PollSerializer,
    PollUpdateSerializer,
    ChoiceQuestionSerializer,
    TextQuestionSerializer,
    ChoiceAnswerSerializer,
)

from polls.models import (
    Poll,
    ChoiceQuestion,
    ChoiceAnswer,
    TextQuestion
)


class CreatePollView(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PollSerializer


class UpdatePollView(UpdateAPIView):
    serializer_class = PollUpdateSerializer
    queryset = Poll.objects.all()
    permission_classes = [permissions.IsAdminUser]


class DeletePollView(DestroyAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CreateChoiceQuestionView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = ChoiceQuestionSerializer(data=request.data)
        serializer.is_valid()
        return Response(
            data={"status": "201 Created"},
            status=201
        )


class UpdateChoiceAnswerView(UpdateAPIView):
    serializer_class = ChoiceAnswerSerializer
    queryset = ChoiceAnswer.objects.all()
    permission_classes = [permissions.IsAdminUser]


class DeleteChoiceAnswerView(DestroyAPIView):
    serializer_class = ChoiceAnswerSerializer
    queryset = ChoiceAnswer.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CreateTextQuestionView(CreateAPIView):
    serializer_class = TextQuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateTextQuestionView(UpdateAPIView):
    serializer_class = TextQuestionSerializer
    queryset = TextQuestion.objects.all()
    permission_classes = [permissions.IsAdminUser]


class DeleteTextQuestionView(DestroyAPIView):
    serializer_class = TextQuestionSerializer
    queryset = TextQuestion.objects.all()
    permission_classes = [permissions.IsAdminUser]
