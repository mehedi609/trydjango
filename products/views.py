from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

from .forms import ProductForm, ProductRawForm
# Create your views here.


def product_create_raw_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        print(title)

    context = {}
    return render(request, 'products/product_create_raw.html', context)


def product_create_django_form_view(request):
    my_form = ProductRawForm(request.POST or None)
    if my_form.is_valid():
        print(my_form.cleaned_data)
        Product.objects.create(**my_form.cleaned_data)
        my_form = ProductRawForm()
    else:
        print(my_form.errors)

    context = {'form': my_form}
    return render(request, 'products/product_create_django_raw.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = Product.objects.all()

    context = {
        'object': obj
    }

    return render(request, 'products/product_detail.html', context)


def render_initial_data(request):
    initial_data = {
        'title': 'This is initial Title'
    }
    # form = ProductForm(request.POST or None, initial=initial_data)
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'object': obj
    }
    return render(request, 'products/dynamic_product_detail.html', context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('pages:home')
    context = {}
    return render(request, 'products/product_delete.html', context)




