from rest_framework import serializers

from chat.models import Thread, Message


class ThreadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

    def create(self, validated_data):
        new_participants = validated_data['participants']
        new_participants = [user.id for user in new_participants]
        instance = Thread.objects.filter(participants__in=new_participants)
        if instance:
            return instance[0]
        return super().create(validated_data)


class ParticipantSerializer(serializers.Serializer):
    username = serializers.CharField()


class ThreadGetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    participants = ParticipantSerializer(many=True)


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageGetSerializer(serializers.Serializer):
    sender = serializers.CharField()
    text = serializers.CharField()
    thread = serializers.CharField()
    created = serializers.DateTimeField()
    is_read = serializers.BooleanField()


class MessageUpdateSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.is_read = True
        instance.save()
        return instance
