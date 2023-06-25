from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def users():
    countries = country_repository.select_all() # NEW
    return render_template("countries.html", countries = countries)

# @users_blueprint.route("/users/<id>")
# def show(id):
#     user = user_repository.select(id)
#     locations = location_repository.locations_for_user(user)
#     return render_template("users/show.html", user=user, locations=locations)
