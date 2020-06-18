from django.contrib.auth.models import User
from django.forms import ImageField
from rest_framework import serializers, request
from discussions.models import Discussion, Comment, CATEGORY_TYPE
from django.contrib.auth.models import User


class DiscussionSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(allow_null=True, required=False)
    user = serializers.CharField(read_only=True, required=False)
    timestamp = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=130, required=True)
    slug = serializers.CharField(read_only=True)
    content = serializers.CharField(required=True, max_length=1500)
    img = serializers.ImageField(required=False, use_url=True)
    category = serializers.ChoiceField(default='Others', choices=CATEGORY_TYPE)
    tags = serializers.CharField(required=False, allow_blank=False)
    views = serializers.IntegerField(required=False, read_only=True)
    votes = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].write_only = True

    def get_votes(self, obj):
        return obj.votes.count()

    class Meta:
        model = Discussion
        fields = ('user_id', 'user', 'title', 'slug', 'timestamp', 'updated', 'content', 'img', 'category', 'tags', 'views', 'votes')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'timestamp', 'content')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']