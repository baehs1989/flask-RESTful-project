from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.player import PlayerModel

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
        if PlayerModel.find_by_name_back_number(name, data['back_number']).count() > 0:
            return {"message": "Player already exists in this team"}
        player = PlayerModel(name, **data)
        player.save_to_db()
        return player.json()


    def delete():
        pass
