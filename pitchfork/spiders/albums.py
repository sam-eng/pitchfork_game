import scrapy

class AlbumsSpider(scrapy.Spider):
	name = "albums"

	def start_requests(self):
		urls = [
			'https://pitchfork.com/reviews/albums/popular/?page=1',
			'https://pitchfork.com/reviews/albums/popular/?page=2',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		album_names = response.css('.review__title-album').extract()
		artists = response.css('.review__title-artist').extract()
		print(album_names)
		print(artists)
		with open(filename, 'w') as f:
			for i in album_names:
				f.write(i)
			for j in artists:
				f.write(j)