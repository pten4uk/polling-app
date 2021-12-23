from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Poll, TextAnswer, ChoiceAnswer
from .serializers import (
    PollSerializer,
    TextAnswerCreateSerializer,
    ChoiceAnswerUpdateSerializer,
    CompletedPollsSerializer
)

User = get_user_model()


class GetActivePollsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class GetCompletedPolls(APIView):
    def get(self, request):
        serializer = CompletedPollsSerializer(request.user)
        return Response(serializer.data)


class CreateTextAnswerView(CreateAPIView):
    serializer_class = TextAnswerCreateSerializer
    queryset = TextAnswer.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateChoiceAnswerView(UpdateAPIView):
    serializer_class = ChoiceAnswerUpdateSerializer
    queryset = ChoiceAnswer.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch']

    def perform_update(self, serializer):
        users_to_add = serializer.validated_data['users']
        obj = self.get_object()
        obj.users.add(*users_to_add)
        obj.save()