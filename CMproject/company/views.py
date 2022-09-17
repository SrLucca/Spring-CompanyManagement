from django.shortcuts import render
from company.forms import companyRegister
from django.contrib import messages

# Create your views here.

def registerCompanyView(request):
    
    if request.method == "POST":
        form = companyRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, "Erro no cadastro da empresa.")
            return redirect("/register-company")
    else:
        form = companyRegister()
    
    return render(request, "pages/register_company.html", {"form":form})