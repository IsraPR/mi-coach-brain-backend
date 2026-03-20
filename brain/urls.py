# assistant/urls.py
from django.urls import path
from .views import CareerPathAPIView

urlpatterns = [
    path(
        "career-path/",
        CareerPathAPIView.as_view(),
        name="career-path-feedback",
    ),
]
