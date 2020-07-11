from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def format_pub_date(self):
        return self.pub_date.__format__("%Y. %m. %d.")

    def summary(self):
        return self.body[:100]
