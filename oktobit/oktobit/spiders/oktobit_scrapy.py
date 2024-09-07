import scrapy

class LaptopSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['oktobit.store']
    start_urls = ['https://oktobit.store/product-category/laptops/']

    def parse(self, response):
        pcs = response.css('div.col-inner')
        
        # Loop through each product in the listing
        for pc in pcs:
            name = pc.css('p a::text').get()
            price = pc.css('span.woocommerce-Price-amount.amount bdi::text').get()
            category = pc.css('div.title-wrapper p.category::text').get().strip() if pc.css('div.title-wrapper p.category::text').get() else None
            url = pc.css('p a').attrib['href']

            # Go to product details page to get more information like RAM, stockage, etc.
            yield response.follow(url, callback=self.parse_product, meta={'name': name, 'price': price, 'category': category})

        # Follow pagination if there's a next page
        next_page = response.css('li a.next.page-number::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        # Get the passed metadata from the product listing
        name = response.meta.get('name')
        price = response.meta.get('price')
        category = response.meta.get('category')

        # Extract additional details from the product details page
        ram = response.xpath('//li[contains(text(), "RAM")]/text()').get()
        stockage = response.xpath('//li[contains(text(), "Stockage")]/text()').get()
        os = response.xpath('//li[contains(text(), "Windows")]/text()').get()
        batterie = response.xpath('//li[contains(text(), "Batterie")]/text()').get()
        poids = response.xpath('//li[contains(text(), "Poids")]/text()').get()

        # Yield all the collected data
        yield {
            'name': name,
            'price': price.strip() if price else None,
            'category': category,
            'RAM': ram.strip() if ram else None,
            'Stockage': stockage.strip() if stockage else None,
            'OS': os.strip() if os else None,
            'Batterie': batterie.strip() if batterie else None,
            'Poids': poids.strip() if poids else None,
            'url': response.url,
        }
