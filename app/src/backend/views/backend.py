from django.views.generic import ListView
from backend.models import Medterm

class IndexView(ListView):
    template_name = 'backend/index.html'
    model = Medterm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_fetch = Medterm.objects.order_by('?')[:1]
        context['word_of_the_day'] = list(random_fetch)
        # context['alphabet_list'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1-9']
        return context

