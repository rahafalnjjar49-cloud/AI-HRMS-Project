from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Candidate
from ..serializers import CandidateSerializer
import logging

logger = logging.getLogger(__name__)

class CreateCandidateAPIView(APIView):
    def post(self, request):
        try:
            serializer = CandidateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Failed to create candidate: {e}")
            return Response({'error': 'An unexpected error occurred!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)