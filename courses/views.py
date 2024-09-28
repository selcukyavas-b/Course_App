from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

from courses.forms import CourseCreateForm
from .models import Course, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

data={
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

db={
    "courses":[
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"1.jpg",
            "slug":"javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title":"python kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"2.jpg",
            "slug":"python-kursu",
            "date": date(2022,9,10),
            "isActive": False,
            "isUpdated": False

        },
        {
            "title":"web geliştirme kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"3.jpg",
            "slug":"web-geliştirme-kursu",
            "date": date(2022,8,10),
            "isActive": True,
            "isUpdated": True
        }


    ],
    "categories": [
        {"id":1, "name":"programlama","slug":"programlama"},
        {"id":2, "name":"web gelistirme","slug":"web-gelistirme"},
        {"id":3, "name":"mobil uygulamalar","slug":"mobil-uygulamalar"},
    ]
        
    

}



def index(request):
    # list comphension
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    kategoriler= Category.objects.all()
    
    # for kurs in db['courses']:
    #     if kurs["isActive"]==True:
    #         kurslar.append(kurs)

    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar

    })

def isAdmin(user):
    return user.is_superuser


@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/kurslar")
    else:
        form = CourseCreateForm()
    
    return render(request, "courses/create-course.html", {"form":form})


    


    # if request.method == "POST":
        

    #     title=request.POST["title"]
    #     description=request.POST["description"]
    #     imageUrl=request.POST["imageUrl"]
    #     slug=request.POST["slug"]

    #     # if isActive == "on":
    #     #     isActive = True
        
    #     # if isHome == "on":
    #     #     isHome = True


    #     error = False
    #     msg=""

    #     if title =="":
    #         error=True
    #         msg += "Title zorunlu bir alan."
        
    #     if len(title) < 5:
    #         error = True
    #         msg += " Title için en az 5 karakter girmelisiniz"
        
    #     if error:
    #         return render(request, "courses/create-course.html", {"error": True, "msg": msg})
        
    #     kurs = Course(title=title, description=description, imageUrl=imageUrl, slug=slug, isActive=isActive, isHome=isHome)

    #     kurs.save()

    #     return redirect("/kurslar")

  


    


def search(request):
    if "q" in request.GET and request.GET["q"] !="":
        q=request.GET["q"]
        kurslar= Course.objects.filter(isActive=True,title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")
    

    


    return render(request, 'courses/search.html',{
        'categories': kategoriler,
        'courses': kurslar,

    })

def details(request, slug):
    # try:
    #     course = Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()
    course=get_object_or_404(Course, slug=slug)
    context={
        'course': course

    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar= Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = Category.objects.all()

    paginator=Paginator(kurslar,2)
    page=request.GET.get('page',1)
    page_obj=paginator.page(page)

    print(page_obj,paginator.count)
    print(page_obj.paginator.num_pages)

    return render(request, 'courses/list.html',{
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug

    })

    # try:
    #     category_text=data[category_name]
    #     return render(request,'courses/kurslar.html', {
    #         'category': category_name,
    #         'category_text': category_text

    #     })
    # except:
    #     return HttpResponseNotFound("yanlış kategori seçimi")

# def getCoursesByCategoryId(request, category_id):
#     category_list=list(data.keys())
#     if(category_id > len(category_list)):
#         return HttpResponseNotFound("yanlış kategori seçimi")

#     category_name=category_list[category_id - 1]

#     redirect_url=reverse('courses_by_category', args=[category_name])

#     return redirect(redirect_url)



    






