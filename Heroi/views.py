from django.shortcuts import render, HttpResponse
from .models import Heroi
from .forms import HeroiForm
import redis

# Create your views here.

def home(request):
    conexão = redis.Redis()
    form = HeroiForm(request.POST or None)
    lista = Heroi.objects.all()
    if form.is_valid():
        form.save()
        dic = {'nome':form.cleaned_data['nome'], 'universo':form.cleaned_data['universo'],
               'habilidade':form.cleaned_data['habilidade']}
        conexão.hmset(str(form.cleaned_data['nome']), dic)
        redis_lista = conexão.hgetall(str(form.cleaned_data['nome'])).items()
        form = HeroiForm()
        return render(request, 'index.html', {'form':form, 'lista':lista, 'redis':redis_lista})
    else:
        form = HeroiForm()
        redis_lista = conexão.keys()
        return render(request, 'index.html', {'form':form, 'lista':lista, 'redis':redis_lista})