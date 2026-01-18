from rest_framework import serializers
from .models import Topic, Category, Post


class TopicSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=60)
    created = serializers.DateTimeField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
    
    def validate_name(self, value):
        # spacje też są akceptowalne
        value_temp = value.replace(' ','') 
        if not value_temp.isalpha():
            raise serializers.ValidationError(
                "Nazwa musi zawierać tylko litery!",
            )
        return value


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['id', 'title', 'text', 'topic', 'slug', 'created_at', 'updated_at', 'created_by']
        # lub jeżeli chcemy serializować wszystkie pola modelu
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']