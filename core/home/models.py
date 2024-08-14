from django.db import models

# Create your models here.
class Menue(models.Model):
    cname = models.CharField(max_length=200)
    slug=models.SlugField()
    def __str__ (self):
        return self.cname
    def __eq__(self, other) :
        return self.cname == other.cname
    


class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug=models.SlugField()
    def __str__ (self):
        return self.name
    cname = models.ForeignKey(Menue,related_name="product", on_delete=models.CASCADE)
    def __eq__(self, other) :
        return self.cname == other.cname
    
    

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__ (self):
        return self.name 