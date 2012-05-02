import cgi
print cgi.escape('"<b&ld>"',quote=True) 
#--> &quot;&lt;b&amp;ld&gt;&quot;
