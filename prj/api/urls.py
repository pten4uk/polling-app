from django.urls import path, include

from .admin.views import *
from .user.views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('get/active_polls/', GetActivePollsView.as_view()),  # GET
    path('get/completed_polls/', GetCompletedPollsView.as_view()),  # GET

    path('create/poll/', CreatePollView.as_view()),  # CREATE
    path('create/choice_question/', CreateChoiceQuestionView.as_view()),  # CREATE
    path('create/text_question/', CreateTextQuestionView.as_view()),  # CREATE
    path('create/text_answer/', CreateTextAnswerView.as_view()),  # CREATE

    path('update/poll/<int:pk>', UpdatePollView.as_view()),  # PUT, PATCH
    path('update/choice_answer/<int:pk>', UpdateChoiceAnswerView.as_view()),  # PUT, PATCH
    path('update/text_question/<int:pk>', UpdateTextQuestionView.as_view()),  # PATCH
    path('update/choice_answer/<int:pk>/add_user', AddUserToChoiceAnswerView.as_view()),  # PATCH

    path('delete/poll/<int:pk>', DeletePollView.as_view()),  # DELETE
    path('delete/choice_answer/<int:pk>', DeleteChoiceAnswerView.as_view()),  # DELETE
    path('delete/text_question/<int:pk>', DeleteTextQuestionView.as_view()),  # DELETE
]
