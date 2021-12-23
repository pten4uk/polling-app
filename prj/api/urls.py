from django.urls import path

from .user.views import *

urlpatterns = [
    path('get/active_polls/', GetActivePollsView.as_view()),  # GET
    path('get/completed_polls/', GetCompletedPolls.as_view()),  # GET

    path('create/text_answer/', CreateTextAnswerView.as_view()),  # CREATE

    path('update/choice_answer/<int:pk>', UpdateChoiceAnswerView.as_view()),  # PATCH
]
