from django.db import models

class Password(models.Model):
    class Meta:
        app_label = 'home'
    id = models.IntegerField(primary_key=True)
    site = models.URLField(max_length=256)
    name_site = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.site