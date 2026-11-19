from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer
import logging

logger = logging.getLogger(__name__)

class ScreeningResultDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            result = ScreeningResult.objects.get(pk=pk)
            serializer = ScreeningResultSerializer(result)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ScreeningResult.DoesNotExist:
            return Response({"error": f"Screening result with ID {pk} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Failed to retrieve screening result {pk}: {e}")
            return Response({'error': 'An unexpected error occurred!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)