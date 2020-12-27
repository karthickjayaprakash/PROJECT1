from django.db import models

# Create your models here.
class Food(models.Model):#anything is Food
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images', default='static/images/DIET3.jpg')

class Paleo(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images',default='static/images/DIET3.jpg')

class Vegetarian(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images' ,default='images/DIET3.jpg')

class Vegan(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images' ,default='static/images/DIET3.jpg')

class Ketogenic(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images', default='static/images/DIET3.jpg')

class Mediterranean(models.Model):
	name=models.CharField(max_length=150)
	calories=models.FloatField()
	carbohydrates=models.FloatField()
	protiens=models.FloatField()
	fat=models.FloatField()
	img=models.ImageField(upload_to='images', default='static/images/DIET3.jpg')


class review(models.Model):
	name=models.CharField(max_length=10)
	comment=models.CharField(max_length=50)

class drop(models.Model):
	mealchoice =(
		('light meal','light meal'),
		('medium meal','medium meal'),
		('heavy meal','heavy meal')
		)
	choicename= models.CharField(max_length=120,choices= mealchoice)