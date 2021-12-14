from django.shortcuts import render
from django.views.generic import ListView

from polls.models import Poll


class PollList(ListView):
    model = Poll
    context_object_name = 'polls'
