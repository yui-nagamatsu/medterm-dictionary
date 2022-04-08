from re import template
from django.views.generic import ListView, DetailView
from backend.models import Medterm
from django.http import HttpResponse
from django.views import generic
import string

class IndexView(ListView):
    template_name = 'backend/index.html'
    model = Medterm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_fetch = Medterm.objects.order_by('?')[:1]
        context['word_of_the_day'] = list(random_fetch)
        context['alphabet_list'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1-9']
        return context

class SearchResultView(ListView):
    template_name = 'backend/search_result.html'
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            term_list = Medterm.objects.filter(term__icontains=q_word)
        else:
            term_list = Medterm.objects.all()
        return term_list

class TermDetail(generic.DetailView):
    model = Medterm
    template_name = 'backend/detail.html'
