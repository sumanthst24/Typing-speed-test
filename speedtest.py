import random
import time
import sys
from threading import Timer

def speedCalculation(sen,initial,final):
    words=sen.count(" ")+1
    timediff=final-initial
    return (words/timediff)


def accuracyCalculation(sen,written):
    if(len(sen)==len(written)):
        count=0
        for i in range(0,len(sen)):
            if(sen[i]==written[i]):
                count=count+1
        return (count/len(sen))

    elif(len(sen)>len(written)):
        print("You haven't entered the complete text")
        count=0
        minlength=min(len(sen),len(written))
        for i in range(0,minlength):
            if(sen[i]==written[i]):
                count=count+1
        return (count/len(sen))

    elif(len(sen)<len(written)):
        print("You have entered the incorrect text")


def collectSentence():
    sentenceslist=[]
    with open ('sentences.txt', 'rt') as myfile:
        for myline in myfile:
            sentenceslist.append(myline.rstrip())
            #print(myline) 
            #print(sentenceslist)
    return sentenceslist


def playGame():    
    sentenceslist=collectSentence()
    sentenceindex=random.randrange(0,len(sentenceslist),2)
    sen=sentenceslist[sentenceindex]
    print(sen)
    starttime=time.time()
    st=input()
    endtime=time.time()
    #print(starttime,endtime)
    if(round(accuracyCalculation(sen,st)>=0.9)):
       print("You have good typing skills")
       print("Your accuracy is "+str(round(accuracyCalculation(sen,st)*100,2)))
    print(str(round(speedCalculation(sen,starttime,endtime)*60,2))+" words/minute")




while(1):
    print("Test your typing skills here")
    print("Choose your option")
    print("1.Start the test")
    print("2.Exit")
    #print("The system closes automatically if you choose nothing")
    n=(input())
    if(int(n)<0 and int(n)>2):
        print("Invalid Option")
        sys.exit()
    elif(n=='1'):
        playGame()
    elif(n=='2'):
        sys.exit()
    else:
        print("You selected an invalid option")
        sys.exit()


