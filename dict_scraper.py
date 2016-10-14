from urllib2 import Request, urlopen, URLError

wordlist = list(open("unknown_words.txt", "r"))
words = [x.strip() for x in wordlist] # remove /n line ends

base_url = 'http://www.dictionary.com/browse/'
urls =[]

for word in words:
    urls.append(base_url+word)

def scan(someurl):                # page scanning function
    # split off the last part of url and stuff it into a variable
    keyword = someurl.split('/')[4]
    req = Request(someurl)
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            #print 'We failed to reach a server.'
            #print 'Reason: ', e.reason
            print keyword, e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        the_page = response.readlines()
        for line in the_page:
            if '<meta name="description"' in line:
#                print line
                splitline = line.split('"')
#                print splitline
                for entry in splitline:
                    if 'definition,' in entry:
                        #print entry
                        #print entry.split('definition,')
                        print keyword+":", ''.join(entry.split('definition, ')[1:])
#                        def_unknowns = open("unknown_words_defs.txt", "a")
#                        def_unknowns.write((keyword+":", ''.join(entry.split('definition, ')[1:])+"\n"))
#                        def_unknowns.close()                       
for url in urls:
    scan(url)
    print