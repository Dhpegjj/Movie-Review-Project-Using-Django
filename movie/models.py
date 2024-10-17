from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='movie/images/')
    url=models.URLField(blank=True)
    def __str__(self):
        return self.title
class Email(models.Model):
    emailid=models.EmailField(max_length=50)

    def __str__(self):
       return self.emailid