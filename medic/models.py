from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='poster/')


	class Meta:
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'
		ordering = ['-id']

	def __str__(self):
		return self.title	


# Create your models here.

class Index(models.Model):
	name = models.CharField('Ismi',max_length=150)
	email = models.EmailField('Emaili',max_length=100)
	phone = models.CharField('Telefon raqami',max_length=50)
	subject = models.CharField('Kasalligi',max_length=80)
	message = models.CharField('Xabari',max_length=200)

	def __str__(self):
		return f"{self.name}"	
 
	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contactlar'





class Contact(models.Model):	
	name = models.CharField('Ismi', max_length=50)
	email = models.EmailField('Emaili', max_length=200)
	medic = models.CharField('Doktor',max_length=50)
	vaqt = models.TimeField('Time', max_length=70)
	message = models.CharField('Xabari',max_length=200)
	day = models.DateField('Day', max_length=80)
	Choice= (
		('Mr.Javlonbek'),
		('Mr.Michael'),

		('Yakshanba'),
		('Dushanba'),
		('Seshanba'),
		('Chorshanba'),
		('Payshanba'),
		('Juma'),
		('shanba'),
		('8:00'),
		('9:00'),
		('10:00'),
		('11:00'),
		('14:00'),
		('15:00'),
		('16:00'),
		('17:00'),
		('18:00'),
),

	def __str__(self):
		return f"{self.name}"	
 
	class Meta:
		verbose_name = 'buyurtma'
		verbose_name_plural = 'buyurtmalar'
