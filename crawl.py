from bs4 import BeautifulSoup
import urllib2
import requests

mylist = []
u_in = []
def crawler(url):
	try:
		r  = requests.get(url, timeout=10)
	except requests.exceptions.RequestException as e:  # This is the correct syntax
	    print e
	    return
	data = r.text
	soup = BeautifulSoup(data)
	for link in soup.findAll('a'):#, href=True):
		if ( link.get('href') not in mylist ):
			# if('http' in link.get('href') and u_in[0] not in link.get('href')): #external link
			# 	return
			# else:
			mylist.append ( link.get ( 'href' ) )
	return 

def main():
	# user_input = raw_input("Enter a website to extract the URL's from: ")
	# user_input = "syedfaaizhussain.com"
	# user_input = "learnyouahaskell.com"
	user_input = "carameltechstudios.com" #35 some answers are 22 more than 30
	u_in.append(user_input)
	crawler("http://" + user_input)
	newlist = []
	for i in mylist:
		print i

	i=0 
	while i<len(mylist):
		url  = mylist[i]
		if (url == None):# empty link
			i=i+1
			continue
		if("http" in url):
			if("user_input" in url):#sub domain
				crawler(url)
			else: # external link
				i=i+1 
				continue
		else:  # internal link within major domain 
			if(len(url)):
				if(url[0]!='/'):
					url = '/' + url
			crawler("http://" + user_input + url)
		i=i+1
	for i in mylist:
		if ( i==None ) :
			continue
		elif ( ( ( "http" in i ) or ("www" in i) ) and ( user_input not in i ) ) :
			continue
		else:
			newlist.append(i)

	print "dekh lo"
	for i in newlist:
		print i
	print len(newlist)
if __name__ == '__main__':
    main()

   # haskell 19