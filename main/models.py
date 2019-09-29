from django.db import models

# Create your models here.

class Data_database(models.Model):
	title = models.CharField("isim",max_length=120) # admin sayfasındaki baslik isimlerini 
	system_name = models.TextField("System name")
	publishing_date = models.DateTimeField("yayin tarihi",auto_now_add=True)
	data1 = models.IntegerField()
	data2 = models.IntegerField()
	data3 = models.IntegerField()
	
	def __str__(self):
		return self.system_name