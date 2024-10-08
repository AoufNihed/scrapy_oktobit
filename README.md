# Web Scraping Oktobit Store with Python (Scrapy)

## Project Overview
This project involves scraping product data from the Oktobit e-commerce store using the Python Scrapy framework. The collected data includes key product attributes such as name, price, category, RAM, operating system, battery life, and weight.

## Project Structure
```bash
|-- oktobit_scraper/
    |-- spiders/
        |-- oktobit_spider.py  # Main spider to scrape product data
    |-- items.py              # Define data fields for the scraped products
    |-- pipelines.py          # Manage how scraped data is processed
    |-- settings.py           # Scrapy settings such as request delays, user agents
    |-- output/
        |-- laptops.csv       # Exported CSV file with scraped product data

git clone git@github.com:AoufNihed/scrapy_oktobit.git
cd oktobit-scraper
pip install scrapy pandas psycopg2-binary
