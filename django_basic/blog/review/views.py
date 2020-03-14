from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm()

    return render(request, 'new.html', {'form': form})
