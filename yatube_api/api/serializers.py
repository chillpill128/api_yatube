from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Group, Post


class GroupSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerialazer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerialazer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
