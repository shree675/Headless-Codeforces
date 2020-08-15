from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import csv

class CodeForces:
    
    def __init__(self):
        self.opts=Options()
        self.opts.set_headless()
        self.browser=Chrome(options=self.opts)
        
    def close(self):
        self.browser.close()

    def getTopRated(self):
        try:
            self.browser.get('https://www.codeforces.com')
            section=self.browser.find_elements_by_tag_name('table')
            newsec=section[0].text
            newsec=newsec[14:]
            newsec=newsec.split('\n')
            l=[]
            for i in range(len(newsec)):
                n=newsec[i].split(' ')
                l.append(n)
            with open('top_rated.csv','w') as fil:
                f=csv.writer(fil)
                f.writerow(['RANK','USERNAME','RATING'])
                for i in range(len(l)):
                    f.writerow(l[i])
            print('Successfully created/updated "top_rated.csv"')
        except Exception as e:
            print('Error occured')
            print(e)

    def getTodaysProblems(self):
        try:
            self.browser.get('https://www.codeforces.com/problemset')
            section=self.browser.find_elements_by_class_name('problems')
            newsec=section[0].text
            newsec=newsec[9:]
            newsec=newsec.split('\n')
            l=[];n=[];ids=[];newl=[None for i in range(2*len(l))];final=[None for i in range(len(l))];d=[]
            for i in range(len(newsec)):
                if (i%4)==1:
                    n.append(newsec[i])
            for i in range(len(newsec)):
                if (i%4)==0:
                    ids.append(newsec[i])
            for i in range(len(newsec)):
                if (i%4)==3:
                    l.append(newsec[i])
            for i in range(len(l)):
                newl.append(l[i].split(' '))
            for i in range(len(newl)):
                if newl[i][0]=='':
                    d.append('None')
                    continue
                val=int(newl[i][0])
                if val>0 and val<=1700:
                    d.append('Easy')
                elif val>1700 and val<=2600:
                    d.append('Medium')
                else:
                    d.append('Hard')
            with open('todays_problem_set.csv','w') as fil:
                f=csv.writer(fil)
                f.writerow(['ID','PROBLEM','LEVEL','DIFFICULTY'])
                for i in range(len(n)):
                    f.writerow([ids[i],n[i],newl[i][0],d[i]])
            print('Successfully created/updated "todays_problem_set.csv"')
            print('Note: Problem sets change from time to time')
        except Exception as e:
            print('Error occured')
            print(e)

    def getLatestContest(self):
        try:
            self.browser.get('https://codeforces.com/contests')
            section=self.browser.find_element_by_class_name('sidebox')
            newsec=section.text.split('\n')
            name=newsec[2]
            section2=self.browser.find_elements_by_class_name('dark')
            d=section2[2].text
            d=d[:len(d)-7]
            l=section2[3].text
            with open('upcoming_contest.txt','w') as fil:
                fil.write('UPCOMING CONTEST:\n\n')
                fil.write('Name of the contest: '+name+'\n')
                fil.write('Begin date: '+d+' UTC+5.5\n')
                fil.write('Duration: '+l+'hrs\n')
            print('Successfully created/updated "upcoming_contest.txt"')
        except Exception as e:
            print('Error occured')
            print(e)

c=CodeForces()
c.getTopRated()
c.getTodaysProblems()
c.getLatestContest()
c.close()