from application.services.infoFuria import getFuriaRoster, getFuriaRecentMatches, getFuriaUpcomingMatches
from application.model.db_roster import RosterDatabase
from application.model.db_matches import MatchesDatabase

DBRoster = RosterDatabase()
DBMatches = MatchesDatabase()

def update_roster():
    players = getFuriaRoster()
    if not DBRoster.check_roster_exists():
        DBRoster.insert_roster(players)
    else:
        DBRoster.update_roster(players)

def update_upcoming_matches():
    upcoming_matches = getFuriaUpcomingMatches()
    if not DBMatches.check_upcoming_matches_exist():
        DBMatches.insert_upcoming_matches(upcoming_matches)
    else:
        DBMatches.update_upcoming_matches(upcoming_matches)

def update_past_matches():
    past_matches = getFuriaRecentMatches()
    if not DBMatches.check_past_matches_exist():
        DBMatches.insert_past_matches(past_matches)
    else:
        DBMatches.update_past_matches(past_matches)
