from django.shortcuts import render, HttpResponse
from .models import Heroi
from .forms import HeroiForm
import redis

# Create your views here.

def home(request):
    conexão = redis.Redis()
    form = HeroiForm(request.POST)
    if form.is_valid():
        form.save()
        conexão.set('nome:' + str(form.cleaned_data['nome']), form.cleaned_data['nome'])
        conexão.set('universo:' + str(form.cleaned_data['nome']), form.cleaned_data['universo'])
        conexão.set('habilidade:' + str(form.cleaned_data['nome']), form.cleaned_data['habilidade'])
        #conexão.rpush(str(form.cleaned_data['nome']), form.cleaned_data['nome'], form.cleaned_data['universo'], form.cleaned_data['habilidade']))
        lista = Heroi.objects.all()
        #lista_redis = conexão.lrange(str(form.cleaned_data['nome']), 0, -1)
        lista_redis = conexão.keys()
        form = HeroiForm()
        return render(request, 'cadastro.html', {'form': form, 'lista':lista, 'lista_redis':lista_redis})
    else:
        form = HeroiForm()
        return render(request, 'cadastro.html', {'form':form})