from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Count
from .models import Post
from .forms import PostForm  # forms.py එකෙන් PostForm එක Import කරගැනීම


# 1. Post List View (Home Page with Search and Pagination)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(status="published").order_by("-created_at")
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = (
            Post.objects.filter(status="published")
            .values("category")
            .annotate(count=Count("category"))
        )
        return context


# 2. Post Detail View
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# 3. Post Create View (Using PostForm)
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm  # fields වෙනුවට PostForm එක භාවිත වේ
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})


# 4. Post Update View (Using PostForm)
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm  # fields වෙනුවට PostForm එක භාවිත වේ
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})


# 5. Post Delete View
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("home")


# About & Contact Views
def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/contact.html")