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


