import scrapy
import re

#removes html tags from scraped text by using regular expressions
def remove_html(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

class AlbumsSpider(scrapy.Spider):
	name = "albums"
	open('album_names.txt', 'w').close()
	open('artists.txt', 'w').close()

	def start_requests(self):
		#list of first five pages (first 60 albums) of most popular pitchfork album reviews
		urls = [
			'https://pitchfork.com/reviews/albums/popular/?page=1',
			'https://pitchfork.com/reviews/albums/popular/?page=2',
			'https://pitchfork.com/reviews/albums/popular/?page=3',
			'https://pitchfork.com/reviews/albums/popular/?page=4',
			'https://pitchfork.com/reviews/albums/popular/?page=5', 
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse_albums)

	def parse_albums(self, response):
		album_file = 'album_names.txt'
		artist_file = 'artists.txt'
		#image_file = 'covers.txt' 
		album_names = response.css('.review__title-album').extract()
		artists = response.css('.review__title-artist').extract()
		with open(album_file, 'a') as al:
			for i in album_names:
				al.write(remove_html(i) + "\n")
		with open(artist_file, 'a') as art:
			for j in artists:
				art.write(remove_html(j) + "\n")
