from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Report, Activity

from django.core.exceptions import SuspiciousOperation
from django.contrib.gis.geos import Point

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'reports')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ActivityRelatedField(serializers.RelatedField):
    queryset = Activity.objects.all()

    def to_representation(self, value):
        return [value.id, str(value)]

    def to_internal_value(self, data):
        try:
            acti = Activity.objects.get(id=data)
            return acti
        except Activity.DoesNotExist:
            raise SuspiciousOperation("Invalid activity send")


class GeoPointField(serializers.Field):
    """
    Representation of a GeoDjango Point with lat and long separately
    """
    def to_representation(self, obj):
        return {'lon':obj.x, 'lat':obj.y}

    def to_internal_value(self, data):
        try:
            return Point(float(data['lon']), float(data['lat']), srid=4326)
        except:
            raise SuspiciousOperation("Invalid geolocalization information send")


class ReportSerializer(serializers.ModelSerializer):
    #activity = serializers.StringRelatedField(many=False)
    activity = ActivityRelatedField(many=False)
    pos = GeoPointField()
    class Meta:
        model = Report
        fields = ('pos', 'activity',)

class Signup(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:

        model = User
        fields = ('id', 'username', 'email', 'password')



