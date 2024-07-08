from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import city

def cityMain(request):
  city = City.objects.first()
  return render(request, 'cityMain.html', {'city': member})
  
  #template = loader.get_template('cityMain.html')
  #return HttpResponse(template.render())

  def main_page(request):
    # Get the first city in the database
    city = City.objects.first()
    return render(request, 'main_page.html', {'city': city})


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

def handle_invalid_path(request, invalid_path):
    return render(request, '404.html')