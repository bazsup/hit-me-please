from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Hitter

class LandingPageView(View):
    def get(self, request):
        return render(
            request,
            'index.html'
        )

    def post(self, reuqest):
        email = reuqest.POST.get('email')

        Hitter.objects.create(email=email)

        return HttpResponse()
