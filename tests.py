import unittest
import fetcher
import main


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.client = main.fetcher.test_client()
        self.client.testing: bool = True

    def tearDown(self):
        pass

    @staticmethod
    def test_extract():
        data = fetcher.extract.extract(url='https://www.bbc.com/news')
        assert (data['success'])
        assert (data['title'] == 'Home - BBC News')
        assert (data['url'] == 'https://www.bbc.co.uk/news')
        assert ('description' in data)
        assert ('image' in data)

    @staticmethod
    def test_extract_network_error():
        data = fetcher.extract.extract(url='https://this.page.does.noe.exist')
        assert (data['success'] is False)

    @staticmethod
    def test_extract_network_404error():
        data = fetcher.extract.extract(url='http://www.bbc.co.uk/newsssss')
        assert (data['success'] is False)

    @staticmethod
    def test_extract_NOdata_error():
        data = fetcher.extract.extract(
            url='http://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/2.2.2/bbc_news_logo.png')
        assert (data['success'] is False)

    def test_info(self):
        rv = self.client.get('/info?url=https://www.bbc.com/news')
        assert rv.status == '200 OK'
        assert b'Title: Home - BBC News' in rv.data

    def test_info_error(self):
        rv = self.client.get('/info?url=https://this.page.does.noe.exist')
        assert b'Unable to fetch data for' in rv.data


if __name__ == '__main__':
    unittest.main(verbosity=2)
