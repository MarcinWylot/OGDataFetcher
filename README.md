# Open Graph Data Fetcher

Simple HTTP API endpoint that takes a URL, and returns the following metadata:
Canonical URL
Title
Description (if available)
Image (if available)

Data is scraped from the Open Graph tags, if there are no Open Graph tags availablethe data is retrieved from HTML meta tags (e.g., title, odescription tags).


Run the endpoint

```
python main.py 
```

run unitests
```
python tests.py 
```