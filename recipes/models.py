from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=65)

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length= 65)
    preparation_steps = models.TextField() #Para campos grandes, onde temos que deixar o tamanho livre
    preparation_steps_is_html = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True) #Gera uma data no momento da ciração
    updated_at = models.DateField(auto_now = True) #sem o add, só na data de alteração
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to = 'recipes/covers/%Y/%m/%d/')

    #Relações
    category = models.ForeignKey(
        Category, on_delete = models.RESTRICT , null = True
        
    )

    autor = models.ForeignKey(
        User, on_delete = models.SET_NULL, null = True
    )

