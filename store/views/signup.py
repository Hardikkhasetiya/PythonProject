from django.shortcuts import render, redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        firstname = postdata.get('firstname')
        lastname = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        # validation
        value = {'firstname': firstname, 'lastname': lastname, 'phone': phone,
                 'email': email, 'password': password}
        customer = Customer(firstname=firstname, lastname=lastname, phone=phone, email=email, password=password)
        error_message = None
        if (not firstname):
            error_message = "firstname is required"
        elif (len(firstname)) < 4:
            error_message = "firstname is required"

        elif (not lastname):
            error_message = "lastname is required"
        elif (len(lastname)) < 4:
            error_message = "lastname is required"

        elif (not phone):
            error_message = "phone is required"
        elif (len(phone)) < 10:
            error_message = "phone is required"

        elif (len(email)) < 5:
            error_message = "email must be 5 char long"
        elif (len(password)) < 6:
            error_message = "password must be 6 char long"
        elif customer.isExists():
            error_message = "email address already registered.."

        # saving
        if (not error_message):
            print(firstname, lastname, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {'error': error_message, 'values': value}
            return render(request, 'signup.html', data)
