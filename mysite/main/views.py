from django.shortcuts import render, redirect, get_object_or_404
from .models import Cafe
from .forms import CafeForm
# from django.core import serializers
import django.core.serializers
import django.http
# import models



# serializing 
# 여러개 불러올때
def testSerialize(request):
    s = django.core.serializers.serialize('json',Cafe.objects.all())
    # s is a string with [] around it, so strip them off
    # o=s.strip("[]")
    return django.http.HttpResponse(s)



# 한개만 가져올때 
def testSerialize_one(request,pk):
    s = django.core.serializers.serialize('json',[Cafe.objects.get(id=pk)])
    # s is a string with [] around it, so strip them off
    o=s.strip("[]")
    return django.http.HttpResponse(o)



# 제주카페찾기 사이트 관련 함수
def index(request):
    if request.method == "POST":
        print(request)
        print(request.POST.keys())
        
        keys = list(request.POST.keys())
        keys.remove('csrfmiddlewaretoken')
        print(keys[0])
        
        cafelistobj = []
        cafelistobjall = Cafe.objects.all()
        print(cafelistobj)
        print(type(cafelistobj))
        print(dir(cafelistobj))
    
        for key in keys:
            for cafelist in cafelistobjall:
                print(cafelist['tag'], key, cafelist.tag == key)
                cafetag = list(cafelist.tag.values())
                print(cafetag[0]['name'], key, cafetag[0]['name'] == key)
                if cafetag[0]['name'] == key:
                    cafelistobj.append(cafelist)
        print(cafelistobj)
        return render(request, 'main/cafe/cafelist.html', {'cafelistobj':cafelistobj})
    return render(request, 'main/index.html')


def cafeindex(request):
    return render(request, 'main/cafe/cafeindex.html')

def about(request):
    return render(request, 'main/cafe/about.html')

def cafelist(request):
    cafelistobj = Cafe.objects.all()
    if request.method == "POST":
        form = CafeForm(request.POST, request.FILES)
        if form.is_valid():
            cafe = form.save(commit=False)
            cafe.save()
            return render(request, 'main/cafe/cafedetails.html', {'cafeobj': cafe})
    return render(request, 'main/cafe/cafelist.html', {'cafelistobj':cafelistobj})

def cafedetails(request, pk):
    cafeobj = Cafe.objects.get(pk=pk)
    return render(request, 'main/cafe/cafedetails.html', {'cafeobj':cafeobj})

def new(request):
    form = CafeForm()
    return render(request, 'main/cafe/write.html', {'form': form})

def cafe_update(request, pk):
    cafeobj = Cafe.objects.get(pk=pk)
    cafe = get_object_or_404(Cafe, pk=pk)
    form = CafeForm(request.POST or None, instance=cafe)
    if form.is_valid():
        form.save()
        return redirect('../cafelist')
    return render(request, 'main/cafe/update.html', {'form':form, 'cafeobj':cafeobj})

def cafe_delete(request, pk, template_name='main/cafe/cafe_confirm_delete.html'):
    cafe= get_object_or_404(Cafe, pk=pk)
    if request.method=='POST':
        cafe.delete()
        return redirect('../cafelist')
    return render(request, template_name, {'object':cafe})

# def book_update(request, pk, template_name='books/book_form.html'):
#     book= get_object_or_404(Book, pk=pk)
#     form = BookForm(request.POST or None, instance=book)
#     if form.is_valid():
#         form.save()
#         return redirect('book_list')
#     return render(request, template_name, {'form':form})



# 회원 목록 받아서 탬플렛으로 보내주기 함수
# def memberlist(request):
#     memberlistobj = Member.objects.all()  
#     return render(request, 'main/memberlist.html', {'memberlist':memberlistobj})

# FAQ의 목록 받아서 탬플렛으로 보내주기 함수
# def faqlist(request):
#     faqlistobj = Faq.objects.all()
#     return render(request, 'main/faq.html', {'faqlistobj':faqlistobj})


