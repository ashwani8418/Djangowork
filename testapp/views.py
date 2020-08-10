from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movies_page_view(request):
    news1='''Aishwarya Rai Bachchan remembers Saroj Khan; shares, "had so many memorable experiences dancing under your guidance"'''
    news2="Happy birthday Tom Cruise: Here are some of the lesser-known facts about the action actor that every fan must know"
    news3='''Bhumika Chawla pens a heart-wrenching final good-bye to Sushant Singh Rajput, "It's been almost 20 days and I wake up thinking of you"'''
    news4="Neetu Kapoor and Riddhima Kapoor Sahni proud of Bharat Sahni for donating plasma encourages other patients recovered from coronavirus to do the same"
    news5="Exclusive: Lagaan actress Gracy Singh remembers the time when Saroj Khan choreographed Radha Kaise Na Jale"
    news6="Saroj Khan passes away: Kriti Sanon mourns the loss of ace choreographer, says 'there was no one else like you masterji'Sooraj Pancholi: Sushant Singh Rajput was really good to me and I respected him as my senior"
    news7="Sooraj Pancholi: Sushant Singh Rajput was really good to me and I respected him as my senior"
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6,'news7':news7}
    return render(request,'testapp/movies.html',my_dict)

def politics_page_view(request):
    p1="Anil Baluni, BJP National Media Head, to Get Priyanka Gandhi's Lodhi Estate Bungalow"
    p2="Bhupinder Hooda Dares Manohar Lal Khattar to Contest Baroda Assembly Bypoll against Him"
    p3="RJD Celebrates Foundation Day Without Lalu Prasad; Sons Take Out Bicycle Rally"
    p4="PM Cares Fund Putting Lives at Risk: Rahul Gandhi Questions Purchase of 'Substandard' Ventilators'"
    p5="With Devt Agendas and Discussions, BJP, Congress Intensify Preparations for Madhya Pradesh Bypolls"
    p6="TMC Worker Hacked to Death, SUCI Member Found Hanging as Clashes Break Out in West Bengal's Kultali"
    p7="Siddaramaiah Asks Karnataka Govt to Evaluate if SSLC Exams Were Held Safely amid Covid-19 Pandemic"
    my_dict={'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7}
    return render(request,'testapp/politics.html',my_dict)
