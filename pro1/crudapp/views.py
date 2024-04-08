from django.shortcuts import render, redirect
from django.views import View
from .forms import BookForm
from .models import Book


class Create_view(View):

    def get(self, request):
        form = BookForm()
        template_name = 'crudapp/create.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request):
        form = BookForm()
        if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('show_url')


class Show(View):
    def get(self, request):
        template_name = 'crudapp/show.html'
        orders = Book.objects.all()
        context = {'orders': orders}
        return render(request, template_name, context)


class Update(View):
    def get(self, request, pk):
        obj = Book.objects.get(id=pk)
        form = BookForm(instance=obj)
        context = {'form': form}
        return render(request, 'crudapp/create.html', context)

    def post(self, request, pk):
        obj = Book.objects.get(id=pk)
        form = BookForm(instance=obj)
        if request.method == "POST":
            form = BookForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect("show_url")
        context = {'form': form}
        return render(request, 'crudapp/create.html', context)


class Cancel_order(View):
    def get(self, request, pk):
        obj = Book.objects.get(id=pk)
        return render(request, 'crudapp/confirmation.html')

    def post(self, request, pk):
        obj = Book.objects.get(id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('show_url')
        return render(request, 'crudapp/confirmation.html')


