# Database Module

import mysql.connector
from datetime import datetime

# Creates Player Table
#cursor.execute("CREATE TABLE Players (PlayerID int PRIMARY KEY NOT NULL AUTO_INCREMENT, PlayerName VARCHAR(15) NOT NULL, PlayerPassword VARCHAR(20) NOT NULL, DateCreated datetime NOT NULL)")
#cursor.execute("CREATE TABLE Games (PlayersID int, Difficulty ENUM('Beginner', 'Intermediate', 'Expert') NOT NULL, Time DECIMAL(5, 1) NOT NULL, Score DECIMAL(4, 1) NOT NULL, Created datetime NOT NULL)")


def AddToTable(Difficulty, PlayersID, Time, Score):
    if PlayersID != -1: # If they arent guest and have logged in
    # %s allows me to pass in variables
        DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
        cursor = DATABASE.cursor(buffered=True)
        cursor.execute('INSERT INTO Games (PlayersID, Difficulty, Time, Score, Created) VALUES (%s, %s, %s, %s, %s)', (PlayersID, Difficulty, Time, Score, datetime.now())) # Adds info and the playerID into the game table
        DATABASE.commit()

def SelectFromTable(Difficulty, Order):
    DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
    cursor = DATABASE.cursor(buffered=True)
    if Order == 'Time':
        cursor.execute("SELECT PlayersID, Time FROM Games WHERE Difficulty = '%s' AND Score = '100.0' ORDER BY Time" %(Difficulty))
    if Order == 'Date':
        cursor.execute("SELECT PlayersID, Created FROM Games WHERE Difficulty = '%s' AND Score = '100.0' ORDER BY Created" %(Difficulty))
    data = []
    PlayerIDs = []
    # Probably a smarter way of doing this
    for x in cursor:
        data.append(x[1])
        PlayerIDs.append(x[0])
    PlayerNames = []
    for i in range(len(PlayerIDs)):
        if PlayerIDs[i] == -1:
            PlayerNames.append("('Guest')")
        else:
            cursor.execute("SELECT PlayerName FROM Players WHERE PlayerID = '%s'" %(PlayerIDs[i]))
            for x in cursor:
                PlayerNames.append(x)
    info = []
    for i in range(len(PlayerNames)):
        info.append(str(PlayerNames[i]) + str(data[i]))
        
    return info

def SelectFromPlayer(PlayerID):
    DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
    cursor = DATABASE.cursor(buffered=True)
    cursor.execute("SELECT DateCreated FROM Players WHERE PlayerID = '%s'" %(PlayerID))
    for x in cursor:
        DateCreated = x
    return DateCreated


def SelectFromGames(PlayerID, Difficulty):
    DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
    cursor = DATABASE.cursor(buffered=True)
    cursor.execute("SELECT Difficulty, Score, Time, Created FROM Games WHERE PlayersID = '%s' AND Difficulty = '%s' ORDER BY Created DESC" %(PlayerID, Difficulty))
    GamesPlayed = 0
    PlayerGameHistory = ''
    for x in cursor:
        PlayerGameHistory = PlayerGameHistory + str(x)   
        GamesPlayed += 1
    cursor.execute("SELECT * FROM Games WHERE PlayersID = '%s' AND Score = '100.0' AND Difficulty = '%s'" %(PlayerID, Difficulty))
    GamesWon = 0
    for x in cursor:
        GamesWon += 1
    GamesLost = GamesPlayed - GamesWon
    
    cursor.execute("SELECT * FROM Games")
    TotalGamesPlayed = 0
    for x in cursor:
        TotalGamesPlayed += 1
    cursor.execute("SELECT * FROM Games WHERE Score = '100.0'")
    TotalGamesWon = 0
    for x in cursor:
        TotalGamesWon += 1
    
    return GamesWon, GamesLost, GamesPlayed, PlayerGameHistory, TotalGamesPlayed, TotalGamesWon
    
    
def clearAllFromTable():
    # Used for manually clearing tables
    DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
    cursor = DATABASE.cursor(buffered=True)
    cursor.execute("TRUNCATE TABLE Players")
    cursor.execute("TRUNCATE TABLE Games")


def CheckAvailability(Username):
    # Checks if the Username is already in use to avoid people stealing peoples names
    DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
    cursor = DATABASE.cursor(buffered=True)
    cursor.execute("SELECT PlayerName, PlayerPassword FROM Players WHERE PlayerName = '%s'" %(Username))
    y = 0
    for x in cursor:
        y = y + 1
    if y == 0:
        return True # Not taken
    else:
        return False # Taken
        
def AddPlayer(Username, Password):
    DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
    cursor = DATABASE.cursor(buffered=True)
    cursor.execute("INSERT INTO Players (PlayerName, PlayerPassword, DateCreated) VALUES (%s, %s, %s)", (Username, Password, datetime.now()))
    DATABASE.commit()
    
 
def LogIn(Username, Password):

    # Logs Into account to not appear as guest
 
    DATABASE = mysql.connector.connect(host="localhost",user="root",passwd="root",database="minesweeperscores")
    cursor = DATABASE.cursor(buffered=True)
    cursor.execute("SELECT PlayerID, PlayerName, PlayerPassword FROM Players WHERE PlayerName = '%s' AND PlayerPassword = '%s'" %(Username, Password))
    y = 0
    for x in cursor: # Checks it exsits
        y = y + 1
        PlayerID = x[0]
    if y == 0:
        PlayerID = 0
        print('Password wrong')
        return PlayerID, Username, False # Returns the players ID
    else:
        print('logged in')
        return PlayerID, Username, True

