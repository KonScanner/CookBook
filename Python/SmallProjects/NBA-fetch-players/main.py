from Api import get_players, write_file


if __name__ == "__main__":
    season = 2021
    data = get_players(year=season)
    player_ob = data.league.standard
    for i in player_ob[:5]:
        print(i.pos, i.firstName, i.lastName, i.heightMeters,
              i.isActive, i.jersey, i.dateOfBirthUTC, i.country)
    write_file(season=season)
