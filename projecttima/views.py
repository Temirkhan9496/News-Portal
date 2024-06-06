from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Post
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def request_to_be_author(request):
    if request.method == 'POST':
        authors_group = Group.objects.get(name='authors')
        request.user.groups.add(authors_group)
        return redirect('profile')
    return render(request, 'news/request_to_be_author.html')


class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    permission_required = 'news.add_post'

class PostEditView(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    permission_required = 'news.change_post'

@login_required
def profile_view(request):
    return render(request, 'news/profile.html')
from django.shortcuts import render

@login_required
def restricted_page(request):
    return HttpResponse("только для зарегистрированных пользователей")