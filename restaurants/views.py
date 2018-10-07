from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    restaurants=[{'restaurant_name':'Potatoes','food_type':'All things potatoes!'},{'restaurant_name':'Steakhouse','food_type':'All things meat!'},{'restaurant_name':'Mexicana','food_type':'Mexican'}]
    context = {"my_list": restaurants}
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
 "my_object": {
            "restaurant_name":"Mexicana",
            'food_type':"Mexican"
    }}
    return render(request, 'detail.html', context)
