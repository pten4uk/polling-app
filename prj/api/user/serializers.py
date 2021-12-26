from rest_framework import serializers

from polls.models import (
    Poll,
    TextAnswer,
    ChoiceAnswer
)


class PollSerializer(serializers.ModelSerializer):
    text_questions = serializers.SerializerMethodField()
    choice_questions = serializers.SerializerMethodField()

    def get_text_questions(self, obj):
        return obj.text_questions.all().values('pk', 'text')

    def get_choice_questions(self, obj):
        return obj.choice_questions.all().values('pk', 'text', 'multiple')

    class Meta:
        model = Poll
        fields = [
            'title',
            'datetime_start',
            'datetime_end',
            'description',
            'text_questions',
            'choice_questions'
        ]


class TextAnswerCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TextAnswer
        fields = [
            'user',
            'question',
            'text'
        ]


class ChoiceAnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceAnswer
        fields = [
            'users'
        ]

    def validate(self, data):
        if data:
            return data
        raise serializers.ValidationError({"users": ["Обязательное поле"]})


class CompletedPollsSerializer(serializers.BaseSerializer):
    def add_answers_to_dict(self, data, answers_list, dict_key):
        for answer in answers_list:
            data[dict_key].append(
                {
                    'poll': answer.question.poll.pk,
                    'question': answer.question.pk,
                    'answer': answer.text
                }
            )

    def to_representation(self, user):
        choice_answers = user.choice_answers.all()
        text_answers = user.text_answers.all()

        data = {
            'user': user.pk,
            'choice_answers': [],
            'text_answers': []
        }

        self.add_answers_to_dict(data, choice_answers, 'choice_answers')
        self.add_answers_to_dict(data, text_answers, 'text_answers')

        return data
