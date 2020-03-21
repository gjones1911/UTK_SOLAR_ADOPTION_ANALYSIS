from django.db import models

# Create your models here.
class Tutorial(models.Model):                                   # this creates a table called a model in django
        tutorial_title = models.CharField(max_length=200)        # creates a character field of 200 chars
        tutorial_content = models.TextField()                   # creates a field for text of undetermined size
        tutorial_published = models.DateTimeField("data published")

        def __str__(self):
                return self.tutorial_title                     # will return the title string if cast to a string
