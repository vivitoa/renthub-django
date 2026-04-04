from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Item, Review
from .forms import ItemForm, ReviewCreateForm, ReviewUpdateForm
from common.mixins import CheckUserIsOwner, CheckUserIsItemOwner


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = (
            self.request.user.is_authenticated and
            self.request.user == self.object.owner
        )
        if self.request.user.is_authenticated:
            context['in_wishlist'] = self.object in self.request.user.wishlist.items.all()
        return context

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/item_form.html'
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, CheckUserIsItemOwner, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/item_form.html'
    success_url = reverse_lazy('catalog:list')

class ItemDeleteView(LoginRequiredMixin, CheckUserIsItemOwner, DeleteView):
    model = Item
    template_name = 'catalog/item_confirm_delete.html'
    success_url = reverse_lazy('catalog:list')

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'catalog/review_form.html'

    def form_valid(self, form):
        item = get_object_or_404(Item, pk=self.kwargs['pk'])
        form.instance.item = item
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.kwargs['pk']})

class ReviewUpdateView(LoginRequiredMixin, CheckUserIsOwner, UpdateView):
    model = Review
    form_class = ReviewUpdateForm
    template_name = 'catalog/review_form.html'

    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.object.item.pk})

class ReviewDeleteView(LoginRequiredMixin, CheckUserIsOwner, DeleteView):
    model = Review
    template_name = 'catalog/review_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('catalog:details', kwargs={'pk': self.object.item.pk})

