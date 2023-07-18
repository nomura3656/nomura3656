from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product  # Productモデルをインポート

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_product(request):  # 追加
    if request.method == 'POST':
        product_name = request.POST['product_name']
        price = request.POST['price']
        release_date = request.POST['release_date']
        description = request.POST['description']
        image_url = request.POST['image_url']

        product = Product(product_name=product_name, price=price, release_date=release_date, description=description, image_url=image_url)
        product.save()

        return redirect('success')  # Success.htmlへリダイレクト
    else:
        return HttpResponse('Invalid request')

def success(request):
    return render(request, 'success.html')