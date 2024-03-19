from django.shortcuts import render
from .models import Feedback
from .models import Product
from django.http import JsonResponse
import re
import re
from django.shortcuts import render
from .models import Feedback
from django.shortcuts import render, redirect



def contactfunction(request):
    if request.method == "POST":
        name = request.POST.get('n')
        phone = request.POST.get('number')
        email = request.POST.get('mail')
        feedback = request.POST.get('feed')

        # Check for phone length and email validity before creating the Feedback object
        if len(phone) > 10 or len(phone)<10:
            m2 = "Phone number should be 10 digits."
            return render(request, "customerapp/contact.html", {"msgm2": m2})
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            m3 = "Invalid email address. Please enter a valid email."
            return render(request, "customerapp/contact.html", {"msgm3": m3})
        else:
            contact = Feedback(name=name, phone=phone, email=email, feedback=feedback)
            contact.save()
            m1 = "Your Feedback Was Sent Successfully!!"
            return render(request, "customerapp/contact.html", {"msgm1": m1})

    return render(request, "customerapp/contact.html")


def greeting(request):
    return render(request,"customerapp/greeting.html")


def search_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query)

    # Add these lines for debugging
    print(f"Search Query: {query}")
    print(f"Number of Products Found: {products.count()}")

    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'customerapp/search_results.html', context)


def search_view1(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query)

    # Add these lines for debugging
    print(f"Search Query: {query}")
    print(f"Number of Products Found: {products.count()}")

    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'customerapp/search_results1.html', context)



def search_suggestions(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(title__icontains=query).values_list('title', flat=True)
    suggestions = list(products)
    return JsonResponse({'suggestions': suggestions})


