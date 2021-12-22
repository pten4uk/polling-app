from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from polls.models import Poll, TextAnswer
from .serializers import PollSerializer, TextAnswerCreateSerializer

User = get_user_model()


class GetActivePollsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class CreateTextAnswerView(CreateAPIView):
    serializer_class = TextAnswerCreateSerializer
    queryset = TextAnswer.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)