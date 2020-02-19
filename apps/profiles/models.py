from django.db import models

from apps.core.models import TimestampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)

    favorites = models.ManyToManyField(
        'projects.Projects',
        related_name='favorited_by'
    )

    def __str__(self):
        return self.user.username

    def favorite(self, project):
        self.favorites.add(project)

    def unfavorite(self, project):
        self.favorites.remove(project)

    def has_favorited(self, project):
        return self.favorites.filter(pk=project.pk).exists()