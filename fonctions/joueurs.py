from fonctions.connexion import joueurs
from bson import ObjectId
from fonctions.tournoi import rejoindre_tournoi



def recherche_joueur(_id):
    result = joueurs.find_one({"_id": ObjectId(_id)})
    return result

    
def inserer_joueur(nom, prenom, age, niveau, email, tournois):
    j = joueurs.insert_one({
        "nom": nom,
        "prenom": prenom,
        "âge": age,
        "niveau": niveau,
        "email": email,
        "Tournois": ObjectId(tournois)
    }
    )
    rejoindre_tournoi(tournois,j.inserted_id)

def inserer_joueur_pour_equipe(nom, prenom, age, niveau, email, tournois):
    j = joueurs.insert_one({
        "nom": nom,
        "prenom": prenom,
        "âge": age,
        "niveau": niveau,
        "email": email,
        "Tournois": ObjectId(tournois)
    }
    )
    id_joueur = j.inserted_id
    rejoindre_tournoi(tournois,j.inserted_id)
    return id_joueur


def rechercher_joueur(_id):
    joueur = joueurs.find_one({"_id": ObjectId(_id)})
    return ObjectId(joueur)


def modifier_joueur(_id, data):
    joueurs.update_one({"_id": ObjectId(_id)}, {"$set": data})


def supprimer_joueur(_id):
    joueurs.delete_one({"_id": ObjectId(_id)})
    

def dell():
    joueurs.delete_many({})