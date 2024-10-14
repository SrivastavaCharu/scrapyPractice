import scrapy


class ActiveJobs(scrapy.Spider):
    name = 'activeJobs'
    start_urls = ['https://careers.classmethod.jp/requirements/']

    def parse(self, response):
        job_positions = response.css('ul.c-column.-S-2-XS-1.-requirements li.c-column__item div.p-requirements')
        for job in job_positions:
            position = job.css('a span::text').get()
            yield {
                'position': position
            }