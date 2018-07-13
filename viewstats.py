import sqlite3
import datetime

urls = []

def convTstamp(ts):
    i_ts = int(ts)
    dt = datetime.datetime.fromtimestamp(i_ts/1000)
    s_dt = str(dt)
    return s_dt[0:10]

def urlAdd(url):
    urls.append(url)
    return url

def urlCount(url):
    furl = urls.count(url)
    return furl
conn = sqlite3.connect('webstats.db')
print ("Opened database successfully")

#June 2016 = 1464739200

'''
'probation','publicsafety',
'mentalhealth','parks','homes',
'humanrights','finance', 'veterans', 'women',
'correction', 'citizenparticipation', 'environment',
'emergencyservices','humanresources', 'doit',
'labs', 'publicworks',
'planning', 'socialservices',
'tourism', 'airport', 'africanamerican', 'archives',
'bps', 'hispanic', 'lgbt', 'tlc', 
'westchesterda.net',
'www.westchesterda.net',
'westchesterlegislators.com',
'www.westchesterlegislators.com',
'www.westchesterclerk.com',
'westchesterclerk.com',
'homes.westchestergov.com/resources/housing-settlement',
'homes.westchestergov.com/homeseeker-housing',
'homes.westchestergov.com/homeownership/homeseeker-opportunities/housing-opportunities-sign-up',
'homes.westchestergov.com/homeseeker-housing/formulario-de-interes',
'homes.westchestergov.com/homeseeker-housing/buscador-de-hogar',
'homes.westchestergov.com/heritage-homes',
'homes.westchestergov.com/grant-park',
'homes.westchestergov.com/the-mews-ii',
'homes.westchestergov.com/park-terrace',
'homes.westchestergov.com/waterwheel-condos',
'homes.westchestergov.com/5-minerva-place',
'homes.westchestergov.com/437-south-10th-ave',
'homes.westchestergov.com/washington-ave-condos',
'homes.westchestergov.com/bridleside-apts',
'homes.westchestergov.com/round-top',
'homes.westchestergov.com/37-wildwood',
'homes.westchestergov.com/art-lofts',
'homes.westchestergov.com/21-cooley-street-pleasantville-ny',
'homes.westchestergov.com/the-ambassador',
'homes.westchestergov.com/100-cedar-st',
'homes.westchestergov.com/72-croton-ave',
'homes.westchestergov.com/developers/210-fair-and-affordable/2643-underhill-apartments-yorktown-ny',
'homes.westchestergov.com/oregon-ave-1',
'homes.westchestergov.com/oregon-ave-2',
'homes.westchestergov.com/208-harris-rd-1',
'homes.westchestergov.com/208-harris-rd-2',
'homes.westchestergov.com/25-oak-rd',
'homes.westchestergov.com/11-westview-ave',
'homes.westchestergov.com/8-beech-street-white-plains',
'homes.westchestergov.com/freedom-gardens-for-handicapped',
'homes.westchestergov.com/component/content/article/210-fair-and-affordable/2687-491-franklin-street-ryebrook',
'homes.westchestergov.com/240-halstead-avenue-harrison',
'homes.westchestergov.com/289-manville-road-pleasantville',
'homes.westchestergov.com/developers/210-fair-and-affordable/2685-2-spruce-rd-lewisboro',
'homes.westchestergov.com/17-broadway-harrison',
'homes.westchestergov.com/70-west-street-harrison',
'homes.westchestergov.com/106-lake-kitchawan-drive-lewisboro',
'homes.westchestergov.com/component/content/article/210-fair-and-affordable/2692-armonk-commons',
'homes.westchestergov.com/22-old-route-22-armonk-ny',
'homes.westchestergov.com/homeownership/210-fair-and-affordable/2649-crompond-crossing-yorktown-ny',
'humanrights.westchestergov.com/file-a-complaint/your-rights',
'humanrights.westchestergov.com/file-a-complaint/filing-a-complaint',
'humanrights.westchestergov.com/human-rights-law',
'humanrights.westchestergov.com/file-a-complaint/fair-housing',
'humanrights.westchestergov.com/news-and-events/events-education-and-outreach'
'''
#June TimeStamp 1464739200
#July TimeStamp 1467346925
#August TimeStamp 1470013200
#September TimeStamp 1472688000
#October TimeStamp 1475347188
#November TimeStamp 1478008654
#Dec TimeStamp 1480619604
#Dec 1st 2016 1480600654
#Dec 2016 -- 1480550400
#Jan 1st 1483279054
#Jan 25th 2017 1485352654
str_base = "SELECT id, PAGEURL, CLIENTIP, DATE  from RAWSTATS WHERE DATE >= 1483279054 AND PAGEURL LIKE 'http://"
str_depts = ['','www.westchesterputnamonestop.com','humanresources','health', 'seniorcitizens', 'business','www3','consumer','youth','www.jobswaiting.com',
'www3.westchestergov.com/fatherhood-initiative',
'www.westchesterda.net/crime-prevention/rights-of-crime-victims',
'seniorcitizens.westchestergov.com/medicare',
'seniorcitizens.westchestergov.com/caregiving/ny-connects-long-term-care',
'socialservices.westchestergov.com/medical-assistance/medical-and-home-care-services',
'seniorcitizens.westchestergov.com/money-and-legal/info-centers',
'seniorcitizens.westchestergov.com/money-and-legal/social-security',
'seniorcitizens.westchestergov.com/money-and-legal/medicare',
'seniorcitizens.westchestergov.com/housing',
'seniorcitizens.westchestergov.com/senior-programs-and-services/publications',
'health.westchestergov.com/forms-and-permits',
'health.westchestergov.com/contact',
'health.westchestergov.com/services/locations',
'health.westchestergov.com/septic-systems',
'health.westchestergov.com/bisphenol-a-bpa',
'health.westchestergov.com/eip-early-intervention-program',
'health.westchestergov.com/petroleum-bulk-storage',
'health.westchestergov.com/sanitation',
'health.westchestergov.com/nutrition/transfat-',
'health.westchestergov.com/services'
]
str_end = "%'"
cnt = 0
tmp_urls = 0
for x in str_depts:
    str_final = str_base + str_depts[cnt] + str_end
    #print (str_final)

    cursor = conn.execute( str_final )
    for row in cursor:
       #print ("ID = ", row[0])
       #print ("PAGEURL = ", urlAdd(row[1]))
       #print ("CLIENTIP = ", row[2])
       #print ("DATE = ", convTstamp(row[3]), "\n")
       urlAdd(row[1])
       tmp_urls += 1

    #count times per month a page gets hit
    #print (urls[0], "was visited:", urlCount(urls[0]), "times")
    #print (urls[1], "was visited:", urlCount(urls[1]), "times")
    #print (urls[2], "was visited:", urlCount(urls[2]), "times")
    #print (urls[3], "was visited:", urlCount(urls[3]), "times")
    #print (urls[4], "was visited:", urlCount(urls[4]), "times")
    #print (urls[5], "was visited:", urlCount(urls[5]), "times")
    #print (urls[6], "was visited:", urlCount(urls[6]), "times")
    #print (urls[7], "was visited:", urlCount(urls[7]), "times")
    #print (urls[8], "was visited:", urlCount(urls[8]), "times")
    #print (urls[9], "was visited:", urlCount(urls[9]), "times")
    #print (urls[10], "was visited:", urlCount(urls[10]), "times")
    #print (urls[11], "was visited:", urlCount(urls[11]), "times")
    #print (urls[12], "was visited:", urlCount(urls[12]), "times")
    #print (urls[13], "was visited:", urlCount(urls[13]), "times")
    #for x in urls:
    #   print (x)
    print (str_depts[cnt],":", tmp_urls,"\n")
    cnt+=1
    tmp_urls = 0
    #print ("Total:",len(urls)*.25+len(urls))
    
print ("Database closed succesfully")
conn.close()