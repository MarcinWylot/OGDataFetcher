import fetcher.opengraph


def extract(url: object) -> object:
    """Fetches data from the URL

    Parameters
    ----------
    url : str
        URL of the website we fetch data from
        
    Returns
    -------
    dictionary
        data fetched from the website
    """
    try:
        data = fetcher.opengraph.OpenGraph(url=url, scrape=True)
        if data.is_valid():
            data['success'] = True
        else:
            data['success'] = False
            data['url'] = url
            data['msg'] = 'No data available on on the website'
    except Exception as e:
        data = {'success': False, 'url': url, 'msg': str(e)}

    return data
