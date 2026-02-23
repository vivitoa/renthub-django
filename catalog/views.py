from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Item
from .forms import ItemForm
# Create your views here.


class ItemListView(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        return queryset

class ItemDetailView(DetailView):
    model = Item
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/item_form.html'
    success_url = reverse_lazy('catalog:list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/item_form.html'
    success_url = reverse_lazy('catalog:list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'catalog/item_confirm_delete.html'
    success_url = reverse_lazy('catalog:list')

