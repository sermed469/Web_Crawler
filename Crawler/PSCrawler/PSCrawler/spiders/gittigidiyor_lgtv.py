import scrapy

class GittigidiyorLgtvSpider(scrapy.Spider):
    name = 'gittigidiyor_lgtv'
    allowed_domains = ['gittigidiyor.com']
    start_urls = ['https://www.gittigidiyor.com/lg-televizyon',
    'https://www.gittigidiyor.com/lg-televizyon?sf=2',
    'https://www.gittigidiyor.com/lg-televizyon?sf=3',
    'https://www.gittigidiyor.com/lg-televizyon?sf=4']

    def parse(self, response):
        
        tv_Name = response.xpath("//div[@class='gg-w-24 gg-d-24 gg-t-24 gg-m-24 product-title-info']//span/text()").extract()
        tv_Price = response.xpath("//div[@class='gg-w-24 gg-d-24 gg-t-24 gg-m-24 padding-none product-price-info']//div[@class='gg-w-24 gg-d-24 gg-t-24 gg-m-24 padding-none srp-product-catalog-ab-variant']/div[@class='priceListener gg-w-24 gg-d-24 gg-t-24 gg-m-24 padding-none']/div/p[@class='fiyat price-txt robotobold price']/text()").extract()
        tv_img = response.xpath("//div[@class='cell-border-css']/p/img/@data-original").extract()                          
        nextPage = response.xpath("//div[@class='clearfix']/ul[@class='catalog-view clearfix products-container']//a/@href").extract()

        for p in tv_Price:
            if len(p) == 17:
                tv_Price.remove(p)

        page_list = []
        for page in nextPage:
            page_list.append( '/' + page.split('/')[3] + '/' + page.split('/')[4])

        rowData = zip(tv_Name,tv_Price,tv_img,page_list)
       
        for item in rowData:
            scraped_info = {
                    'page':response.url,
                    'tv_Name':item[0].strip(),
                    'tv_Price':item[1].strip(),
                    'tv_img':item[2].strip(),
                    'nextPage':item[3].strip(),
            }

            yield scraped_info
