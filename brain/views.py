import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CareerPathRequestSerializer
from .services import generate_career_path
from .mocks import MOCK_CAREER_PATH_RESPONSE


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

        validated_data = serializer.validated_data
        is_test_mode = validated_data.pop("test_mode")
        if is_test_mode:
            time.sleep(
                5
            )  # so frontend devs can test their loading spinners/skeletons
            return Response(
                MOCK_CAREER_PATH_RESPONSE, status=status.HTTP_200_OK
            )

        try:
            # 2. Process via AI Service
            # We pass the clean, validated dictionary to our service
            career_plan_dict = generate_career_path(validated_data)

            # 3. Return the structured JSON
            return Response(career_plan_dict, status=status.HTTP_200_OK)

        except RuntimeError as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
