from django.shortcuts import render
from  .models import*
from django.views.generic import ListView,DetailView
from django.db.models import Q
# Create your views here.
class HomeView(ListView):
	model = Post
	template_name = 'index.html'



def index(request):
	if request.method == 'POST':
		n = request.POST['name']
		e = request.POST['email']
		m = request.POST['message']
		s = request.POST['subject']
		p = request.POST['phone']
		Index.objects.create(name=n, email=e,message=m, subject=s, phone=p)
		print('#'*50)
	else:
		print('error'*10)	
	return render(request,'index.html')




def contact(request):
	if request.method == 'POST':
		n = request.POST['name']
		e = request.POST['email']
		day = request.POST['day']
		medic = request.POST['medic']
		vaqt = request.POST['vaqt']
		m = request.POST['message']
		Contact.objects.create(name=n, email=e,vaqt=vaqt,day=day,medic=medic, message=m,)
		print('#'*50)
	else:
		print('error'*10)	
	return render(request,'index.html')	


def search (request):
	query = request.GET.get('search')


	context = {
		'index':index
	}
	return render(request, 'index.html', context)
