import scrapy

class EvkurLgtvSpider(scrapy.Spider):
    name = 'evkur_lgtv'
    allowed_domains = ['evkur.com.tr']
    start_urls = ['https://www.evkur.com.tr/televizyonlar?ajax=true&specificationValueIds=1265']

    def parse(self, response):

        tv_Name = response.css('.multiline-ellipsis::text').extract()
        tv_Price = response.xpath("//a[@class='price']/span/text()").extract()
        tv_img = response.xpath("//a[@class='image']/img/@src").extract()
        nextPage = response.css('.image').xpath('@href').getall()

        prices = []
        for cost in tv_Price:
            if "TL" not in cost:
                prices.append(cost)

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