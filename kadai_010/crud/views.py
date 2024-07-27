from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"
    
    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
    #     context['name'] ="侍太郎"
    #     context['age'] = 36
        
    #     return context
        
        

class ProductListView(ListView):
    model = Product
    # template_name = 'product_list.html'
    paginate_by = 3
    
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    
class ProductUpadateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
    
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')
    
class ProductDetailView(DetailView):
    model = Product
    