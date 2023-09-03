import scrapy
from Doctor.items import DoctorProfileItem
from scrapy.loader import ItemLoader

class DoctorpiderSpider(scrapy.Spider):
    name = "doctorspider"
    allowed_domains = ["dzdoc.com"]
    specialties=['98','57','2','3','4','5','68','8','9','89','69','10','11','65','12','80','81','13','90','14','15','16','17','93','96','94','95','97','54','104','70','19','20','21','22','58','23','56','83','72','92','7','24','25','1','26','27','28','29','103','91','33','34','30','100','101','31','73','35','36','53','99','85','74','75','67','52','51','38','76','55','39','77','40','41','43','44','87','42','45','46','48','47','49','50',]

    def  start_requests(self):
       for state in  range(1,48):
            for  specialty in  self.specialties:
                start_urls = f'https://dzdoc.com/recherche.php?specialite={specialty}&region={state}&p=1'
                yield  scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        base_url='https://dzdoc.com/'

        doctor_items=response.css('.list-group-item')
        for doctor_item in  doctor_items:
            doctor_ralative_url=doctor_item.css('.col-md-8 a ::attr(href)').get()
            doctor_url=base_url + doctor_ralative_url
            yield response.follow(doctor_url,callback=self.doctor_profile_parse)
            pass

        next_page=response.css('.next  a::attr(href)').get() 
        if next_page is not None:  
            next_page_url=base_url+next_page
            yield response.follow(next_page_url,callback=self.parse)

    def doctor_profile_parse(self,response):
        
        doctor_item =DoctorProfileItem()
        doctor_item['name']=response.css('.doctor-name ::text').get().strip()
        doctor_item['address']=response.css('#adresse ::text').get().strip()
        doctor_item['specialty']=response.css('.no-margin ::text').get().strip()
        doctor_item['working_hours']=response.css('.col-md-12 .text-justify ::text').getall()
        doctor_item['contact']=response.css('.col-md-12 .unstyled li a ::text').getall()
        yield doctor_item