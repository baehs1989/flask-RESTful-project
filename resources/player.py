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
        'team_name',
        type=str,
        required=True,
        help="This field must be integer"
    )

    parser.add_argument(
        'new_back_number',
        type=str,
        required=False,
        help="This field must be integer"
    )

    def get(self, name, division=None, team_name=None):
        if team_name is None and division is None:
            players = PlayerModel.find_by_name(name)
            if players.count() > 0:
                return {"players": [player.json() for player in players]}
        elif team_name is None:
            print (division)
        else:
            team = TeamModel.find_by_name_division(team_name, division)
            if team:
                players = PlayerModel.find_by_team_id(team.id)
                if players.count() > 0:
                    return {"players": [player.json() for player in players]}
        return {"message": "Player does not exists"}

    def post(self, name):
        data = Player.parser.parse_args()
        team = TeamModel.find_by_name(data['team_name'])
        if team is None:
            return {"message" : "Team does not exist"}

        if PlayerModel.find_by_back_number_in_team(data['back_number'], team.id):
            return {"message" : "Back number is already taken."}

        player = PlayerModel(name, data['back_number'], team.id)
        player.save_to_db()
        return player.json()


    def delete(self, name):
        data = Player.parser.parse_args()
        team = TeamModel.find_by_name(data['team_name'])
        if team is None:
            return {"message" : "Team does not exist"}

        player = PlayerModel.find_player_in_team(name, team.id, data['back_number'])
        if player:
            player.delete_from_db()
        return {"message":"Player deleted"}

    def put(self, name):
        data = Player.parser.parse_args()

        team = TeamModel.find_by_name(data['team_name'])
        if team is None:
            return {"message" : "Team does not exist"}

        if PlayerModel.find_by_back_number_in_team(data['new_back_number'], team.id):
            return {"message" : "Back number is already taken."}

        player = PlayerModel.find_player_in_team(name, team.id, data['back_number'])

        if player is None:
            return {"message" : "Player doesn not exist"}
        else:
            if data['new_back_number'] is None:
                return {"message" : "New Back Number is missing"}
            player.back_number = data['new_back_number']


        player.save_to_db()

        return player.json()


class PlayerList(Resource):
    def get(self, team_name=None, division=None):
        if team_name is None and division is None:
            players = PlayerModel.query.all()
        else:
            team = TeamModel.find_by_name(team_name)
            if team:
                players = PlayerModel.find_by_team_id(team.id)
            else:
                players = PlayerModel.find_by_division(division)


        return {"players" : [player.json() for player in players]}
