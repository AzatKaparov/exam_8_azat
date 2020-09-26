from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from django.urls import reverse_lazy
from webapp.forms import SimpleSearchForm, ProductForm, ReviewForm
from webapp.models import Product, Review
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/create_review.html'
    form_class = ReviewForm

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


class UpdateReviewView(UpdateView):
    model = Review
    template_name = 'review/update_review.html'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.pk})




