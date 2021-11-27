# Ranking of the Most Clutch NBA Players in the Playoffs since the 1996-97 Season by PER

**Definition - Clutch time:** Last three minutes of a game (Q4/OT) if leading or trailing by three points or fewer.

## Folder structure

- **data**:
    + *raw* contains all raw data about either players or teams in clutch time for all NBA playoffs starting from the first available 1996-97 season. It also includes a table with the unique player Ids from [Basketball-Reference](https://www.basketball-reference.com/).
    + *processed* contains all derived data (i.e., league averages). The final CSV table with the ranking of the most clutch players in the NBA playoffs by PER can be found in the *PER* subfolder.
    
- **notebooks** contains two Jupyter notebooks: one for the processing of raw data, and one for PER computation.
