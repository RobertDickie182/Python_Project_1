from flask import Blueprint, request, render_template, redirect
from models.city import City
from repositories import city_repository
from repositories import country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities.html", cities=cities)

@cities_blueprint.route("/cities/new", methods=["GET"])
def new_city():
    countries = country_repository.select_all()
    return render_template("/cities/new_city.html", countries=countries)

@cities_blueprint.route("/cities/<id>")
def show_city(id):
    city = city_repository.select(id)
    return render_template("cities/show_city.html", city=city)


@cities_blueprint.route("/cities", methods=["POST"])
def create():
    name = request.form["name"]
    visited = "visited" in request.form
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)
    city = City(name, visited, country)
    city_repository.save(city)
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete(id):
    city_repository.delete(id)
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit(id):
    city = city_repository.select(id)
    return render_template("/cities/edit_city.html", city=city)

@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update(id):
    city = city_repository.select(id)
    city.name = request.form["name"]
    city.visited = "visited" in request.form
    city_repository.update(city)
    return redirect(f"/cities/{id}")

    
    







