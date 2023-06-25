from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def users():
    countries = country_repository.select_all() # NEW
    return render_template("countries.html", countries = countries)

@countries_blueprint.route("/countries/<id>")
def show(id):
    country = country_repository.select(id)
    cities = city_repository.cities_for_country(country)
    return render_template("countries/show.html", country=country, cities=cities)
