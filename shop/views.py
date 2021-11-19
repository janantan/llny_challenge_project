from django.shortcuts import render
from .models import Customer
from users.models import NetflixUser

def shop(request, data=None):
	context = {'data': data}
	resp = render(request, 'shop/shop.html', context)
	if data:
		resp.set_cookie('data', data, max_age = None, expires = None)
	return resp

def bye(request):
	data = request.COOKIES['data']
	introducer = NetflixUser.objects.filter(user_token=data).first()

	if introducer:
		score = introducer.earn_score
		introducer.score = score
		introducer.save()
		customer, created = Customer.objects.get_or_create(email='guest@company.com')
		customer.introducer = introducer
		customer.name = 'guest'
		customer.save()
	else:
		customer, created = Customer.objects.get_or_create(email='guest@company.com')
		customer.name = 'guest'
		customer.save()
	return render(request, 'shop/shop.html', {'data': data})