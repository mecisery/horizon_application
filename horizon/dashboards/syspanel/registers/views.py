from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.views.generic import list_detail
from forms import RegistrationForm
from keystoneclient.v2_0 import client

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  
            email = form.cleaned_data['email']  
            password = form.cleaned_data['password1']  

            keystone = client.Client(username="admin", password="123qwe", tenant_name="admin", auth_url="http://localhost:5000/v2.0")

            tenant = keystone.tenants.create(tenant_name="test2", description="1ssy new tenant!", enabled=True)

            user= keystone.users.create(username, password, email, "e798654a2f5148bfa86bff350e64f835", enabled=True)

            if user:
                return HttpResponse("Register Success!")  
                #return HttpResponseRedirect('/main/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request,{'form':form})
    return render_to_response('syspanel/registers/register.html',variables)
