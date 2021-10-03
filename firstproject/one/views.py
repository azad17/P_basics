from rest_framework.response import Response
from django.shortcuts import redirect, render
from .forms import BooksForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Books
from rest_framework.views import APIView
from .serializers import BookSerializer

def home(request):
    
    return render(request,'one/home.html',)
def add(request):
    form = BooksForm()
    if request.method=='POST':
        form=BooksForm(request.POST)
        if form.is_valid:
            form.save();
            return redirect('/')
    return render (request,'one/add_book.html',{'form':form})    

class BooksView(ListView):
    model = Books
    template_name = 'one/list.html'
    context_object_name = 'book'
        
class BookDetails(DetailView):
    model = Books
    template_name = 'one/details.html'   
    context_object_name = 'book'   
class  BookUpdate(UpdateView):
    model = Books
    template_name ='one/update.html'
    context_object_name = 'book'   
    fields ='__all__'
    #success_url = reverse_lazy("one:home")
    def get_success_url(self):
        return reverse_lazy('one:details',kwargs={'pk':self.object.id})
class BookData(APIView):
    def get(self,request):
        book1 = Books.objects.all()
        serializer = BookSerializer(book1,many=True)
        return Response(serializer.data)
    
