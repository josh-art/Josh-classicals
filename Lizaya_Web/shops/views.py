from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import Contacts


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)



def contact(request):
    if request.method == "GET":
        return render(request, 'electrical.html')
    elif request.method== "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            message = request.POST['message']
            contact = Contacts(user_name=name, email=email, mobile_number=mobile, message=message)
            contact.save()
            print("name = " + name)
            return render(request, 'electrical.html', {'success' : True})
        except Exception as e:
            print("error in request")
            return  render(request, 'electrical.html', {'success': False})

def feedback(request):
    return render(request, 'contact.html')

def folio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')


@login_required(login_url='../../login/')
def AddFeatured(request):
    name = 'Add Featured Product '
    form = ProductFeaturedForm(request.POST or None)
    context = {
        'name': name,
        'form': form
    }
    if request.method == 'POST':
        form = ProductFeaturedForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Featured Product Saved')
            return redirect('AddFeatured')
        else:
            messages.error(request, " Unsuccessfuly Adding Featured Product")
    else:
        return render(request, 'baseform.html', context)
# Create your views here.

# Create your views here.




# Create your views here.
