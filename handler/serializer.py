from rest_framework.serializers import ModelSerializer
from .models import Twitter_Profiles


class Twitter_Profiles_Serializer(ModelSerializer):
    class Meta:
        model = Twitter_Profiles
        fields = [
            "username",
            "name",
            "description",
            "profile_image_url",
            "url",
        ]
