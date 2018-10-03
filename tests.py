import unittest
import flask
from fetcher import extract, render
from main import fetcher

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.client = fetcher.test_client()
        self.client.testing = True

    def tearDown(self):
        pass
           
    def test_extract(self):
        data = extract.extract(url='https://www.bbc.com/news')
        assert (data['success'])
        assert (data['title'] == 'Home - BBC News')
        assert (data['url'] == 'https://www.bbc.co.uk/news')
        assert ('description' in data)
        assert ('image' in data)
        
    def test_extract_network_error(self):
        data = extract.extract(url='https://this.page.does.noe.exist')
        assert (data['success'] == False)
        
    def test_extract_network_404error(self):
        data = extract.extract(url='http://www.bbc.co.uk/newsssss')
        assert (data['success'] == False)    
        
    def test_extract_NOdata_error(self):
        data = extract.extract(url='http://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/2.2.2/bbc_news_logo.png')
        assert (data['success'] == False)   
    
    def test_info(self):
        rv = self.client.get('/info?url=https://www.bbc.com/news')
        assert rv.status == '200 OK'
        assert b'Title: Home - BBC News' in rv.data

    def test_info_error(self):
        rv = self.client.get('/info?url=https://this.page.does.noe.exist')
        assert b'Unable to fetch data for' in rv.data
        
if __name__ == '__main__':
    unittest.main(verbosity = 2)