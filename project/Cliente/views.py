from django.shortcuts import render, redirect

from . import models, forms

def home(request):
    query = models.Cliente.objects.all()
    context = {"clientes": query}
    return render(request, "Cliente/index.html", context)

def crearclientes(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cliente:home")
    else:
        form = forms.ClienteForm()
    return render(request, "Cliente/crearcliente.html", context={"form": form})