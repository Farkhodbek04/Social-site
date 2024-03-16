from rest_framework.serializers import ModelSerializer

from main import models


class MyModelSerializer(ModelSerializer):
    class Meta:
        model = models.MyModel
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserRelationSerializer(ModelSerializer):
    class Meta:
        model = models.UserReletion
        fieldsc = '__all__'


class ChatSerializer(ModelSerializer):

    class Meta:
        model = models.Chat
        fields = '__all__'


class MessageSerializer(ModelSerializer):

    class Meta:
        model = models.Message
        fields = '__all__'


# Post CRUD serailizer
        
class PostFilesSerializer(ModelSerializer):
    class Meta:
        model = models.PostFiles
        fields = '__all__'

class PostSerializer(ModelSerializer):
    post_files = PostFilesSerializer(many=True)
    class Meta:
        model = models.Post
        fields = '__all__'

