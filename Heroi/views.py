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
        lista = Heroi.objects.all()
        conexão.hset(str(form.cleaned_data['nome']), 'nome', form.cleaned_data['nome'])
        conexão.hset(str(form.cleaned_data['nome']), 'universo', form.cleaned_data['universo'])
        conexão.hset(str(form.cleaned_data['nome']), 'habilidade', form.cleaned_data['habilidade'])
        match_redis = conexão.keys()
        lista_redis = []
        for i in match_redis:
            lista_redis.append(i)
        print(lista_redis)
        form = HeroiForm()
        return render(request, 'cadastro.html', {'form': form, 'lista':lista, 'redis':lista_redis})
    else:
        form = HeroiForm()
        return render(request, 'cadastro.html', {'form':form})