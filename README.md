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

Of course, if we want to use that admin panel (and why would we not?) we'll have to create a Super User first

``


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

        
Now, lets create a review serializer. We are using a different type of serializer, working with the individual Models for this        
        
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
    
    
    
 Next will be our Books serializer. Books have reviews attached, so we'll need to include that serializer in to show off their data. By using the Review Serializer as our View Engine, we are able to see all of its associated data, not just the hyperlink!
 
 
```    
class BookSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many = True,
        read_only = True
    )
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'summary', 'price', 'reviews', 'photo_url')
```


Now when we go to our /Books url, we will be able to see our Review information not as hyperlinks, but as the actual data. Which means if we make an axios call to /books/1, we'll be able to pull all of the attached reviews and render them on our screen!

Make sure to set up and install CORS and all respective Middleware, you should now have a fully functioning Django back end with related data models!
