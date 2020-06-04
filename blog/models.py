from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title