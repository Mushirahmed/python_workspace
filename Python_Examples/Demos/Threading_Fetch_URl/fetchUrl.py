import threading
import urllib2
class FetchUrls(threading.Thread):
    """
    Thread checking URLS
    """
    def __init__(self,urls,output):
        """
        Contructor
        @param urls list of urls to check
        @param output file to write urls output
        """
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output  
    
    def run(self):
        """ 
        Thread run method. Check URLs one by one.
        """
        while self.urls:
            url = self.urls.pop()
            req = urllib2.Request(url)
            try:
                d = urllib2.Request(url)
            except urllib2.URLError,e:
                print 'URL %s failed: %s' %(url,e.reason)
            self.output.write(d.read())
            print 'write done by %s'%self.name
            print 'URL %s fetched by %s' %(url,self.name)
        
    
    
    