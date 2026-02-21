from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def custom_404(request, exception):
    return render(request, "common/errors/404.html", status=404)


class AboutView(TemplateView):
    template_name = "common/about.html"
