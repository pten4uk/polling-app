from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import RegisterForm
from .models import *

User = get_user_model()


class PollList(LoginRequiredMixin, ListView):
    model = Poll
    context_object_name = 'polls'


class UserPolls(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        text_answers = request.user.text_answers.all()
        choice_answers = request.user.choice_answers.all()

        context = {
            'text_answers': text_answers,
            'choice_answers': choice_answers
        }

        return render(request, 'polls/user_polls.html', context)


class TextQuestionDetail(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        text_question = TextQuestion.objects.get(pk=kwargs['pk'])

        context = {
            'text_question': text_question
        }

        return render(request, 'polls/text_question_form.html', context)

    def post(self, request, *args, **kwargs):
        text_question = TextQuestion.objects.get(pk=kwargs['pk'])

        TextAnswer.objects.create(
            text=request.POST['text_answer'],
            user=request.user,
            question=text_question
        )

        return redirect('poll_list')


class ChoiceQuestionDetail(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        choice_question = ChoiceQuestion.objects.get(pk=kwargs['pk'])

        context = {
            'choice_question': choice_question
        }

        return render(request, 'polls/choice_question_form.html', context)

    def post(self, request, *args, **kwargs):
        choice_question = ChoiceQuestion.objects.get(pk=kwargs['pk'])
        choice_answers = ChoiceAnswer.objects.filter(question=choice_question)

        for answer in choice_answers:
            if str(answer.pk) in request.POST.getlist('choice_answer'):
                answer.users.add(request.user)
                answer.save()

        return redirect('poll_list')


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = '/'
    template_name = 'signup.html'
