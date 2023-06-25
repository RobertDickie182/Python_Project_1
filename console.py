import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

# country_repository.delete_all()

country1 = Country("Spain")
country_repository.save(country1)
country2 = Country("Greece")
country_repository.save(country2)
country3 = Country("Italy")
country_repository.save(country3)
country4 = Country("Japan")
country_repository.save(country4)
country5 = Country("Madagascar")
country_repository.save(country5)
country6 = Country("South Africa")
country_repository.save(country6)
country7 = Country("Barbados")
country_repository.save(country7)
country8 = Country("North Korea")
country_repository.save(country8)

country_repository.select_all()

# city_repository.delete_all()

city1 = City("Madrid", True, 1)
city_repository.save(city1)
city2 = City("Athens", True, 2)
city_repository.save(city2)
city3 = City("Rome", True, 3)
city_repository.save(city3)
city4 = City("Tokyo", False, 4)
city_repository.save(city4)
city5 = City("Antananarivo", False, 5)
city_repository.save(city5)
city6 = City("Johannesburg", True, 6)
city_repository.save(city6)
city7 = City("Bridgetown", True, 7)
city_repository.save(city7)
city8 = City("Pyongyang", False, 8)
city_repository.save(city8)



pdb.set_trace()