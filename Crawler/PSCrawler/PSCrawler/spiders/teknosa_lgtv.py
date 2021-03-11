import scrapy

class TeknosaLgtvSpider(scrapy.Spider):
    name = 'teknosa_lgtv'
    allowed_domains = ['www.teknosa.com']
    start_urls = ['https://www.teknosa.com/lg-televizyonlar-bc-101001',
                'https://www.teknosa.com/televizyonlar-c-101001?q=%3Arelevance%3Abrand%3A2331&page=1']

    def parse(self, response):
        
        tv_Name = response.xpath("//div[@class='product-name']/a/span/text()").extract()
        tv_Price = response.xpath("//div[@class='product__listing product__grid category-product-list grid-view']/input/@value").extract()
        tv_img = response.xpath("//div[@class='product-image-item']/a/img/@src").extract()
        nextPage = response.xpath("//div[@class='product-image-item']/a/@href").extract()
        
        prices = []
        for cost in tv_Price:
            t = cost.replace(' TL','')
            prices.append(t)
        
        rowData = zip(tv_Name,prices,tv_img,nextPage)
        for item in rowData:
            scraped_info = {
                    'page':response.url,
                    'tv_Name':item[0].strip(),
                    'tv_Price':item[1].strip(),
                    'tv_img':item[2].strip(),
                    'nextPage':item[3].strip(),
            }

            yield scraped_info