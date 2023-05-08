from django.db import models


class Url(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=50)

    def __str__(self):
        return self.url
