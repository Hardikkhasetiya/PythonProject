
from django.shortcuts import render , redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import  check_password
from django.views import View



class Login(View):
    def get(self , request):
        return render(request, 'login.html')
    def post(self ,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                return redirect('homepage')
            else:
                error_message = "password not valid!"
        else:
            error_message = "email or password not valid!"
        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error': error_message})