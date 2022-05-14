from django.shortcuts import render, redirect  
from contact.forms import contactForm  
from contact.models import contact  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = contactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = contactForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    contacts = contact.objects.all()  
    return render(request,"show.html",{'contacts':contacts})  
def edit(request, id):  
    contact = contact.objects.get(id=id)  
    return render(request,'edit.html', {'contact':contact})  
def update(request, id):  
    contact = contact.objects.get(id=id)  
    form = contactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'contact': contact})  
def destroy(request, id):  
    contact = contact.objects.get(id=id)  
    contact.delete()  
    return redirect("/show")