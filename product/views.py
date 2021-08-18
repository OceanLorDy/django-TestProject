from django.shortcuts import render, redirect
from .models import FastFood
from .forms import FastFoodForm


def ffList(request):
    ff = FastFood.objects.all()
    return render(request, "products/fast-food-list.html", {'ff': ff})


def ffCreate(request):
    if request.method == "POST":
        form = FastFoodForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('fast-food-list')
            except:
                pass
    else:
        form = FastFoodForm()
    return render(request, 'products/fast-food-create.html', {'form': form})


def ffUpdate(request, id):
    ff = FastFood.objects.get(id=id)
    form = FastFoodForm(initial={'name': ff.title, 'price': ff.price})
    if request.method == "POST":
        form = FastFoodForm(request.POST, instance=ff)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('fast-food-list')
            except Exception as e:
                pass
    return render(request, 'products/fast-food-update.html', {'form': form})


def ffDelete(request, id):
    ff = FastFood.objects.get(id=id)
    try:
        ff.delete()
    except:
        pass
    return redirect('fast-food-list')
