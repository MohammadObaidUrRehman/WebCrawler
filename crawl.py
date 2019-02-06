from bs4 import BeautifulSoup
import urllib2
import requests

mylist = []
user_input = ""
counter = 0
global_user_input = []
def crawler(url):
	try:
		r  = requests.get(url, timeout=10)
	except requests.exceptions.RequestException as e:  # This is the correct syntax
	    print e
	    print "error opening url"
	    return
	data = r.text
	soup = BeautifulSoup(data)
	# print soup
	for link in soup.findAll('a'):#, href=True):

		thelink=link.get('href')
		temp = ""
		if (thelink==None):
			continue
		if("#" in thelink):
			sep = "#"
			temp = thelink.split(sep,1)[0]
			if ( temp not in mylist ):
				mylist.append ( temp )
		elif ( thelink not in mylist ):
				mylist.append ( thelink )
	return 

def save(name):
	# print name
	global counter
	# print global_user_input[0]
	opener = ""
	if("http" in name):
		# print "in if"
		# opener = global_user_input[0] + name
		opener = name 
	else:
		# print "in else"
		opener = "http://" + global_user_input[0] + "/" + name
	# response = urllib2.urlopen(opener)
	# y=str(counter)
	print "saving ", opener
	# print "name", opener

	try:
		response = urllib2.urlopen(opener)
	except urllib2.URLError as e:
		response = e
		print "error opening url"
		return

	counter=counter + 1
	f = open('link'+str(counter)+'.html', 'w')
	webContent = response.read()
	f.write(webContent)
	f.close 
	return
# http.request.method =="GET
# http.response.code == 200" 
# learnyouahaskell.com
def main():

	# user_input = raw_input("Enter a website to extract the URL's from: ")
	# user_input = "syedfaaizhussain.com"     #15,16 getting that answer
	# user_input = "learnyouahaskell.com"   #21-2 getting that answer
	user_input = "carameltechstudios.com" #35 some answers are 22 more than 30
	# user_input = "forum.carameltechstudios.com"
	# save("syedfaaizhussain.com")
	global_user_input.append(user_input)
	print "Initiating Crawling"
	crawler("http://" + user_input)
	newlist = []
	i=0 
	while i<len(mylist):
		url  = mylist[i]
		if (url == None):# empty link
			i=i+1
			continue
		if("http" in url):
			if(user_input in url):#sub domain
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
		elif ( ("@" in i) or ( ( "http" in i ) or ("www" in i) ) and ( user_input not in i ) ) :
			continue
		else:
			newlist.append(i)

	for i in newlist:
		print i
	print "Crawling Completed"
	print "The list of websites is"
	print len(newlist)
	print "Starting Saving\n"
	
	for i in newlist:
		save(i)
	print "Saving Completed"
if __name__ == '__main__':
    main()