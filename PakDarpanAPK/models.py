from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.html import mark_safe

# Create your models here.
class UserDetail(models.Model):
	SEX_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
	STATE_CHOICES = (
		("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
		("Andhra Pradesh",'Andhra Pradesh'),
		("Arunachal Pradesh",'Arunachal Pradesh'),
		("Assam",'Assam'),
		("Bihar",'Bihar'),
		("Chandigarh",'Chandigarh'),
		("Chhattisgarh",'Chhattisgarh'),
		("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
		("Daman and Diu",'Daman and Diu'),
		("Delhi",'Delhi'),
		("Goa",'Goa'),
		("Gujarat",'Gujarat'),
		("Haryana",'Haryana'),
		("Himachal Pradesh",'Himachal Pradesh'),
		("Jammu & Kashmir",'Jammu & Kashmir'),
		("Jharkhand",'Jharkhand'),
		("Karnataka",'Karnataka'),
		("Kerala",'Kerala'),
		("Lakshadweep",'Lakshadweep'),
		("Madhya Pradesh",'Madhya Pradesh'),
		("Maharashtra",'Maharashtra'),
		("Manipur",'Manipur'),
		("Meghalaya",'Meghalaya'),
		("Mizoram",'Mizoram'),
		("Nagaland",'Nagaland'),
		("Odisha",'Odisha'),
		("Puducherry",'Puducherry'),
		("Punjab",'Punjab'),
		("Rajasthan",'Rajasthan'),
		("Sikkim",'Sikkim'),
		("Tamil Nadu",'Tamil Nadu'),
		("Telangana",'Telangana'),
		("Tripura",'Tripura'),
		("Uttarakhand",'Uttarakhand'),
		("Uttar Pradesh",'Uttar Pradesh'),
		("West Bengal",'West Bengal'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	dob = models.DateField(null = True)
	photo = models.ImageField(default='default.png',upload_to='user_photos')
	mobile = models.CharField(max_length=10,null=True)
	alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
	address = models.TextField()
	pincode = models.CharField(max_length=6, null=True)
	landmark = models.CharField(max_length=500, null=True, blank=True)
	locality = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	sex = models.CharField(max_length=6,choices=SEX_CHOICES, null=True)

	def __str__(self):
		return self.user.username

	def image_tag(self):
		return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.photo))

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.photo.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.photo.path)