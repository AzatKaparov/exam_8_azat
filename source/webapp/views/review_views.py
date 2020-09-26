from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.urls import reverse_lazy
from webapp.forms import SimpleSearchForm, ProductForm, ReviewForm
from webapp.models import Product, Review
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class ReviewCreateView(PermissionRequiredMixin, CreateView):
    model = Review
    template_name = 'review/create_review.html'
    form_class = ReviewForm
    permission_required = 'webapp.add_review'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        form.save_m2m()
        return redirect('webapp:product_view', pk=product.pk)

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs.get('pk'))
        return context


class UpdateReviewView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'review/update_review.html'
    form_class = ReviewForm
    permission_required = 'webapp.change_review'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user


class DeleteReviewView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/delete_review.html'
    permission_required = 'webapp.delete_review'

    def get_success_url(self):
        return reverse_lazy('webapp:index')

    def has_permission(self):
        return super().has_permission() and self.get_object().author == self.request.user
