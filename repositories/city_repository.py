from db.run_sql import run_sql

import pdb

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, visited, country_id) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.visited, city.country.id]
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

def select(id):
    city = None

    sql = "SELECT * FROM cities where id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = City(result['name'], result['visited'], country, result['id'])
    return city

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql = "UPDATE cities SET (name, visited, country_id) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.visited, city.country.id, city.id]
    run_sql(sql, values)

def cities_for_country(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['visited'], row['country_id'], row['id'])
        cities.append(city)
    return cities
    


