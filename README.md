## SEIR 1003

# Django Serializers II - Model Related Fields

In our previous lesson, we began working with Serializers in Django. But we have seen a small problem - our models are related by Hyperlinks, not by their actual data. We don't want to see something like "localhost:8000/songs/5" when we load up a page, we want to see the actual data.

Lets work with a Book Review Site, attaching our Reviews to our Book Models.

Fork and Clone this repo down, then lets load up our basic installation and set up

First, lets get our Shell created

```
pipenv shell
```

Then, we can run and install Django and Psycopg2

```
pipenv install django
```


```
pipenv install psycopg2-binary
```

```
pipenv instal djangorestframework
```


Now we can load up our SQL file to create our DB. Remember, you only need the "-U Postgres" if you've had to use it before, if you haven't, don't put it in!


```
psql -U postgres -f settings.sql
```


Our migrations should be created with the project, so lets just run a migration to get our tables created

```
python3 manage.py migrate
```

Now we can see our tables in our PSQL shell, and can populate our database with the Django Admin screen, PSQL, or Postico, your pick! 
I'll be using Postico as it is the quickest way to put some data in.


If you try loading up localhost:8000 you'll get some errors, this is because we have not gotten our Serializer View Engine set up yet.


When you load up serializers.py you should see your User model already created. Lets work on the Review and Book Serializers to add full relations to our data

```
from rest_framework import serializers
from .models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name = 'review_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'reviews')
```

We can see that Reviews will be attached to Users in a One-> Many relation, and that we can see url's for our reviews attached when they are created.


Lets get our Book and Review Serializers created next.

If we want to use these models, what do we need to do first?

``
from .models import User, Book, Review
``

        
Now, lets create a review serializer        
        
```        
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
```


Reviews are owned by both Users and Books, so lets attach them in. Then lets add a Meta class so that when we see the models we see what data is attached

```
    users = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only = True
    )
    books = serializers.HyperlinkedRelatedField(
        view_name = 'book_detail',
        read_only = True
    )
    class Meta:
        model = Review
        fields = ('id', 'name', 'title', 'body', 'books', 'users')    
 ```   
    
    
 It should look like this at the end   
    
```
class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only = True
    )
    books = serializers.HyperlinkedRelatedField(
        view_name = 'book_detail',
        read_only = True
    )
    class Meta:
        model = Review
        fields = ('id', 'name', 'title', 'body', 'books', 'users')
```        
    
    
    
class BookSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many = True,
        read_only = True
    )
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'summary', 'price', 'reviews', 'photo_url')
