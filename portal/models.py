
from django.db import models
from django.utils import timezone

class Area(models.Model):
	descricao = models.CharField(max_length=200)
	cor = models.CharField(max_length=50)
	status = models.BooleanField(default=False)
	
	def ativar(self):
		self.status=True
		self.save()

	def dasativar(self):
		self.status=False
		self.save()

	def __str__(self):
		return self.descricao

	
class Noticia(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
	photo = models.ImageField(upload_to='imagens/', null=True, blank=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
	data_publicacao = models.DateTimeField(default=timezone.now)
	
	def publicar(self):
		self.data_publicacao = timezone.now()
		self.save()

	def __str__(self):
		return self.title


# Create your models here.

			


# Create your models here.
