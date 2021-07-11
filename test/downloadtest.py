from urllib import request

def download(url,fname):    
    request.urlretrieve(url, fname)
