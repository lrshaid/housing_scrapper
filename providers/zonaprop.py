#import requests
from bs4 import BeautifulSoup
import logging
from providers.baseprovider import BaseProvider

class Zonaprop(BaseProvider):
    def props_in_source(self, source):
        page_link = self.provider_data['base_url'] + source
        page = 1
        processed_ids = []

        while(True):
            logging.info(f"Requesting {page_link}")
            page_response = self.request(page_link)
            
            if page_response.status_code != 200:
                break
            
            page_content = BeautifulSoup(page_response.content, 'lxml')
            properties = page_content.find('div', class_='postings-container').contents
            
            repeated = 0

            for prop in properties:
                # if data-id was already processed we exit
                dataid = prop.next_element['data-id']
                #dataid = prop.find("div",class_="PostingCardLayout-sc-i1odl-0 egwEUc")#['data-id']

                if dataid in processed_ids:
                    repeated += 1
                    if repeated == 4:
                        return
                if type(prop) is None:
                    pass
                processed_ids.append(dataid)
                title=prop.find('h3', class_="PostingDescription-sc-i1odl-11 fECErU")
                if title is None:
                    title = None
                else:
                    title = prop.find('h3', class_="PostingDescription-sc-i1odl-11 fECErU").get_text().strip()

                price_section = prop.find('div', class_='Price-sc-12dh9kl-3 geYYII')

                if price_section is not None and title is not None:
                    title = title + ' ' + price_section.get_text()
                elif price_section is not None:
                    price_section = prop.find('div', class_='Price-sc-12dh9kl-3 geYYII').get_text()
                else:
                    price_section=None
                    
                yield {
                    'title': title, 
                    'url': self.provider_data['base_url'] + prop.next.attrs['data-to-posting'],
                    'internal_id': dataid,
                    'provider': self.provider_name
                    }

            page += 1
            page_link = self.provider_data['base_url'] + source.replace(".html", f"-pagina-{page}.html")
    