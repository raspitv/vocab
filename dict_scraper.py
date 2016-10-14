from __future__ import print_function
try:
    # Python2
    from urllib2 import Request, urlopen, URLError
except ImportError:
    # Python3
    from urllib.request import Request, urlopen, URLError

wordlist = list(open("unknown_words.txt", "r"))
words = [x.strip() for x in wordlist]    # remove \n line ends

base_url = 'http://www.dictionary.com/browse/'

def lookup(keyword):                     # word lookup function
    # build url to lookup
    someurl = base_url + keyword
    req = Request(someurl)               # grab web page
    try:
        grab_page = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print(keyword, e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        web_page = grab_page.readlines()               # read web page lines
        for line in web_page:
            line = line.decode('utf-8')
            if '<meta name="description"' in line:     # find required line
                splitline = line.split('"')
                for entry in splitline:                # extract bits we want
                    if 'definition,' in entry:
                        write_line = keyword+": "+''.join(entry.split('definition, ')[1:])
                        print(write_line)
                        write_line +="\n"           
                        def_unknowns = open("unknown_words_defs.txt", "a")
                        def_unknowns.write(write_line) # write word + def'n to file
                        def_unknowns.close()                       
for word in words:
    lookup(word)
    print()
