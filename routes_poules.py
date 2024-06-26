from flask import Blueprint, request, jsonify
from fonctions.poules import creer_poules,rechercher_poule_de_tournoi, dell
from bson import json_util

poule_bp = Blueprint('poule_bp', __name__)


# Route pour la création des poules d'un tournoi
@poule_bp.route('/cree/<string:_id>', methods=['POST'])
def creer_poules_tournoi(_id):
    poules_created = creer_poules(_id)
    return jsonify({"message": "Poules créées avec succès", "poules_created": poules_created})


@poule_bp.route('/rechercher/<string:_id>', methods=['GET'])
def rechercher_poules_tournoi(_id):
    poule = rechercher_poule_de_tournoi(_id)
    return jsonify(poule)


@poule_bp.route('/del', methods=['GET'])
def dell():
    dell()
    return jsonify({"message": "Poules créées avec succè"})
