URLs for API
- /register
  - POST (create user. Must pass "username" and "password" in JSON)

- /get_token
  - POST (return JWT token if registered "username" and "password" in JSON)

- /team/<team_name>
  - GET (return team info and player list)
  - POST (create team. "division" number must be included in JSON)
  - PUT (Update or create team. "division" number must be included in JSON)
  - DELETE (delete team. JWT token required)

- /teams
  - GET: list all teams

- /teams/<division_number>
  - GET: list all teams in division

- /player/<player_name>
  - GET: list all players with <player_name>
  - POST: create player. "back_number" and "team_name" must be included in JSON
  - DELETE: delete player. "back_number" and "team_name" must be included in JSON
  - PUT: update player's back number. "back_number, "team_name" and "new_back_number" must be included in JSON

- /players
  - GET: list all players

- /players/<division_number>
  - GET: list all players in the division

- /player/<team_name>
  - GET: list all players in the team
