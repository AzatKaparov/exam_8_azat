from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q
from django.urls import reverse_lazy
from webapp.forms import SimpleSearchForm, ProductForm
from webapp.models import Product, Review
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class ProductIndexView(ListView):
    template_name = 'product/product_index.html'
    context_object_name = 'products'
    model = Product
    ordering = ['name']
    paginate_by = 6
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['reviews'] = Review.objects.filter(product=self.object)
        all = Review.objects.filter(product=self.object)
        if all:
            sum = 0
            for i in Review.objects.filter(product=self.object):
                sum += i.mark
            avg = sum / len(Review.objects.filter(product=self.object))
            context['avg'] = f'{avg:.2}'
        else:
            context['avg'] = 0
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.form_valid(form)

        else:
            return self.form_valid(form)


class ProductUpdateView(PermissionRequiredMixin ,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    context_object_name = 'product'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    permission_required = 'webapp.delete_product'

    def get_success_url(self):
        return reverse('webapp:index')



