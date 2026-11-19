from django.db import models
from .candidate import Candidate
from .jobPosition import JobPosition
from django.core.validators import MinValueValidator, MaxValueValidator


class ScreeningResult(models.Model):
    class RecommendationChoices(models.TextChoices):
        PROCEED= 'proceed' , 'Proceed'
        HOLD= 'hold' , 'Hold'
        REJECT= 'reject' , 'Reject'

    candidate =models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='screening_result')
    job_position =models.ForeignKey(JobPosition, on_delete=models.CASCADE, related_name='screening_result')

    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Score from 0 to 100"
    )
    strengths =models.JSONField(default=list, help_text="List of candidate's strengths")
    missing_skills=models.JSONField(default=list, help_text="List of candidate's missing skills")
    recommendation =models.CharField(
        max_length=10,
        choices=RecommendationChoices.choices,
        default=RecommendationChoices.HOLD,
    )
    summary=models.TextField(help_text="Summary of the screening result")
    raw_report=models.JSONField(help_text="Raw report of the screening result")
    generated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"screening result for: {self.candidate.full_name} - score {self.score} "

