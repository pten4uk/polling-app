from rest_framework import serializers

from polls.models import (
    Poll,
    TextQuestion,
    ChoiceQuestion,
    ChoiceAnswer
)


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class PollUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        exclude = ('datetime_start',)


class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuestion
        fields = (
            'text',
            'poll'
        )


class ChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceAnswer
        fields = ('text', )


class ChoiceQuestionSerializer(serializers.ModelSerializer):
    choice_answers = serializers.ListField()

    class Meta:
        model = ChoiceQuestion
        fields = (
            'text',
            'poll',
            'multiple',
            'choice_answers'
        )

    def pre_save(self, **kwargs):
        return ChoiceQuestion.objects.create(
            text=kwargs['text'],
            poll=kwargs['poll'],
            multiple=kwargs['multiple']
        )

    def validate(self, data):
        question = self.pre_save(**data)
        answers = []

        for answer in data['choice_answers']:
            answers.append(
                ChoiceAnswer.objects.create(
                    question=question,
                    text=answer
                )
            )

        data['choice_answers'] = answers
        return data
