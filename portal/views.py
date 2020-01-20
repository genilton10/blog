from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import AreaForm, NoticiaForm
from .models import Area, Noticia

def home(request):
	return render(request, 'portal/base.html', {})
# Listar
def area_list(request):
	areas=Area.objects.all()
	return render(request, 'portal/area_list.html', {'areas':areas})

def noticia_list(request):
	noticias = Noticia.objects.filter(data_publicacao__lte=timezone.now())
	return render(request, 'portal/noticia_list.html', {'noticias':noticias})

#Detalhe
def area_detail(request, pk):
	area = get_object_or_404(Area, pk=pk)
	return render(request, 'portal/area_detail.html', {'area':area})

def noticia_detail(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	return render(request, 'portal/noticia_detail.html', {'noticia':noticia})

#Adicionar 
def area_new(request):
	if request.method == "POST":
		form = AreaForm(request.POST, request.FILES)
		if form.is_valid():
			area = form.save(commit=False)
			area.author = request.user
			area.save()
			return redirect('area_detail', pk=area.pk)

	else:
		form=AreaForm()
	return render(request, 'portal/area_edit.html', {'form':form})

def noticia_new(request):
	if request.method == "POST":
		form = NoticiaForm(request.POST, request.FILES)
		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.author = request.user
			noticia.save()
			return redirect('noticia_detail', pk=noticia.pk)

	else:
		form = NoticiaForm()
	return render(request, 'portal/noticia_edit.html', {'form':form})

# Editar 
def area_edit(request, pk):
	area = get_object_or_404(Area, pk=pk)
	if request.method == "POST":
		form = AreaForm(request.POST, request.FILES, instance=area)
		if form.is_valid():
			area = form.save(commit=False)
			area.author = request.user
			area.save()
			return redirect('area_detail', pk=area.pk)

	else:
		form=AreaForm(instance=area)
	return render(request, 'portal/area_edit.html', {'form':form})

def noticia_edit(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	if request.method == "POST":
		form = NoticiaForm(request.POST, request.FILES, instance=noticia)
		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.author = request.user
			noticia.save()
			return redirect('noticia_detail', pk=noticia.pk)

	else:
		form=NoticiaForm(instance=noticia)
	return render(request, 'portal/noticia_edit.html', {'form':form})

# Remover
def area_remove(request, pk):
	area=get_object_or_404(Area, pk=pk)
	area.delete()
	return redirect('area_list')

def noticia_remove(request, pk):
	noticia=get_object_or_404(Noticia, pk=pk)
	noticia.delete()
	return redirect('noticia_list')

# Create your views here.