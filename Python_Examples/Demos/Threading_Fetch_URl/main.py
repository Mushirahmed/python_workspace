from fetchUrl import *
def main():
        #list 1 of urls to fetch
        urls1 = ['http://www.google.com','http://facebook.com']
        #list 2 of urls to fetch
        urls2 = ['http://www.yahoo.com','http://www.youtube.com']
        f = open('output.txt','w+')
        t1 = FetchUrls(urls1,f)
        t2 = FetchUrls(urls2,f)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        f.close()
if __name__ == '__main__':
    main()
        
  
            