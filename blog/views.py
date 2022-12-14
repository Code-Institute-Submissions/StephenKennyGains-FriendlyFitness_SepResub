""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to enter into a full view
of listed posts and comment on them and like them if registered
and logged in"""

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class AllPosts(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Posts limited to 3 most recent for each category """

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"


class PostDetail(View):

    """ Sets the view for the full post detail """

    def get(self, request, slug, *args, **kwargs):
        """ Defines parameters for full post view """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_full.html",
            {
                "post": post,
            },
        )
