#!/usr/bin/python
import cgi

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>-  CGI Python Program</title>'
print '</head>'
print '<body>'
print '<h2> CGI program </h2>'
print '</body>'


print '<h2> New Internet Connection </h2>' + '<br'

print '</html>'

print "Content-type:text/html\r\n\r\n" + '<br>'
message = form.getvalue("message", "(no message)")
print '<br>'

print "Name1 is: "    +" %s" % form.getvalue('name1') + '<br>'
print"Name2 is: "   + "%s" % form.getvalue('name2') + '<br>'
print "Name3 is: " + "%s" % form.getvalue('name3') + '<br>'
print"Name4 is: " + "%s" % form.getvalue('name4')  + '<br>'
