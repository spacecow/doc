import urllib
import urllib2
p = urllib.urlopen('http://www.example.com')
print p.headers['server'] #--> Apache/2.2.3 (CentOS)

#curl -I http://www.example.com
#HTTP/1.0 302 Found
#Location: http://www.iana.org/domains/example/
#Server: BigIP
#Connection: Keep-Alive
#Content-Length: 0

