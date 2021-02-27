from django.shortcuts import render,redirect
from .models import Product
from .forms import ListForm
# Create your views here.
def index(request):
    tasks = Product.objects.all()
    if (request.GET.get('DeleteButton')):
        Product.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('/')

    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')

        else:
            form = ListForm()    
    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request, 'index.html',context)