from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', PollList.as_view(), name='poll_list'),
    path('mypolls/', UserPolls.as_view(), name='user_polls'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),

    path('text_question/<int:pk>', TextQuestionDetail.as_view(), name='text_question'),
    path('choice_question/<int:pk>', ChoiceQuestionDetail.as_view(), name='choice_question'),
]
