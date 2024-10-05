from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    sparc2028members = Member.objects.all().values()
    template = loader.get_template("allmembers.html")
    context = {
        'mymembers' : sparc2028members,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  x = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'x': x,
  }
  return HttpResponse(template.render(context, request))