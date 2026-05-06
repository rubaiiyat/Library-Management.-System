from django.db import models
from category.models import CategoryModel
from django.utils.text import slugify

# Create your models here.
class AddBooksModel(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(unique=True,blank=True)
    image=models.ImageField(upload_to='books/')
    author=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    category=models.ManyToManyField(CategoryModel)
    available_copies=models.IntegerField(default=1)


    def __str__(self):
        return f'{self.name} - {self.author}'
    
    def save(self,*args, **kwargs):

        if not self.slug:
            self.slug=slugify(self.name)

        super().save(*args, **kwargs)