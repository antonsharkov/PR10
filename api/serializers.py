from rest_framework import serializers

class ZamenaSerializer(serializers.Serializer):
    array = serializers.CharField()
    s1 = serializers.IntegerField()
    s2 = serializers.IntegerField()
    result = serializers.ListField()