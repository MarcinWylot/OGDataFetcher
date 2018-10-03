from fetcher import opengraph

def extract(url):
    try:
        data = opengraph.OpenGraph(url=url,scrape=True)
        if data.is_valid():
            data['success'] = True 
        else:
            data['success'] = False
            data['url'] = url
            data['msg'] = 'No data available on on the website'
    except Exception as e:
        data = {'success': False, 'url': url, 'msg': str(e)}
        


    return data