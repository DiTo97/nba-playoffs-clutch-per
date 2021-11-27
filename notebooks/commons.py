import typing as t
import unicodedata

from datetime import datetime
from pathlib import Path


DIR_root = Path(__file__).absolute().parents[1]
DIR_data = DIR_root / 'data'

DIR_raw  = DIR_data / 'raw'
DIR_pro  = DIR_data / 'processed'

# Folder structure: Playoffs
DIR_raw_po = DIR_raw / 'PO'
DIR_pro_po = DIR_pro / 'PO'

DIR_raw_po_pace    = DIR_raw_po / 'pace'
DIR_raw_po_players = DIR_raw_po / 'players'
DIR_raw_po_teams   = DIR_raw_po / 'teams'

DIR_pro_po_teams   = DIR_pro_po / 'teams'
DIR_pro_po_players = DIR_pro_po / 'players'
DIR_pro_po_league  = DIR_pro_po / 'league'

# Folder structure: Regular season
DIR_raw_rs = DIR_raw / 'RS'
DIR_pro_rs = DIR_pro / 'RS'

DIR_raw_rs_pace    = DIR_raw_rs / 'pace'
DIR_raw_rs_players = DIR_raw_rs / 'players'
DIR_raw_rs_teams   = DIR_raw_rs / 'teams'

DIR_pro_rs_teams   = DIR_pro_rs / 'teams'
DIR_pro_rs_players = DIR_pro_rs / 'players'
DIR_pro_rs_league  = DIR_pro_rs / 'league'

# Metaparameters
GP_min = 3

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


def year2rangestr(year1: int,
                  year2: t.Optional[int] = None) -> str:
    if year2 is None:
        year2 = year1 + 1

    year2_suffix = str(year2)[2:]
    
    return '{}-{}'.format(year1, year2_suffix)


def year2filename(year1: int,
                  year2: t.Optional[int] = None,
                  ext: str = 'csv') -> str:
    _range = year2rangestr(year1, year2)
    
    return '{}.{}'.format(_range, ext)
