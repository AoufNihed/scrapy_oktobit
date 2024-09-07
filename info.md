 laptops = response.css('div.col-inner')

more_deatils_link= responce.css(' p a').attrib['href']

name_pc = response.css('p a::text').get() 

price = response.css('span.woocommerce-Price-amount.amount bdi::text').get() **have to clean after ***

cateegory= responce.css('div.title-wrapper p::text').get() **have to clean after ***

url_of_pc_details = responce.css('p a').attrib['href']

link_next_page=response.css('li a.next.page-number::attr(href)').get()


category_check=responce.css('p.category.uppercase.is-smaller.no-text-overflow.product-cat op-7')


-----------------------------------------------------------------------------------------------------------------------------
scraping more details :

RAM :

OS:

Stocakage:

Batterie:

Etat :

poids:

