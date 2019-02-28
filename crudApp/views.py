from django.shortcuts import render , redirect , get_object_or_404
from .forms import ContactForm , ContactModel

# Create your views here.
# name , email , phoneNumber
# superuser name:admin Password:test4321
# each view gets a responding template html page
def index(request):
    modelList = ContactModel.objects.all()
    # this page simply renders the entire list when you open it and the necessary spots to create a new user
    context=\
        {
            'contactList':modelList,
        }
    return render(request,'crudApp/index.html', context)


def createUser(request):
    form = ContactForm(request.POST or None)
    # this opens the form runs it through twice and then sends back to index for simple runtime
    if form.is_valid():
       form.save()
       return redirect('index')

    return render(request,'crudApp/createUser.html',{'form':form})


def deleteUser(request,userID):
    removed = get_object_or_404(ContactModel, pk= userID)
    if request.method == 'POST':
        removed.delete()
        return redirect('index')
    # this only needs to compare the info and make sure the person wants to delete it
    return render(request,'crudApp/deleteUser.html',)


def updateUser(request,userID):
    user = get_object_or_404(ContactModel,pk=userID)
    formData = ContactForm(request.POST or None, instance= user)
    if formData.is_valid():
        formData.save()
        return redirect('index')
    # this collects the info from models and uses form to display and allow it to be changed
    return render(request,'crudApp/updateUser.html',{'form':formData})