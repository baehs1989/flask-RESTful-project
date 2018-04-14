from db import db

class TeamModel(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    division = db.Column(db.Integer)

    players = db.relationship('PlayerModel', lazy='dynamic', single_parent=True, cascade="all, delete-orphan")

    def __init__(self, name, division):
        self.name = name
        self.division = division

    def json(self):
        return {"team_id": self.id, "name": self.name, "division": self.division, "players": [player.json() for player in self.players.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_division(cls, division):
        return cls.query.filter_by(division=division)

    @classmethod
    def find_by_name_division(cls, name, division):
        return cls.query.filter_by(division=division, name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
