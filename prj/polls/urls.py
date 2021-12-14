from django.contrib import admin
from django.urls import path, include

from polls.views import PollList

urlpatterns = [
    path('', PollList.as_view(), name='poll_list')
]
