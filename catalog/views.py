from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Item, Review
from .forms import ItemForm, ReviewCreateForm


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

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'catalog/review_form.html'

    def form_valid(self, form):
        item = get_object_or_404(Item, pk=self.kwargs['pk'])
        form.instance.item = item

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.kwargs['pk']})