from django.db import models
from .candidate import Candidate
class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='resume')
    file = models.FileField(upload_to='resume/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Resum of {self.candidate.full_name}"
