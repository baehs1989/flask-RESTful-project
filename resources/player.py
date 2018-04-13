from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.player import PlayerModel
from models.team import TeamModel

class Player(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'back_number',
        type=int,
        required=True,
        help="This field must be integer"
    )

    parser.add_argument(
        'team_id',
        type=int,
        required=True,
        help="This field must be integer"
    )

    def get(self, name):
        players = PlayerModel.find_by_name(name)
        if players.count() > 0:
            return {"players": [player.json() for player in players]}
        return {"message": "Player does not exists"}

    def post(self, name):
        data = Player.parser.parse_args()
        if TeamModel.find_by_id(data['team_id']) is None:
            return {"message" : "Team does not exist"}
        if PlayerModel.find_by_back_number_in_team(data['back_number'], data['team_id']):
            return {"message" : "Back number is already taken."}
        if PlayerModel.find_player_in_team(name, data['team_id'], data['back_number']):
            return {"message": "Player already exists in this team"}
        player = PlayerModel(name, **data)
        player.save_to_db()
        return player.json()


    def delete(self, name):
        data = Player.parser.parse_args()
        if TeamModel.find_by_id(data['team_id']) is None:
            return {"message" : "Team does not exist"}
        player = PlayerModel.find_player_in_team(name, data['team_id'], data['back_number'])
        if player:
            player.delete_from_db()
        return {"message":"Player deleted"}

class PlayerList(Resource):
    def get(self, team_id=None):
        if team_id:
            players = PlayerModel.find_by_team_id(team_id)
        else:
            players = PlayerModel.query.all()
        return {"players": [player.json() for player in players]}