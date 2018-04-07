import scrapy
import re

def remove_html(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

class AlbumsSpider(scrapy.Spider):
	name = "albums"

	def start_requests(self):
		urls = [
			'https://pitchfork.com/reviews/albums/popular/?page=1',
			'https://pitchfork.com/reviews/albums/popular/?page=2',
			'https://pitchfork.com/reviews/albums/popular/?page=3',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		album_file = 'album_names.txt'
		artist_file = 'artists.txt'
		album_names = response.css('.review__title-album').extract()
		artists = response.css('.review__title-artist').extract()
		with open(album_file, 'w') as al:
			for i in album_names:
				al.write(remove_html(i) + "\n")
		with open(artist_file, 'w') as art:
			for j in artists:
				art.write(remove_html(j) + "\n")
