from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.models import Profile

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):
    # follower_count = serializers.SerializerMethodField()

    # url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            # 'url',
        ]

    # def get_url(self, obj):
    #     return reverse_lazy("profiles:detail",
    #                         kwargs={'username': obj.username})


class ProfileModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'image']
