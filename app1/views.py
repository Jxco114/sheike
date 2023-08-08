from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import Clientmsg




# Create your views here.
def index(request):
    form = Clientmsg
    if request.method == 'POST':
        form = Clientmsg(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('Invalid Form')
    return render(request, 'cvit/index.html', {'form': form})