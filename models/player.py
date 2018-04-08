from db import db

class PlayerModel(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    back_number = db.Column(db.Integer)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team = db.relationship('TeamModel')

    def __init__(self, name, back_number, team_id):
        self.name = name
        self.back_number = back_number
        self.team_id = team_id

    def json(self):
        return {"name": self.name, "back_number": self.back_number, "team": self.team.name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
