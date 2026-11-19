from django.contrib import admin
from .models import Candidate,Department,InterviewQuestionSet,JobPosition,Resume,ScreeningResult
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','created_at')
    list_filter = ('full_name','email','phone','created_at')
    search_fields = ('full_name','email','phone','created_at')
    ordering = ('full_name','email','phone','created_at')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at')
    list_filter = ('name','created_at')
    search_fields = ('name',)
    ordering = ('name','created_at')

@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('department','title','created_at')
    list_filter= ('department','created_at')
    search_fields = ('department','title')
    ordering = ('department','title','created_at')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('candidate','uploaded_at')
    search_fields = ('candidate','uploaded_at')
    list_filter= ('candidate','uploaded_at')
    ordering = ('candidate','uploaded_at')
@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = ('candidate','job_position','score','recommendation')
    search_fields = ('candidate','job_position','score','recommendation')
    list_filter = ('recommendation','job_position')
@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ('candidate','job_position','generated_at')
    search_fields = ('candidate','job_position','generated_at')
    list_filter = ('candidate','job_position','generated_at')




# Register your models here.
