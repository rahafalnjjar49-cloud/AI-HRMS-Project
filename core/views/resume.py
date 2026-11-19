import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Candidate, Resume
from ..serializers import ResumeSerializer
import logging

logger = logging.getLogger(__name__)

class UploadResumeAPIView(APIView):
    def post(self, request):
        try:
            candidate_id = request.data.get('candidate')
            uploaded_file = request.FILES.get('file')

            if not candidate_id or not uploaded_file:
                raise ValueError("Both candidate ID and file are required.")

            try:
                Candidate.objects.get(pk=candidate_id)
            except Candidate.DoesNotExist:
                return Response({"error": "Candidate does not exist."}, status=status.HTTP_404_NOT_FOUND)

            ext = os.path.splitext(uploaded_file.name)[1].lower()
            valid_extensions = ['.pdf', '.docx', '.txt']
            if ext not in valid_extensions:
                raise ValueError(f"Invalid file type. Only {', '.join(valid_extensions)} are allowed.")

            serializer = ResumeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Failed to upload resume: {e}")
            return Response({'error': 'An unexpected error occurred!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)