#Current plan is to map the features to a dictioanary and then convert it to a csv file.
# Feauture extraction 
class feature_extractor(object):
    def __init__(self,url):
        self.url=url
        self.length=len(url)
        #self.domain=url.split('//')[-1].split('/')[0]
    #def entropy(self):
    
    def num_digits(self):
        return sum(n.isdigit() for n in self.url)
    
    def num_char(self):
        return sum(n.alpha() for n in self.url)
    
    def has_http(self):
        if "http" in self.url:
            return 1
        else:
            return 0
    
    def has_https(self):
        if "https" in self.url:
            return 1
        else:
            return 0
    
    #def num_special_char(self):
    #
    
    #def num



def clean(input):
    tokensBySlash = str(input.encode('utf-8')).split('/')
    allTokens=[]
    for i in tokensBySlash:
        tokens = str(i).split('-')
        tokensByDot = []
        for j in range(0,len(tokens)):
            tempTokens = str(tokens[j]).split('.')
            tokentsByDot = tokensByDot + tempTokens
        allTokens = allTokens + tokens + tokensByDot
    allTokens = list(set(allTokens))
    if 'com' in allTokens:
        allTokens.remove('com')
    return allTokens
    