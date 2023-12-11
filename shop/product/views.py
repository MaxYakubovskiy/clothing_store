from django.shortcuts import render
from django.views import View


# Create your views here.
class MainShop(View):
    template_name = 'product/main.html'

    def get(self, request):
        return render(request, self.template_name)