from django.shortcuts import render
from django.views import generic
from create.models import create_code
from django.views.generic.edit import CreateView,DeleteView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.

class IndexView(generic.ListView):
    template_name ='create/index.html'

    def get_queryset(self):
        return create_code.objects.all()


class CodeCreate(CreateView):
    model=create_code
    template_name = 'create/detail.html'
    fields=['slug','lang','content','expire']


def result(request, slug):
    object=create_code.objects.get(slug=slug)
    context={
        'object': object
    }
    return render(request,'create/result.html',context)

def addObject(request):
    print(request.method)
    content = request.POST['content']
    lang = request.POST['lang']
    slug = request.POST['slug']
    print(slug)
    print(content)
    expire = '1'
    newPaste = create_code(content=content, lang=lang, slug=slug, expire=expire)
    newPaste.save()
    rs = '/create/result/' + str(slug)
    return HttpResponseRedirect(rs);

def modify(request, slug):
    code = create_code.objects.get(slug=slug)
    code.content = request.POST['content']
    print(code.content)
    code.save()
    rs = '/create/result/' + str(slug)
    return redirect(rs);

class DeleteObject(DeleteView):
    model=create_code
    success_url=reverse_lazy('create:detail')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
