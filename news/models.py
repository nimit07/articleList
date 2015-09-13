from django.db import models

class Articles(models.Model):
    email=models.EmailField()
    article=models.TextField()
    author=models.CharField(max_length=70)
    heading=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def as_article(self):
        return dict(email=self.email,article=self.article,author=self.author,heading=self.heading,timestamp=self.timestamp.isoformat(),updated=self.updated.isoformat())


# Create your models here.
