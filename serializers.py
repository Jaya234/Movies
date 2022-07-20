#serializers are important because we are going to map all
#the values step by step
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    #now inside this we have to match each indiviual element.
    id = serializers.IntegerField(read_only= True) #read only
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    #the serializers has been created that is going to map
    #all the values
    
    
