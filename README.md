# Open Graph Data Fetcher

Simple HTTP API endpoint that takes a URL, and returns the following metadata:
<ul>
<li>URL</li>
<li>Title</li>
<li>Description (if available)</li>
<li>Image (if available)</li>
</ul>


Data is scraped from the Open Graph tags, if there are no Open Graph tags availablethe data is retrieved from HTML meta tags (e.g., title, description).


Run the endpoint

```
python main.py 
```

Tun unitests
```
python tests.py 
```