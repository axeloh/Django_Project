from django.db import models

# This contains database information and metadata

# Creating a table in the database
class Post(models.Model):
    # Defining the columns in the table
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

