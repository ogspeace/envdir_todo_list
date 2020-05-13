from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save() #insert into table where field == "";
            all_items = List.objects.all()
            context = {'all_items': all_items}
            return render(request, 'home.html', context)
    else:
        all_items = List.objects.all() # select * from List
        context = {'all_items': all_items}
        return render(request, 'home.html', context)

def about(request):
    my_name = "Adrian Ablazo"
    return render(request, 'about.html', {"myname":my_name})

def contact(request):
    return render(request, 'contact-us.html', {})

def delete(request, list_id):
    item = List.objects.get(pk=list_id) #where id = list_id
    item.delete() # delete something from your table
    return redirect('home')

def strike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True #update
    item.save()
    return redirect('home')

def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

