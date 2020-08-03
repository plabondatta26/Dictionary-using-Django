from django.shortcuts import render, redirect
from .forms import  add_word, input_form
from .models import Dictionary
from django.contrib import messages
# Create your views here.
def home(request):
    form = input_form()
    return render(request, 'home.html', {'form':form})

def get_query(request):
    form = input_form(request.GET)
    print(form)
    if form.is_valid():
        word = form.cleaned_data['word']
        dictionary = Dictionary.objects.filter(word=word).first()
        if dictionary is None:
            messages.error(request, ('word was not found in Dictionary'))
            return render(request, 'home.html', {'form':form})
        contex ={'form':form, 'definition': dictionary.definition}
        return render(request, 'home.html', contex)
    messages.error(request, 'your input has error')
    return render(request, 'home.html',{'form':form})

def about(request):
    contex ={}
    return render(request, 'about.html', contex)

def content(request):
    all_words = Dictionary.objects.all()
    if request.method =="POST":
        form = add_word(request.POST)
        if not form.is_valid():
            messages.success(request, "You should add a word and definition to the dictionary")
            return render(request, 'content.html', {'form': form, 'all_words': all_words})
        form.save()
        messages.success(request,"Your word has been saved to the dictionary")
    return render(request, 'content.html', {'form':add_word(), 'all_words': all_words})

def delete(requst, id):
    words = Dictionary.objects.get(id=id)
    words.delete()
    messages.success(requst, 'Word is deleted!!')
    return redirect('content')