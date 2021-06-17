import pyshorteners


def get_url(link):
    urls = link
    s = pyshorteners.Shortener()
    tinyurl = s.tinyurl.short(urls)
    dagd = s.dagd.short(urls)
    osdb = s.osdb.short(urls)

    a = pyshorteners.Shortener(api_key="f8d435c7a95e278285c32d1f7e4f92a4", user_id="25486205", domain="q.gs")
    adfly = a.adfly.short(urls)
    
    short_url = {'tinyurl': tinyurl, 'dagd': dagd, 'osdb': osdb, 'adfly': adfly}

    return short_url