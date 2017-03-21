from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, ReportSerializer, Signup
from .models import Report

from django.contrib.gis.geos import GEOSGeometry


class UserCreate(generics.CreateAPIView):

    permission_classes = ()
    deserializer_class = Signup
    serializer_class   = UserSerializer

    def create(self, request, *args, **kwargs):
        deserializer = self.deserializer_class(data = request.data)
        deserializer.is_valid(raise_exception = True)

        saved = self.perform_create(deserializer)
        serializer = self.serializer_class(saved, context={'request': request})

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """
        Get reports
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def list(self, request):
        if request.data.get('lon') and request.data.get('lat'):
            ptn = GEOSGeometry('POINT('+request.data.get('lon')+ ' '+request.data.get('lat')+')', 4326)

            queryset = Report.objects.filter(pos__distance_lte=(pnt, D(km=7)))


