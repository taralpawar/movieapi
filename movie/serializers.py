from rest_framework import serializers
from .models import MovieList


class movieSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieList
        fields = '__all__'


# class watchSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Watch
#         fields = '__all__'

# class popularSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PopularList
#         fields = '__all__'

# class latestSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = LatestList
#         fields = '__all__'
