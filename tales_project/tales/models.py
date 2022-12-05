from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Book(models.Model):
    title = models.CharField(max_length=50, default='no title')
    author = models.CharField(max_length=50, default='no author')
    genre = models.CharField(max_length=50, default='no genre')
    summary = models.CharField(max_length=250, default='no summary')
    price = models.CharField(max_length=50, default='no price')
    photo_url = models.CharField(max_length=250, default='no summary')

    def __str__(self):
        return self.title 

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    rating = models.CharField(max_length=50)

    def __str__(self):
        return self.name 