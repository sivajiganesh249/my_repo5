from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movie_news_view(request):
    news1='In Telugu Devdas Movie is not good'
    news2='Sonali slowly getting curing'
    news3='Amithab bachan next movie is thugs of Hindustan'
    news4='Salman and Katrina are going to marry'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'testapp/mnews.html',my_dict)

def politic_news_view(request):
    news1='CM YS Jagan Reddy launched Ammavodi scheme to benficers'
    news2='Pawan Kalyan meets Modi'
    news3='Collector says that There is no COVID case in kadapa still now'
    news4='Complaint Against SEC Nimmagadda For Cheating AP Govt By Claiming HRA'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'testapp/pnews.html',my_dict)

def sports_news_view(request):
    news1='A Great Partnership contributes Ashwin & Vihari'
    news2='India won the Badminton championship 2020'
    news3='Rohit Sharma visited Tirumala yesterday'
    news4='India won Border-Gavaskar Trophy 2021 with lead of 2-1'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'testapp/snews.html',my_dict)
