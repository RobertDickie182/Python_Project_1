from db.run_sql import run_sql

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, visited, country_id) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.visited, city.country_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], row['visited'], country, row['id'])
        cities.append(city)
        return cities

    

