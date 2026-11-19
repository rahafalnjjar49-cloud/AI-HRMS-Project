from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer
import logging

logger = logging.getLogger(__name__)

class InterviewQuestionSetDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            question_set = InterviewQuestionSet.objects.get(pk=pk)
            serializer = InterviewQuestionSetSerializer(question_set)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except InterviewQuestionSet.DoesNotExist:
            return Response({"error": f"Interview question set with ID {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Failed to retrieve interview questions {pk}: {e}")
            return Response({'error': 'An unexpected error occurred!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)