from flask_sqlalchemy import Pagination
from inf5190_projet_src import db
from inf5190_projet_src.models.patinoire import Patinoire
from sqlalchemy import or_, and_, func, desc


def save_patinoire(nom_pat, arrond_id):
    patinoire = Patinoire(nom_pat, arrond_id)
    print('patinoire received :',patinoire.asDictionary())
    db.session.add(patinoire)
    db.session.commit()
    print('patinoire created :',patinoire.asDictionary())
    return patinoire

def find_patinoire_by_name(nom_pat):
    return Patinoire.query.filter_by(nom_pat=nom_pat) \
                        .first()

# def get_patinoire_id(nom_pat):
#     find_patinoire_by_name(nom_pat)

def find_patinoires_by_arr_id(arr_id):
    return Patinoire.query.filter_by(arron_id=arr_id).all()

