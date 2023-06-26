from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries", methods=["GET"])
def users():
    countries = country_repository.select_all()
    return render_template("countries.html", countries = countries)

@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show(id):
    country = country_repository.select(id)
    return render_template("/countries/show.html", country=country)

@countries_blueprint.route("/countries/new", methods=["GET"])
def new_task():
    return render_template("/countries/new_country.html")

@countries_blueprint.route("/countries", methods=["POST"])
def create():
    name = request.form["name"]
    country = Country(name)
    country_repository.save(country)
    return redirect("/countries")

@countries_blueprint.route("countries/<id>/delete", methods=["POST"])
def delete(id):
    country_repository.delete(id)
    return redirect("/countries")
    


