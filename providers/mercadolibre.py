from bs4 import BeautifulSoup
import logging
import re
from providers.baseprovider import BaseProvider

class Mercadolibre(BaseProvider):
    def props_in_source(self, source):
        page_link =self.provider_data['base_url'] + source + '_NoIndex_True'+self.provider_data['filtros_meli']
        from_ = 1
        regex = r"(MLA-\d*)"

        
        while(True):
            logging.info(f"Requesting {page_link}")
            page_response = self.request(page_link)

            if page_response.status_code != 200:
                break
            
            page_content = BeautifulSoup(page_response.content, 'lxml')
            properties = page_content.find_all('li', class_='ui-search-layout__item')

            if len(properties) == 0:
                break
            if properties[0] is None:

                page_content = BeautifulSoup(page_response.content, 'lxml')
                properties = page_content.find_all('li', class_='ui-search-layout__item')
                
                if properties[0] is not None:
                    pass
                else:
                    retry_count = retry_count+1
                
                if retry_count == 5:
                    break

            for prop in properties:
                if prop is None:
                    pass
                info = prop.find('div',class_='ui-search-result__content-wrapper')
                section = info.find('div', class_ ="ui-search-item__group__element ui-search-item__title-grid")
                href = section.next.attrs['href']
                matches = re.search(regex, href)
                internal_id = matches.group(1).replace('-', '')
                price_section = info.find('div', class_='ui-search-item__group__element ui-search-item__group--price-grid').getText().strip().replace(".","")
                title_section = section.getText()
                title = section.text#.find('span').get_text().strip() + \   ': ' + title_section.find('h2').get_text().strip()
                if price_section is not None:
                    title = title + ' ' + price_section.strip()
        
                yield {
                    'title': title_section, 
                    'url': href,
                    'internal_id': internal_id,
                    'provider': self.provider_name
                    }

            from_ += 50
            page_link = self.provider_data['base_url'] + source + f"_Desde_{from_}_NoIndex_True"+self.provider_data['filtros_meli']
    