from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class HomeView(ListView):
    model = Post

    # The name of the template to use for the list view
    template_name = "blog/index.html"

    # Name the data that has been queried
    context_object_name = "posts"
