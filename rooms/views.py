from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import ArticleForm


# Create your views here.


def rooms_home(request):
    rooms = Articles.objects.order_by('num')
    return render(request, 'rooms/rooms_home.html', {'rooms': rooms})


class RoomsDetailView(DetailView):
    model = Articles
    template_name = 'rooms/details_view.html'
    context_object_name = 'article'


class RoomsDeleteView(DeleteView):
    model = Articles
    success_url = '/hospital'
    template_name = 'rooms/rooms-delete.html'


class RoomsUpdateView(UpdateView):
    model = Articles
    template_name = 'rooms/update.html'

    fields = ['num', 'name1', 'about1', 'temp1', 'date1', 'name2', 'about2', 'temp2', 'date2', 'name3', 'about3',
                  'temp3', 'date3', 'name4', 'about4', 'temp4', 'date4']


def add(request):
    error = ''
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms_home')
        else:
            error = 'Форма заполнена неверно'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'rooms/create.html', data)
