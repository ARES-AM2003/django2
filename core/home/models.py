from django.db import models

# Create your models here.
class Menue(models.Model):
    name = models.CharField(max_length=200)
    slug=models.SlugField()
    def __str__ (self):
        return self.name
    


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug=models.SlugField()
    def __str__ (self):
        return self.name
    
    category = models.ForeignKey(Menue,related_name="product", on_delete=models.CASCADE)

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__ (self):
        return self.name 