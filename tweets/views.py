from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Tweet

from .forms import TweetModelForm

# Create your views here.
# def create(request):
#     pass
class TweetCreateView(CreateView):
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweet/create/"
    # fields = [
    #     "content",
    # ]

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TweetCreateView,self).form_valid(form)

#rertrieve
class TweetDetailView(DetailView):
    template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()


# def tweet_detail_view(request,id=1):
#     tweet = Tweet.objects.get(id=id)
#     print(tweet)
#     context = {'tweet':tweet}
#     return render(request,'tweets/detail_view.html',context)
#
# def tweet_list_view(request,id=1):
#     query_set = Tweet.objects.all()
#     print(query_set)
#     context = {
#         'query_set':query_set
#     }
#     return render(request,'tweets/list_view.html',context)

def update(request):
    pass

def delete(request):
    pass
