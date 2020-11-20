from rest_framework import serializers

from ..models import Poll, Question


class PollSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Poll
        fields = [
            'id', 'name', 'start_date', 'expiration_date', 'description'
        ]


class QuestionSerializer(serializers.ModelSerializer):

    poll = serializers.PrimaryKeyRelatedField(queryset=Poll.objects)
    text = serializers.CharField(required=True)
    answer_type = serializers.CharField(required=True)
    votes = serializers.IntegerField(required=True)

    class Meta:
        model = Question
        fields = '__all__'
