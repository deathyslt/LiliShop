from django.shortcuts import render,get_object_or_404

from django.http import JsonResponse 

def show_all_stores(request):
    return JsonResponse({"status" : "niiice"})

def show_store_flowers(request,store_name):
    return JsonResponse({"status" : store_name})


# class show_store_flowers():
