from django.http import HttpResponse
from django.template import loader

def cityMain(request):
  template = loader.get_template('cityMain.html')
  return HttpResponse(template.render())

def cityNews(request):
  template = loader.get_template('cityNews.html')
  return HttpResponse(template.render())

def cityAdministration(request):
  template = loader.get_template('cityAdministration.html')
  return HttpResponse(template.render())

def cityFacts(request):
  template = loader.get_template('cityFacts.html')
  return HttpResponse(template.render())

def cityContacts(request):
  template = loader.get_template('cityContacts.html')
  return HttpResponse(template.render())

def cityHistory(request):
  template = loader.get_template('cityHistory.html')
  return HttpResponse(template.render())