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
