from rest_framework import viewsets, generics, mixins, status
from .models import Projects
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.projects.serializers import ProjectSerializer
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
)
from .renderers import ProjectJSONRenderer
from django.shortcuts import render
# import logging
# logger = logging.getLogger(__name__)
# logger.error(renderer_classes)
# from django.http import HttpResponse

class ProjectListView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

class ProjectsFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ProjectJSONRenderer,)
    serializer_class = ProjectSerializer

    def delete(self, request, slug=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            project = Projects.objects.get(slug=slug)
        except Projects.DoesNotExist:
            raise NotFound('Project with this slug was not found.')

        profile.unfavorite(project)

        serializer = self.serializer_class(project, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug=None):
        profile = self.request.user.profile
        serializer_context = {'request': request}

        try:
            project = Projects.objects.get(slug=slug)
        except Projects.DoesNotExist:
            raise NotFound('Project with this slug was not found.')

        profile.favorite(project)

        serializer = self.serializer_class(project, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_201_CREATED)