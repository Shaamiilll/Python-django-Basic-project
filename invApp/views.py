from django.shortcuts import render , redirect

# Create your views here.
from .forms import ProductForm
from .models import Product

#Home view
def home_view(request):
    return render(request ,'invApp/home.html')

#create view
def product_crate_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request ,'invApp/product_form.html', {'form':form})    


# read view
def  product_list_view(request):
    products = Product.objects.all()
    return render(request ,'invApp/product_list.html', {'products':products})

#Update view
def product_update_view(request, product_id):
    # Use product_id instead of id
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)  # Fix: pass the correct instance
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)  # Fix: Use form variable
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})  # Corrected template name



# Delete view
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request , 'invApp/product_confirm_delete.html',{'product':product})