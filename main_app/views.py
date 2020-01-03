from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Wish

def home(request):
    wishes = Wish.objects.all()
    print (wishes)
    return render(request, 'home.html', {'wishes': wishes})

def wish_delete(request, wish_id):
    Wish.objects.filter(id = wish_id).delete()
    return redirect('/')


class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'