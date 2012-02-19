from mainpage.models import  Seller, Product, Category
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def main_index(request):

    sellers = Seller.objects.all()
    msg = "Showcase!!!"
    return render_to_response('main/index.html',{
    'sellers':sellers,},
    context_instance = RequestContext(request))

def seller(request, slug):
    seller = get_object_or_404(Seller, slug=slug)

    return render_to_response('main/index.html', {
    'seller':seller
    }, context_instance=RequestContext(request))