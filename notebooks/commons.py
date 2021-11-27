import unicodedata

from datetime import datetime
from pathlib import Path


DIR_root = Path(__file__).absolute().parents[1]
DIR_data = DIR_root / 'data'

DIR_raw  = DIR_data / 'raw'
DIR_processed = DIR_data / 'processed'

DIR_raw_pace = DIR_raw / 'Pace'
DIR_raw_players = DIR_raw / 'Players'
DIR_raw_teams = DIR_raw / 'Teams'

DIR_processed_league = DIR_processed / 'League'

YEAR_start = 1996
YEAR_end   = 2020


def unicd2ascii(unicd_data: str) -> str:
    """
    Normalise unicode data in Python to remove umlauts, accents etc.
    """
    return unicodedata.normalize('NFKD', unicd_data) \
                      .encode('ASCII', 'ignore')     \
                      .decode('UTF-8')


def dob2age(dob: str, _format: str = "%m/%d/%Y") -> int:
    """
    Compute the age from the date of birth (DoB).
    """
    bdate = datetime.strptime(dob, _format).date()
    today = bdate.today()
  
    return today.year - bdate.year \
               - ((today.month, today.day) < 
                  (bdate.month, bdate.day))


def year2rangestr(year: int) -> str:
    next_year   = year + 1
    next_suffix = str(next_year)[2:]
    
    return '{}-{}'.format(year, next_suffix)


def year2filename(year: int, ext: str = 'csv') -> str:
    year_range = year2rangestr(year)
    
    return '{}.{}'.format(year_range,
                          ext)
