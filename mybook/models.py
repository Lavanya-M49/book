from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    rating=models.IntegerField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField()
    genre=models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.CASCADE)

    def __str__(self):
        return self.title