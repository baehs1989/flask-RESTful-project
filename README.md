URLs
../register
  - POST: register user in the system. Must pass "username" and "password" in JSON

../get_token
  - POST: will return JWT token if registered "username" and its correct "password" passed in JSON format.
  - You will need to include valid JWT token to request DELETE calls.

../team/<string:name>
  - GET: return JSON with the team info/ player list
  - POST: create the team. Must send JSON with "division" variable
  - PUT: Update or create the team. Must send JSON with "division" variable
  - DELETE : delete the team. JWT token required

../teams
  - GET: return all teams in JSON format

../teams/<int:division>
  - GET: return all teams in the division in JSON format

../player/<string:name>
  - GET: return the players with the name in JSON
  - POST: create the player. Must send JSON with "back_number", "team_name"
  - DELETE: delete the player. Must send JSON with "back_number", "team_name"
  - PUT: Update the player's back number. Must send JSON with "back_number", "team_name", and "new_back_number"

../players
  - GET: return all players in JSON format

../players/<int:division>
  - GET: return all players participated in the division in JSON format

../players/<int:team_name>
  - GET: return all players in the team.
