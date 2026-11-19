from django.db import models
from .department import Department
class JobPosition(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='job_position')
    title = models.CharField(max_length=150)
    description = models.TextField()
    required_skills =models.JSONField(default=list,help_text="List of required skills")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title