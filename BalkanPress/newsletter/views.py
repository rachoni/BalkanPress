from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from BalkanPress.common.helpers import get_next_url

from .forms import NewsletterSubscribeForm


# Create your views here.
class NewsletterSubscribeView(View):
    def post(self, request, *args, **kwargs):
        form = NewsletterSubscribeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You havesubscribed successfully.")
        else:
            email_errors = form.errors.get("email")
            if email_errors:
                messages.error(request, email_errors[0])
            else:
                messages.error(request, "Subscription failed. Please try again.")

        return redirect(get_next_url(request))
