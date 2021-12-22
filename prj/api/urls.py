from django.urls import path

from .views import *

urlpatterns = [
    path('get/active_polls/', GetActivePollsView.as_view()),

    path('create/text_answer/', CreateTextAnswerView.as_view()),
]
