from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import UserSerializer

class StatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Status
        fields = ['id', 'user', 'content', 'image']
        read_only_fields = ['user']

    def validate_content(self, value):
        # print('value----', value)
        if len(value) > 30000:
            raise serializers.ValidationError('Content is too long')
        return value

    def validate(self, data):
        # print('data----', data)
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Both content and image can not be empty')
        return data
