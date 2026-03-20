# assistant/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CareerPathRequestSerializer
from .services import generate_career_path


class CareerPathAPIView(APIView):
    """
    POST /ai-api/career-path/
    Analyzes user skills and feedback to generate a structured career progression map.
    """

    def post(self, request):
        # 1. Validate Input
        serializer = CareerPathRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 2. Process via AI Service
            # We pass the clean, validated dictionary to our service
            career_plan_dict = generate_career_path(serializer.validated_data)

            # 3. Return the structured JSON
            return Response(career_plan_dict, status=status.HTTP_200_OK)

        except RuntimeError as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
