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


class ChoiceAnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceAnswer
        fields = [
            'users'
        ]
