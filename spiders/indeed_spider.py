import scrapy


# you may need to log into indeed.com for this to work
class IndeedSpider(scrapy.Spider):
    # identity
    # Instantiate Spider
    name = 'indeed'

    # requests
    def start_requests(self):
        urls = [
            'https://www.indeed.com/jobs?as_and=Data+Scientist&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&sr=directhire&as_src=&salary=&radius=25&l=New+York%2C+New+York&fromage=last&limit=50&sort=&psf=advsrch'
            ]
        for url in urls:
            yield scrapy.Requests(url=url, callback=self.parse)

    # response
    with open("Today's Data Science Positions In NYC", 'wb') as f:
        f.write(response.body)
