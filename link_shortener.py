import pyshorteners


def shorten_link(link):
    urls = link
    s = pyshorteners.Shortener()
    tinyurl = s.tinyurl.short(urls)
    dagd = s.dagd.short(urls)
    osdb = s.osdb.short(urls)
    
    short_url = {'tinyurl': tinyurl, 'dagd': dagd, 'osdb': osdb}

    return short_url
