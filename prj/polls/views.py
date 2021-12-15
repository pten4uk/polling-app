from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .models import Poll, TextQuestion, ChoiceQuestion, TextAnswer


class PollList(ListView):
    model = Poll
    context_object_name = 'polls'


class TextQuestionDetail(View):
    def get(self, request, *args, **kwargs):
        text_question = TextQuestion.objects.get(pk=kwargs['pk'])
        print(request.COOKIES)
        context = {
            'text_question': text_question
        }

        return render(request, 'polls/text_question_form.html', context)

    def post(self, request, *args, **kwargs):
        # TextAnswer.objects.create(
        #     text=request.POST['text_answer'],
        #     user=
        # )

        return redirect('poll_list')


class ChoiceQuestionDetail(View):
    def get(self, request, *args, **kwargs):
        choice_question = ChoiceQuestion.objects.get(pk=kwargs['pk'])
        context = {
            'choice_question': choice_question
        }
        return render(request, 'polls/choice_question_form.html', context)
