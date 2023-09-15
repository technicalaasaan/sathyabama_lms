from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import BookForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Books

data = [
     {'name': 'suresh', 'loc': 'chennai', 'val': 600091},
     {'name': 'sugumar', 'loc': 'bangalore', 'val': 560017},
]
# Create your views here.
def contact(request):
    return render(request, 'contact.html', {'out': data})
def home(request):
    return render(request, 'home.html', {'out': data})
    # return render(request, 'home.html', {'out': data})
    # return JsonResponse({ 'name':'Thank you!'})
# def home(request):
#     return render(request, 'home.html')
#     # return HttpResponse('Test')

def create_view(request):
    # data = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    # data['form'] = form
    return render(request, 'books.html', {'name': form})
        
def get_books(request):
    data = {}
    data['books'] = Books.objects.all()
    return render(request, 'get_books.html', data)

def update_books(request):
    res = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
         form.save()
         return HttpResponse('Saved!')
    res['data'] = Books.objects.get(book_id=request.GET.get('book_id'))
    return render(request, 'book_update.html', res)

class CreateBook(CreateView):
     model = Books
     fields = '__all__'
     template_name = 'books.html'

class GetBook(ListView): # DetailView
     model = Books
     template_name = 'get_books.html'


class UpdateBook(UpdateView):
    model = Books
    fields = ['author', 'qty']
    template_name = 'book_update.html'
    success_url = '/'