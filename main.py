import flask
from fetcher import extract, render

fetcher = flask.Flask('ogdatafetcher')


@fetcher.route("/info")
def info():
    url = flask.request.args.get('url')
    data: dict = extract.extract(url=url)
    rendered = render.render(data)

    return rendered


if __name__ == '__main__':
    fetcher.run(host='localhost', port=8000, debug=True)
