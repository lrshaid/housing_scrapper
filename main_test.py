from providers.mercadolibre import Mercadolibre
from providers.baseprovider import BaseProvider

provider_name = 'mercadolibre'
provider_data = {'base_url':'https://inmuebles.mercadolibre.com.ar','sources':['/departamentos/departamento-3-ambientes']}

provider=Mercadolibre(provider_name, provider_data)#.props_in_source(provider_data)

properties =[]
print(provider)

for prop in provider.next_prop():
 
    properties.append(prop)

properties
#"Mercadolibre","https://inmuebles.mercadolibre.com.ar/departamentos/departamento-3-ambientes"