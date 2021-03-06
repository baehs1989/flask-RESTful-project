from db import db
from models.team import TeamModel

class PlayerModel(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    back_number = db.Column(db.Integer)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team = db.relationship('TeamModel')
    division = db.Column(db.Integer)

    def __init__(self, name, back_number, team_id):
        self.name = name
        self.back_number = back_number
        self.team_id = team_id
        self.division = TeamModel.find_by_id(team_id).division

    def json(self):
        return {"name": self.name, "back_number": self.back_number, "team_name" : self.team.name, "division": self.division}

    @classmethod
    def find_by_name(cls, name):
        print (cls.query.filter_by(name=name))
        return cls.query.filter_by(name=name) # SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def find_player_in_team(cls, name, team_id, back_number):
        return cls.query.filter_by(name=name, team_id=team_id, back_number=back_number).first()

    @classmethod
    def find_by_back_number_in_team(cls, back_number, team_id):
        return cls.query.filter_by(back_number=back_number, team_id=team_id).first()

    @classmethod
    def find_by_name_back_number(cls, name, back_number):
        return cls.query.filter_by(name=name, back_number=back_number)

    @classmethod
    def find_by_team_id(cls, team_id):
        return cls.query.filter_by(team_id=team_id)

    @classmethod
    def find_by_division(cls, division):
        return cls.query.filter_by(division=division)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
