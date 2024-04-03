from django.shortcuts import render, get_object_or_404
from .models import Category
from .models import Contacts


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    context = {
        'category': category,
        'categories': categories,

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




# Create your views here.




# Create your views here.
