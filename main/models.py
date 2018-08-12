from django.db import models

class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
    text = models.TextField()
    author = models.CharField(max_length=512)
