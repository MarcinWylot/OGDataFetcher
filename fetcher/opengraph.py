# based on https://github.com/erikriver/opengraph
# with small changes

import re
import urllib.request
import bs4


class OpenGraph(dict):
    """
    """

    required_attrs = ['title', 'url']
    expected_attrs = required_attrs + ['image', 'description']

    def __init__(self, url=None, html=None, scrape=False, **kwargs):
        # If scrape == True, then will try to fetch missing attributes
        # from the page's body

        self.scrape = scrape
        self._url = url

        for k in kwargs.keys():
            self[k] = kwargs[k]

        dict.__init__(self)

        if url is not None:
            self.fetch(url)

        if html is not None:
            self.parser(html)

    def __setattr__(self, name, val):
        self[name] = val

    def __getattr__(self, name):
        return self[name]

    def fetch(self, url):
        """
        """
        raw = urllib.request.urlopen(url)
        html = raw.read()
        return self.parser(html)

    def parser(self, html):
        """
        """
        if not isinstance(html, bs4.BeautifulSoup):
            doc = bs4.BeautifulSoup(html, "html5lib")
        else:
            doc = html
        ogs = doc.html.head.findAll(property=re.compile(r'^og'))
        for og in ogs:
            if og.has_attr(u'content'):
                self[og[u'property'][3:]] = og[u'content']
        # Couldn't fetch all attrs from og tags, try scraping body
        if not self.is_valid() and self.scrape:
            for attr in self.expected_attrs:
                if not self.valid_attr(attr):
                    try:
                        self[attr] = getattr(self, 'scrape_%s' % attr)(doc)
                    except AttributeError:
                        pass

    def valid_attr(self, attr):
        return self.get(attr) and len(self[attr]) > 0

    def is_valid(self):
        return all([self.valid_attr(attr) for attr in self.required_attrs])

    def to_html(self):
        if not self.is_valid():
            return u"<meta property=\"og:error\" content=\"og metadata is not valid\" />"

        meta = u""
        for key, value in self.iteritems():
            meta += u"\n<meta property=\"og:%s\" content=\"%s\" />" % (key, value)
        meta += u"\n"

        return meta

    def to_json(self) -> object:
        pass

    def to_xml(self):
        pass

    @staticmethod
    def scrape_image(doc: object) -> object:
        images = [dict(img.attrs)['src']
                  for img in doc.html.body.findAll('img')]

        if images:
            return images[0]

        return u''

    @staticmethod
    def scrape_title(doc: object) -> object:
        return doc.html.head.title.text

    @staticmethod
    def scrape_type(doc):
        return 'other'

    def scrape_url(self, doc):
        return self._url

    @staticmethod
    def scrape_description(doc):
        tag = doc.html.head.findAll('meta', attrs={"name": "description"})
        result = "".join([t['content'] for t in tag])
        return result
