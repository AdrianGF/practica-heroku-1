from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    favorited = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = ['slug', 'favorited', 'title', 'description', 'img', 'financed', 'pub_date']
    
    def get_favorited(self, instance):
        request = self.context.get('request', None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return False

        return request.user.profile.has_favorited(instance)
