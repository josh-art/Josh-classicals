from django.shortcuts import render
from .models import Contacts
from .models import Post
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def index1(request):
    posts = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    user = request.user
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, 'cityblogs/home.html', context)


def contactForm(request):
    if request.method == "GET":
        return render(request, 'cityblogs/contactpage.html')
    elif request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            message = request.POST['message']
            contact = Contacts(user_name=name, email=email, mobile_number=mobile, message=message)
            contact.save()
            print("name = " + name)
            return render(request, 'cityblogs/contactpage.html', {'success': True})
        except Exception as e:
            print("error in request")
            return render(request, 'cityblogs/contactpage.html', {'success': False})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['body', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['body', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


############################
# for post update

def post_update(request):
    return render(request, 'post_update.html')

def profile_posts(request):
    posts = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'gallary.html', {'posts': posts})

def contact(request):
    return render(request, 'reach.html')

def about(request):
    return render(request, 'about.html')

def error(request):
    return render(request, 'Error.html')
# Create your views here.
