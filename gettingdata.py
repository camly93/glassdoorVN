def GetDetailLINK(link,linklist):
    r = request.urlopen(link)
    html_source = r.read()
    soup = bs4.BeautifulSoup(html_source, 'html.parser')
    fin=soup.find_all('tr',{'class':'job-post'})
    for x in fin:
        a=x.find_all('div',{'class':'col-sm-8 col-sm-pull-3'})
        for b in a:
            g=b.find_all('div',{'class':" new-job"})
            c=b.find_all('div',{'class':' '})
            v=b.find_all('div',{'class':"bold-red new-job"})
            l=b.find_all('div',{'class':"bold-red "})
            for d in c:
                linklist.append(d.a['href'])
            for d in g:
                linklist.append(d.a['href'])
            for d in v:
                linklist.append(d.a['href'])
            for d in l:
                linklist.append(d.a['href'])
    temp=soup.find('li',{'class':'next'})
    print(len(linklist))
    if temp==None:
        return 0
    else:
        link = 'http://www.vietnamworks.com' + temp.a['href']
        return GetDetailLINK(link,linklist)


def getjobdetail(link,jobdetail):
    r=request.urlopen(link)
    html_source=r.read()
    # print(html_source)
    soup=bs4.BeautifulSoup(html_source,'html.parser')#just remember-----we are at body
    # f=soup.find('span',{'class':"center-block text-center box-limit"})
    tempdict={}
    f=soup.find('div',{'class':"col1 col-md-3 employer-logo"})
    if f is not None:
        if f.a is not None:
            tempdict.update({'logo':f.a.img['src']})
        else:
            tempdict.update({'logo':'None'})
    else: tempdict.update({'logo':'None'})
    f=soup.find('h1',{'itemprop':"title"})
    tempdict.update({'title':f.get_text()})
    f=soup.find('span',{'class':"company-name text-lg block"})
    tempdict.update({'company':f.get_text().strip()})
    f=soup.find('span',{'class':"company-address block"})
    tempdict.update({'address':f.get_text().strip()})
    f=soup.find('a',{'itemprop':"addressLocality"})
    tempdict.update({'location':f.get_text().strip()})
    # f=soup.find('div',{'class':"link-list"})
    # tempdict.update({'position':f.get_text().strip()})
    f=soup.find('div',{'id':"job-detail"})
    tempdict.update({'detail':f.get_text().strip().strip()})
    f=soup.find('span',{'id':"companyprofile"})
    tempdict.update({'companyinfo':f.get_text().strip()})
    jobdetail.append(tempdict)
    f = soup.find(lambda tag: tag.name == 'div' and
                              tag.get('class') == ['link-list'])
    posi = f.find('div', {'class': "list-group"})
    tempdict.update({'position':posi.a.get_text()})
    jobtype = f.find('div', {'class': "list-group push-top-xs"})
    types = jobtype.find_all('a')
    templist=[]
    for x in types:
        templist.append(x.get_text())
    tempdict.update({'jobgroup':templist})
    date = soup.find('div', {'class': "pull-right text-gray-light"})
    tempdict.update({'dateandview': date.get_text()})
    print(len(jobdetail))
    print(jobdetail[len(jobdetail)-1])

import pymongo
db_uri='mongodb://Raventine:raven123@ds013564.mlab.com:13564/job-offer'
db=pymongo.MongoClient(db_uri).get_default_database()#mongo data
from urllib import request
import bs4
link='http://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam'#link
r=request.urlopen(link)
html_source=r.read()
# print(html_source)
soup=bs4.BeautifulSoup(html_source,'html.parser')#just remember-----we are at body
linklist=[]
GetDetailLINK(link,linklist)
jobdetail=[]
for x in linklist:
    getjobdetail(x,jobdetail)
db_post=db['job-offer']
for x in jobdetail:
    db_post.insert_one(
        {
            'title':x['title'],
            'logo':x['logo'],
            'company':x['company'],
            'jobgroup':x['jobgroup'],
            'dateandview':x['dateandview'],
            'position':x['position'],
            'address':x['address'],
            'location':x['location'],
            'job-detail':x['detail'],
            'company-info': x['companyinfo']
        }
    )