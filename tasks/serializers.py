from rest_framework import serializers 
from tasks.models import Tasks, Comments
 
 

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('comment',
                  'user',
                  'task')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('title',
                  'description',
                  'user',
                  'comment')
        read_only_fields =  ('comment',)

