from rest_framework import serializers
from ..models import InterviewQuestionSet
class InterviewQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestionSet
        fields = '__all__'
        read_only_fields = ['technical_questions','behavioral_questions','follow_up_questions','generated_at']
