from django.urls import path
from .views.department import CreateDepartmentAPIView
from .views.jobPosition import CreateJobPositionAPIView
from .views.candidate import CreateCandidateAPIView
from .views.resume import UploadResumeAPIView
from .views.screeningResult import ScreeningResultDetailAPIView
from .views.interviewQuestionSet import InterviewQuestionSetDetailAPIView

urlpatterns = [
    path('departments/create/', CreateDepartmentAPIView.as_view(), name='create_department'),
    path('job-positions/create/', CreateJobPositionAPIView.as_view(), name='create_job_position'),
    path('candidates/create/', CreateCandidateAPIView.as_view(), name='create_candidate'),
    path('resumes/upload/', UploadResumeAPIView.as_view(), name='upload_resume'),
    path('screening-results/<int:pk>/', ScreeningResultDetailAPIView.as_view(), name='screening_result_detail'),
    path('interview-questions/<int:pk>/', InterviewQuestionSetDetailAPIView.as_view(), name='interview_questions_detail'),
]