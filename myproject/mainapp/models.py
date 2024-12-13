from django.db import models

class YourModelName(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=70)
    def __str__(self):
        return self.title
# Create your models here.
