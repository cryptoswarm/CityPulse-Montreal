from src.models.base import Base
from sqlalchemy import ForeignKey
from src import db
from sqlalchemy.orm import relationship
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow
from src.models.patinoir_condition import PatConditionSchema


ma = Marshmallow()


class Patinoire(Base):
    __tablename__ = "patinoire"

    nom_pat = db.Column(db.String(255), unique=True, nullable=False)
    arron_id = db.Column(db.Integer, ForeignKey("arrondissement.id"))
    children = relationship("PatinoirCondition")

    def __init__(self, nom_pat, arron_id):
        self.nom_pat = nom_pat
        self.arron_id = arron_id

    def __repr__(self):
        return "<Ptinoire(patinoire_id='%d', nom_pat='%s', arron_id='%d')>" % (
            self.id,
            self.nom_pat,
            self.arron_id,
        )

    def asDictionary(self):
        return {"id": self.id, "nom_pat": self.nom_pat}


class PatAndCondition(Patinoire):
    def __init__(self, id, nom_pat, arron_id, conditions):
        super().__init__(nom_pat, arron_id)
        self.id = id
        self.conditions = conditions


class PatinoireSchema(ma.Schema):
    id = fields.Number()
    nom_pat = fields.String(required=True, validate=validate.Length(1))
    arron_id = fields.Number(required=True)


class EditPatinoireSchema(ma.Schema):
    nom_pat = fields.String(required=True, validate=validate.Length(1))


class PatAndConditionSchema(ma.Schema):
    id = fields.Number()
    nom_pat = fields.String(required=True, validate=validate.Length(1))
    arron_id = fields.Number(required=True)
    conditions = fields.Nested(PatConditionSchema, many=True)
