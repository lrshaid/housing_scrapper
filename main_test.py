from providers.mercadolibre import Mercadolibre
from providers.baseprovider import BaseProvider
from providers.processor import process_properties
import yaml
#provider_name = 'mercadolibre'
#provider_data = {'base_url':'https://inmuebles.mercadolibre.com.ar','sources':['/departamentos/departamento-3-ambientes']}

with open("configuration.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

for provider_name, provider_data in cfg['providers'].items():

    #provider=Mercadolibre(provider_name, provider_data)#.props_in_source(provider_data)
    process_properties(provider_name,provider_data)



#for prop in provider.next_prop():
# 
#    properties.append(prop)
#
#print(properties)
#"Mercadolibre","https://inmuebles.mercadolibre.com.ar/departamentos/departamento-3-ambientes"