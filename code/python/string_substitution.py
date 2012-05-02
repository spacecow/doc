s = "some bold"
print "<b>%s</b> text" % s
#--> <b>some bold</b> text
s2 = "some italic"
print "<b>%s</b> and <i>%s</i> text" % (s,s2)
#--> <b>some bold</b> and <i>some italic</i> text
print "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s." % {'name':'Mike','nickname':'Goose'}
#--> I'm Goose. My real name is Mike, but my friends call me Goose.
