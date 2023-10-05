from django.db import models

# Create your models here.
class place(models.Model):
    name= models.CharField(max_length=255)
    img= models.ImageField(upload_to='pics')
    desc=models.TextField()
    image=models.FileField(upload_to='gal',null=True,blank=True,default=None)

    def __str__(self):
        return self.name