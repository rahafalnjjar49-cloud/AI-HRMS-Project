from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Department, JobPosition
from ..serializers import JobPositionSerializer
import logging

logger = logging.getLogger(__name__)


class CreateJobPositionAPIView(APIView):
    def post(self, request):
        try:
            department_id = request.data.get('department')
            if department_id:
                try:
                    Department.objects.get(pk=department_id)
                except Department.DoesNotExist:
                    return Response(
                        {"error": f"Department with ID {department_id} does not exist."},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            serializer = JobPositionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Failed to create job position: {e}")
            return Response({'error': 'An unexpected error occurred!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)