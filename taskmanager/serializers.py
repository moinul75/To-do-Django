from rest_framework import serializers
from .models import * 


class TodoSerializer(serializers.ModelSerializer):
    #meta and inside meta model and fields 
    class Meta:
        model = Todo
        fields = ('id','title','description','completed')
    