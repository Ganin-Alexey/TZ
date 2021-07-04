from rest_framework import serializers

from .models import *


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['pk', 'title' ]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )
    class Meta:
        model = Question
        fields = ('id', 'text', 'type', 'choices')


class InterrogationSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Interrogation
        fields = ('id', 'title', 'description', 'questions')


class AnswerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'



class InterrogationAnsweredSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.text')
    interrogation = serializers.CharField(source='interrogation.title')

    class Meta:
        model = Answer
        fields = ('id', 'user', 'choice', 'question', 'interrogation')


class CharFieldSerializer(serializers.Serializer):
    interrogation__title = serializers.CharField()


class AnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()
    question_id = serializers.JSONField()
    interrogation_id = serializers.JSONField()
    def validate_answers(self, answers):

        if not answers:
            raise serializers.ValidationError("Answers must be not null.")
        return answers

    def save(self):
        answers = self.data['answers']
        question_id = self.data['question_id']
        interrogation_id = self.data['interrogation_id']
        interrogation = Interrogation.objects.get(id=interrogation_id)
        question = Question.objects.get(id=question_id)
        return [answers, question, interrogation]