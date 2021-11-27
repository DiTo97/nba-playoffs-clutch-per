# Ranking of the Most Clutch NBA Players in the Playoffs since the 1996-97 Season by PER

**Definition - Clutch time:** Last three minutes of a game (Q4/OT) if leading or trailing by three points or fewer.

This projects stems from the necessity to better formalize the concept of clutchness (or clutch gene) which is still somewhat of a grey area in the NBA as of 2021. Moreover, many people, including fans and the media, often associate being clutch with the ability to knock down the last shot. Here instead we privilige the approach taken by the NBA website: the last stretch of a high-pressure close game. Nonetheless, we restrict the time span to three minutes, and discard regular season data altogether. This last decision may be reviewed in the future, as the amount of data points hidden in the NBA playoffs is somewhat limited, which may result in fuzzy PER values with a lot of noise. For the moment, though, we opted for it as the true clutch gene shows up only when the stakes are heighest. It is nice to win games at the buzzer in the regular season, but missing or hitting a shot does not really mean that much, as a 82-game season leaves all the room to recover. Conversely, each game matters in the playoffs.

## About the choice of PER

Being clutch regards many more aspects of ball player than mere shooting: Assisting a teammate, grabbing a tough rebound, or blocking a shot on the other end of the floor are as valuable to the separate who wins from who goes home. For this reason, we discarded many metrics focused eccessively on the ability to shoot the ball: field goal percentage (FG%), effective field goal percentage (eFG%), true shooting percentage (TS%), to name a few. Instead, we were looking for a metric that would highlight the all-around impact of a player on the NBA court when the lanes get tight, fatigue shivers and the hands become slippery: [Player rating efficiency](https://en.wikipedia.org/wiki/Player_efficiency_rating) (PER), introduced by J. Hollinger during the 2006-07 season.

## Folder structure

- **data**:
    + *raw* contains all raw data about either players or teams in clutch time for all NBA playoffs starting from the first available 1996-97 season. It also includes a table with the unique player Ids from [Basketball-Reference](https://www.basketball-reference.com/).
    + *processed* contains all derived data (i.e., league averages). The final CSV table with the ranking of the most clutch players in the NBA playoffs by PER can be found in the *PER* subfolder.
    
- **notebooks** contains two Jupyter notebooks: one for the processing of raw data, and one for PER computation.
