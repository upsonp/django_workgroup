from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "wg_examples/index.html"
