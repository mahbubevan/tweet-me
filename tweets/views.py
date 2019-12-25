from django.shortcuts import render

from .models import Tweet
# Create your views here.

def create(request):
    pass

#rertrieve
def tweet_detail_view(request,id=1):
    tweet = Tweet.objects.get(id=id)
    print(tweet)
    context = {'tweet':tweet}
    return render(request,'tweets/detail_view.html',context)

def tweet_list_view(request,id=1):
    query_set = Tweet.objects.all()
    print(query_set)
    context = {
        'query_set':query_set
    }
    return render(request,'tweets/list_view.html',context)

def update(request):
    pass

def delete(request):
    pass
