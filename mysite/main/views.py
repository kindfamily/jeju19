# import pdb 
# pdb.set_trace() 파이썬 디버깅 방법 원하는 곳에 코드 넣기
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cafe
from .forms import CafeForm



# 제주카페찾기 사이트 관련 함수

def index(request):
    if request.method == "POST":
        #print(request)
        #print(request.POST.keys())
        
        keys = list(request.POST.keys())
        keys.remove('csrfmiddlewaretoken')
        #print(keys[0])
        
        cafelistobj = []
        cafelistobjall = Cafe.objects.all()
        #print(cafelistobj)
        #print(type(cafelistobj))
        #print(dir(cafelistobj))
    
        for key in keys:
            for cafelist in cafelistobjall:
                #print(cafelist['tag'], key, cafelist.tag == key)
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

def write(request):
    form = CafeForm()
    return render(request, 'main/cafe/write.html', {'form': form})

def cafe_update(request, pk):
    cafe = get_object_or_404(Cafe, pk=pk)
    form = CafeForm(request.POST or None, instance=cafe)
    if form.is_valid():
        form.save()
        return redirect('cafelist')
    return render(request, 'main/cafe/write.html', {'form':form})

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


