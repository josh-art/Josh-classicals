from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.models import User
from cart.views import Cart
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


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shops/product/detail.html', context)

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

@login_required(login_url='../../login/')
def addUser(request):
    name = 'Login and Register '
    cart_id = request.session.get('cart_id')
    context = {
        'name': name
    }

    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:

            user = User.objects.create(
                username=uname,
                email=email,
                password=pass1
            )
            if cart_id == None:
                cart = Cart()
                cart.user = user
                cart.save()
                cart_id = cart.id
                request.session['cart_id'] = cart_id
            cart = Cart.objects.get(pk=cart_id)
            cart.user = user
            cart.save()

            messages.success(request, 'Featured Product Saved')
            return redirect('Home')
    else:
        return render(request, 'adduser.html', context)


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
