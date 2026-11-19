from rest_framework import serializers
from ..models import ScreeningResult
class ScreeningResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningResult
        fields = '__all__'
        read_only_fields = ['score','strengths','missing_skills','recommendation','summary','raw_report','generated']


