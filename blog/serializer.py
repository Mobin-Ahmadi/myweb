from rest_framework import serializers
from .models import Post,Comment


class CommentSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['name']

    def create(self, validated_data):
        validated_data['name'] = self.context['request'].user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many=True,read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'