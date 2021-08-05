from django.db import models

# Create your models here.

class Movies(models.Model):
	title = models.CharField(unique=True, max_length=64, null=False)
	episode_nb = models.IntegerField(primary_key=True)
	opening_crawl = models.TextField(null=True)
	director = models.CharField(null=False, max_length=32)
	producer = models.CharField(null=False, max_length=128)
	release_date = models.DateField(null=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
