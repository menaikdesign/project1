from rest_framework import serializers
from .models import Client, Note

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        read_only_fields = (
            'created_by',           
        )
            
        fields = (
            'id',
            'name',
            'contact_person',
            'email',
            'phone',
            'website', 
            'created_at',
            'modified_at',         
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'name',
            'body',
        )