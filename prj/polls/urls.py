from django.contrib import admin
from django.urls import path, include

from .views import PollList, TextQuestionDetail, ChoiceQuestionDetail

urlpatterns = [
    path('', PollList.as_view(), name='poll_list'),
    path('text_question/<int:pk>', TextQuestionDetail.as_view(), name='text_question'),
    path('choice_question/<int:pk>', ChoiceQuestionDetail.as_view(), name='choice_question'),
]
