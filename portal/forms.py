
from django import forms
from .models import Area, Noticia

class AreaForm(forms.ModelForm):

	class Meta:
		model = Area
		fields = ('descricao', 'cor','status')

class NoticiaForm(forms.ModelForm):

	class Meta:
		model = Noticia
		fields = ('author','area','photo', 'title','text', 'data_publicacao')