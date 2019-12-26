from django.shortcuts import render
from django.views.generic import(
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView,
    )
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    login_url = '/admin/'


#rertrieve
class TweetDetailView(DetailView):
    template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    template_name = 'tweets/list_view.html'

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                )
        return qs

    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context

# Update View
class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    # success_url = "/tweet/"
    login_url = "/admin/"


#Delete View
class TweetDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "tweets/delete_confirm.html"
    model = Tweet
    success_url = reverse_lazy("tweet:list")











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
