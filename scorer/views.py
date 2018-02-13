from django.shortcuts import render, redirect
from .models import Paper, User, PaperUser
from .forms import ArticleCheckerForm
import scraper

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ArticleCheckerForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            username = form.cleaned_data['username']
            request.session['username'] = username
            request.session['url'] = url
            return redirect('/scorer/result')
    else:
        form = ArticleCheckerForm()

    return render(
        request,
        'index.html',
        context={'form': form},
    )


def leaderboards(request):
    users = User.objects.all()
    papers = Paper.objects.all()
    paperusers = PaperUser.objects.all()
    lists = []
    # You can get referrer from paper
    for paper in papers:
        # Returns list of referrer, referee pairs of each url, referrer is the same
        searchedPaperUser = paperusers.filter(url=paper.url)
        lists.append([paper.url, paper.title, paper.referrer,
                      searchedPaperUser.count()])
    lists.sort(key=lambda x: x[3], reverse=True)
    return render(
        request,
        'leaderboard.html',
        context={'lists': lists},
    )


'''
URL is link of article
checker is username of user who is currently checking the article out
'''


def result(request):
    url = request.session['url']
    username = request.session['username']

    searchPaper = Paper.objects.all().filter(url=url)
    searchUser = User.objects.all().filter(username=username)
    # Check if such a user exists
    if not searchUser:
        currUser = User(username=username.lower())
        currUser.save()
    else:
        currUser = searchUser[0]
    # Check if entry exists
    if searchPaper:
        paper = searchPaper[0]
        title, body, stance = paper.title, paper.body, paper.stance
        cZero = paper.referrer.username
        # Check if user is the same as in the entry
        if paper.referrer == currUser:
            print(
                "Same user who intially wanted to check this article now wants to recheck")
        else:
            paperUserSearch = PaperUser.objects.all().filter(
                url=paper.url, referrer=paper.referrer, referree=currUser)
            # If there is no existing entry
            if not paperUserSearch:
                # Different user is querying
                PaperUser(url=paper.url, referrer=paper.referrer,
                          referree=currUser).save()
    else:
        cZero = currUser.username
        # Only parse if article does not exist
        title, body, stance = scraper.parseArticle(url)
        Paper(url=url, title=title, body=body,
              stance=stance, referrer=currUser).save()

    if stance == 'agree':
        detail = 'The headline agrees with the body of the article'
    elif stance == 'disagree':
        detail = 'The headline disagrees with the body of the article'
    elif stance == 'discuss':
        detail = 'The body text does not take a position but talks about the same topic as the headline.'
    elif stance == 'unrelated':
        detail = 'The body text talks about a different topic compared to the headline. This might be a clickbait/dubious news'
    return render(
        request,
        'result.html',
        # context={},
        context={'title': title, 'body': body,
                 'stance': stance, 'detail': detail, 'checkerZero': cZero},
    )
