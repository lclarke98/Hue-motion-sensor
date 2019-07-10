import datetime
from astral import Astral

city_name = 'London'

a = Astral()
a.solar_depression = 'civil'

city = a[city_name]

print('Information for %s/%s\n' % (city_name, city.region))


timezone = city.timezone
print('Timezone: %s' % timezone)

print('Latitude: %.02f; Longitude: %.02f\n' % \
    (city.latitude, city.longitude))
Latitude: 51.60; Longitude: 0.08

sun = city.sun(date=datetime.date(2019, 7, 9), local=True)
print('Dawn:    %s' % str(sun['dawn']))
print('Sunrise: %s' % str(sun['sunrise']))
print('Noon:    %s' % str(sun['noon']))
print('Sunset:  %s' % str(sun['sunset']))
print('Dusk:    %s' % str(sun['dusk']))