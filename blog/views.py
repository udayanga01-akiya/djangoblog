from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# 1. Post List View (Class Based View)
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "page_obj"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status="published").order_by("-created_at")

# 2. Post Detail View (Class Based View)
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# 3. Post Create View (අද පාඩම - Part A)
class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "category", "tags", "status"]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})

# 4. Post Update View (අද පාඩම - Part B)
class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "category", "tags", "status"]
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})

# 5. Post Delete View (අද පාඩම - Part B)
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("home")

# 6. About & Contact Views
def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/contact.html")