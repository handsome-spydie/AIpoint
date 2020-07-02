from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_id = models.AutoField
	blog_name = models.CharField(max_length=50,default='')
	desc =	models.CharField (max_length=300,default='')
	category = models.CharField(max_length=50,default='')
	subcategory = models.CharField(max_length=50,default='')
	author = models.CharField(max_length=50)
	pub_date = models.DateField()


	def __str__(self):
		return self.blog_name