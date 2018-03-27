from django.shortcuts import render

# Create your views here.
from rest_framework import permissions,viewsets
from .models import Hi
from rest_framework.generics import CreateAPIView
from .serializers import HiSerializer, RegistrationSerializer
from django.contrib.auth.models import User
from .forms import HiForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages




  
class HiView(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    model = Hi
    serializer_class = HiSerializer
  
    def get_queryset(self):
        queryset = self.model.objects.all()
        # filter to tasks owned by user making request
        queryset = queryset.filter(receiver=self.request.user)
  
        return queryset
  
    def perform_create(self, serializer):
        return serializer.save(receiver=self.request.user)


class RegistrationView(CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)


def index(request):
	if request.method == 'POST':
		item = Hi(sender=request.user)

		title = 'Send Hi!'

		form = HiForm(request.POST ,instance=item)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			messages.success(request, "Hi sent!")
			return HttpResponseRedirect(request.path)

	else:
		form = HiForm()


	return render(request, "index.html", {'form': form, 'his':Hi.objects.filter(receiver=request.user)})



