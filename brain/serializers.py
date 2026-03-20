from rest_framework import serializers


class ActivitySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    type = serializers.CharField()


class StepSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    activities = ActivitySerializer(many=True)


class SkillSerializer(serializers.Serializer):
    skill = serializers.CharField()
    score = serializers.IntegerField(min_value=0, max_value=10)
    type = serializers.CharField()


class FeedbackRequestedSerializer(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()
    value = serializers.FloatField()
    num_skills_with_value = serializers.IntegerField()


class FeedbackSerializer(serializers.Serializer):
    feedback = serializers.CharField()
    requested = FeedbackRequestedSerializer(many=True)


class AchievementSerializer(serializers.Serializer):
    name = serializers.CharField()
    earned_date = serializers.DateTimeField()
    has_certificate = serializers.BooleanField()


class CareerPathRequestSerializer(serializers.Serializer):
    """Main input serializer for the endpoint."""

    current_role = serializers.CharField()
    target_role = serializers.CharField()
    available_steps = StepSerializer(many=True)
    user_skills = SkillSerializer(many=True)
    feedback_360 = FeedbackSerializer(many=True)
    achievements = AchievementSerializer(many=True)
