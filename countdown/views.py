from django.shortcuts import render
from .models import Email

# Create your views here.
def countdown(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        new = Email(
            email = email
        )
        new.save()

        return render(request, 'countdown/count.html', {'on_list':True})
    else:
        return render(request, 'countdown/count.html')