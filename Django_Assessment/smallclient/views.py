from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from smallclient.form import ClientForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from smallclient.models import SmallClient

# Create your views here.
class CreateClient(CreateView):
    form_class = ClientForm
    template_name = 'smallclient/client.html'
    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        files = request.FILES.getlist('profile_pic')

        if form.is_valid():
            if len(files) ==0:
                message ="Profile picture can not be empty"
                return render(request, self.template_name, {'form': form,'message':message})
            client = form.save()
            client.save()
            return HttpResponseRedirect(reverse_lazy('view_client', kwargs={'pk': client.id}))
        return render(request, self.template_name, {'form': form})

class ViewClient(DetailView):
    model = SmallClient
    template_name = 'smallclient/viewclient.html'
    context_object_name = 'data'

class ListClient(ListView):
    model = SmallClient
    paginate_by = 4
    page_kwarg = 'page'
    template_name = 'smallclient/clientlist.html'

def View(request):
    return render(request, 'smallclient/clientlist.html', {})