from django.db import models
from .candidate import Candidate
from .jobPosition import JobPosition
from .screeningResult import ScreeningResult
class InterviewQuestionSet(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    screening_result = models.OneToOneField(ScreeningResult, on_delete=models.CASCADE,related_name='interview_question_set')
    technical_questions=models.JSONField(default=list)
    behavioral_questions = models.JSONField(default=list)
    follow_up_questions =models.JSONField(default=list)
    generated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Interview Questions for {self.candidate.full_name}"


