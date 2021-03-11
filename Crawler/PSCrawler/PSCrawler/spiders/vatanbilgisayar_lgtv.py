import scrapy

class VatanbilgisayarLgtvSpider(scrapy.Spider):
    name = 'vatanbilgisayar_lgtv'
    allowed_domains = ['vatanbilgisayar.com']
    start_urls = ['https://www.vatanbilgisayar.com/arama/televizyon/lg/televizyon/?page=1',
    'https://www.vatanbilgisayar.com/arama/televizyon/lg/televizyon/?page=2',
    'https://www.vatanbilgisayar.com/arama/televizyon/lg/televizyon/?page=3',
    'https://www.vatanbilgisayar.com/arama/televizyon/lg/televizyon/?page=4',
    'https://www.vatanbilgisayar.com/arama/televizyon/lg/televizyon/?page=5']

    def parse(self, response):

        tv_Name =  response.xpath("//a[@class='product-list__link']/div[@class='product-list__product-name']/text()").extract()
        tv_Price = response.xpath("//div[@class='product-list product-list--list-page']/div[@class='product-list__content']/div[@class='product-list__cost']/span[@class='product-list__price']/text()").extract()
        tv_img = response.xpath("//div[@class='slider-img']/img[@class='lazyimg']/@data-src").extract()
        nextPage = response.css('.product-list__link').xpath('@href').getall()
      
        rowData = zip(tv_Name,tv_Price,tv_img,nextPage)
   
        for item in rowData:
            scraped_info = {
                    'page':response.url,
                    'tv_Name':item[0].strip(),
                    'tv_Price':item[1].strip(),
                    'tv_img':item[2].strip(),
                    'nextPage':item[3].strip(),
            }

            yield scraped_info