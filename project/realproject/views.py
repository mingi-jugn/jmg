from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import RstForm,ProductForm,PcommentForm
from .models import Test,Product,Pcomment


# Create your views here.
def index1(request):
    return render(request,'index.html')



def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = RstForm(request.POST, request.FILES)
        if form.is_valid():
            test = Test(
                subject=form.cleaned_data["subject"],
                summary=form.cleaned_data["summary"],
                upload_date=form.cleaned_data["upload_date"],
                image=form.cleaned_data["image"],
                acount=form.cleaned_data["acount"],
            )
            test.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'testgallery.html', {'form': form, 'img_obj': img_obj})
    else:
        form = RstForm()
    return render(request, 'testgallery.html', {'form': form})


def product(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            test = Product(
                subject=form.cleaned_data["subject"],
                price=form.cleaned_data["price"],
                upload_date=form.cleaned_data["upload_date"],
                image=form.cleaned_data["image"],
            )
            test.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return redirect('showindex')
            #return render(request, 'Product.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'Product.html', {'form': form})

def showindex(request):
    tests = Product.objects.all().order_by('-upload_date')
    paginator = Paginator(tests, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        "tests": tests,
        "page_obj": page_obj
    }
    return render(request,"showindex.html",context)



#def blog_index(request):
    #post = Post.object.all().order_by('created_on')
    #context={
        #"post":post,
    #}
    #return render(request,"blog_index.html",context)

def sample1(request):
    return render(request, "sample1.html")


def album(request):
    tests = Product.objects.all().order_by('-upload_date')
    context = {
        "tests": tests,
    }
    return render(request, "album.html", context)

def showdetail(request, subject):
    product= Product.objects.get(subject=subject)
    pcomments = Pcomment.objects.filter(product=product)

    if request.method == "POST":
        form = PcommentForm(request.POST)
        if form.is_valid():
            pcomment = Pcomment(
                name=form.cleaned_data["name"],
                content=form.cleaned_data["content"],
                product=product,
            )
            pcomment.save()

            context = {
                "product": product,
                "pcomments": pcomments,
                "form": form
            }
            return render(request, "pcomments.html", context)

    else:
        form = PcommentForm()
        context = {
            "product": product,
            "form": form,
            "pcomments": pcomments
        }
    return render(request, 'pcomments.html', context)




   # context={
        #"tests": tests,
    #}
    #return render(request,"showdetail.html",context)








