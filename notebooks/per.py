import pandas as pd


def f(row_PTL: pd.DataFrame) -> float:
    """
    League-average: Unknown scaling factor.
    """
    return 2/3 - (0.5*row_PTL['Ast'] / row_PTL['FGM']) \
               / (2.0*row_PTL['FGM'] / row_PTL['FTM'])


def poss_est(row_PTL: pd.DataFrame) -> float:
    """
    League-average: Per-game possessions estimate.
    Ref. NBA.com website.
    """
    return row_PTL['FGA'] - row_PTL['OReb'] \
         + row_PTL['TO']  + 0.44*row_PTL['FTA']


def vop(row_PTL: pd.DataFrame) -> float:
    """
    League-average: Value of possession.
    
    This factor estimates the average # of points per possession.
    """
    return row_PTL['Pts'] / poss_est(row_PTL)


def drbp(row_PTL: pd.DataFrame) -> float:
    """
    League-average: Defensive rebounds percentage.
    """
    return row_PTL['DReb'] / row_PTL['Reb']


def uper(row_PTL: pd.DataFrame,
         eps: float = 1e-1) -> float:
    """
    Unadjusted PER per minute.
    """
    # Avoid D-by-Z error
    row_PTL['FGM_t'] += eps
    row_PTL['PF']    += eps
    row_PTL['Min_p'] += eps
    
    # Scaling factors
    _f = f(row_PTL)
    _d = drbp(row_PTL)
    _v = vop(row_PTL)
    
    # a - 4 terms: Total points scored
    
    # a.1 3-pointers extra point
    a_1 = row_PTL['3PM_p']
    
    # a.2 Total points assisted
    a_2 = (2/3)*row_PTL['Ast_p']
    
    # a.3 Field goals made
    a_3 = (2 - _f*(row_PTL['Ast_t'] / row_PTL['FGM_t']))*row_PTL['FGM_p']
    
    # a.4 Free-throws made
    a_4 = 0.5*row_PTL['FTM_p']*(2 - (1/3)*(row_PTL['Ast_t'] / row_PTL['FGM_t']))
    
    a = a_1 + a_2 + a_3 + a_4
    
    # b - 1 terms: Total points conceded off personal fouls
    b = row_PTL['FTM']*(row_PTL['PF_p'] / row_PTL['PF'])
    
    # c - 8 terms: Total points off lost possessions
    
    # c.1 Turnovers
    c_1 = row_PTL['TO_p']
    
    # c.2 Defensive rebounds off FG missed 
    c_2 = _d*(row_PTL['FGA_p'] - row_PTL['FGM_p'])
    
    # c.3 Defensive rebounds off FT missed
    #   + Offensive rebounds percentage
    c_3 = 0.44*(0.44 + 0.56*_d)*(row_PTL['FTA_p'] - row_PTL['FTM_p'])
    
    # c.4 Defensive rebounds overall
    c_4 = (1 - _d)*(row_PTL['DReb_p'])
    
    # c.5 Offensive rebounds overall
    c_5 = _d*row_PTL['OReb_p']
    
    # c.6 Steals
    c_6 = row_PTL['Stl_p']
    
    # c.7 Defensive rebounds off blocks
    c_7 = _d*row_PTL['Blk_p']
    
    # c.8 Lost possessions off FT conceded
    c_8 = 0.44*row_PTL['FTA']*(row_PTL['PF_p'] / row_PTL['PF'])
    
    c = _v*(- c_1 - c_2 - c_3 + c_4
            + c_5 + c_6 + c_7 + c_8)
    
    tot_uPER = a - b + c
    
    # Return per minute uPER
    return tot_uPER*(1 / row_PTL['Min_p'])


def aper(row_PTL: pd.DataFrame) -> float:
    """
    Adjusted PER for 48 minutes.
    """
    return row_PTL['uPER'] * row_PTL['Pace'] \
                           / row_PTL['Pace_t']


def per(row_PTL: pd.DataFrame,
        aPER_league: float) -> float:
    """
    Player efficiency rating (PER) by J. Hollinger.
    Ref. https://en.wikipedia.org/wiki/Player_efficiency_rating
    
    League-average PER is always 15.
    """     
    return row_PTL['aPER']*(15 / aPER_league)
