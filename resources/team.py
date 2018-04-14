from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.team import TeamModel

class Team(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'division',
        type=int,
        required=False,
        help="This field must be integer"
    )

    def get(self, name, division=None):
        '''
        data = Team.parser.parse_args()
        if data['division']:
            team = TeamModel.find_by_name_division(name, data['division'])
            if team:
                return {"team": team.json()}
        else:
            teams = TeamModel.find_by_name(name)
            if teams.count() > 0:
                return {"teams": [team.json() for team in teams]}
        return {"message" : "Team not found"}, 404
        '''
        if division is None:
            teams = TeamModel.find_by_name(name)
            if teams.count() > 0:
                return {"teams" : [team.json() for team in teams]}
        else:
            team = TeamModel.find_by_name_division(name, division)
            if team:
                return {"teams" : team.json()}
        return {"message" : "Team not found"}, 404

    def post(self, name, division=None):
        # data = Team.parser.parse_args()
        #
        # if data['division'] is None:
        #     return {"division": "This field can not be blank"}
        if division is None:
            return {"division": "This field can not be blank"}

        if TeamModel.find_by_name_division(name, division):
            return {"message" : "{} in division {} already exists".format(name,division)}
        team = TeamModel(name, division)
        try:
            team.save_to_db()
        except:
            return {"message" : "An error occured while creating the team."}, 500

        return team.json()


    def delete(self, name, division=None):
        # data = Team.parser.parse_args()
        #
        # if data['division'] is None:
        #     return {"division": "This field can not be blank"}
        #
        # team = TeamModel.find_by_name_division(name,data['division'])
        # if team:
        #     team.delete_from_db()
        # return {"message": "Team deleted"}
        if division is None:
            return {"message": "Missing Division variable"}, 404
        team = TeamModel.find_by_name_division(name,division)
        if team:
            team.delete_from_db()
        return {"message": "Team deleted"}

class TeamList(Resource):
    def get(self, division=None):
        if division:
            teams = TeamModel.find_by_division(division)
        else:
            teams = TeamModel.query.all()
        return {"teams": [team.json() for team in teams]}
