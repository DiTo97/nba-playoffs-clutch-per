# Player efficiency rating

Player efficiency rating (**PER**) is an advanced NBA metric introduced in 2007 by John Hollinger as a methodology for comparing the relative accomplishments of players across leagues, as well as across years. The idea is relatively simple, despite being commonly viewed as complex: Produce a value for each player such that it captures their influence on the game in terms of **points per possession** (PPP). In fact, we should emphasize the _minute/possession_ relationship, as the original intention of the metric was to to capture per minute effects of each NBA player; however, the PER model transforms that into a per possession framework.

The rest of this write-up is organized as follows: First, we introduce the actual PER model as a combination of 13 terms and three scaling factor. Then, we dive into each of those terms analyzing how it reflects a different aspect of the game of basketball.

## The PER Model

The PER model is constructed in a multi-step fashion. First, a player's **unadjusted PER** is computed. This measurement reflects a player's per minute per possession personal contribution to the game. The formula is given as:

<img src="https://render.githubusercontent.com/render/math?math=\begin{align} \text{uPER} =%26 \dfrac{(1) - (2) %2B (3)}{\text{Min}} \notag \\ \\ \\ \\ (1) =%26 3\text{PM} %2B \dfrac{2}{3}\text{Ast} %2B \left(2 - f \dfrac{\text{Ast}_{tm}}{\text{FGM}_{tm}}\right)\text{FGM} %2B \dfrac{1}{2}\text{FTM} \left(2 - \dfrac{1}{3}\dfrac{\text{Ast}_{tm}}{\text{FGM}_{tm}} \right) \\ \\ (2) =%26 \dfrac{\text{PF}}{\text{PF}_{lg}}\text{FTM}_{lg} \\ \\ (3) =%26 v\left( (\text{Reb} - \text{OReb}) %2B d\text{OReb} -\text{TO} -d\left( \text{FGA} - \text{FGM} \right) -0.44(0.44 %2B 0.56d)(\text{FTA} - \text{FTM}) %2B \text{Stl} %2B d\text{Blk} %2B 0.44 \text{FTA}_{lg} \dfrac{\text{PF}}{\text{PF}_{lg}} \right) \end{align}">

where <img src="https://render.githubusercontent.com/render/math?math=tm"> and <img src="https://render.githubusercontent.com/render/math?math=lg"> are suffixes labelling team- and league-average metrics, respectively, as opposed to player averages. About the league-average scaling factors, <img src="https://render.githubusercontent.com/render/math?math=f"> is an unknown factor regulating the assist-to-point conversion, <img src="https://render.githubusercontent.com/render/math?math=d"> is the defensive rebound percentage, and <img src="https://render.githubusercontent.com/render/math?math=v"> is the value for possession, that is, the average number of points per possession. The latter three are defined as follows:

<img src="https://render.githubusercontent.com/render/math?math=f = \dfrac{2}{3} - \left( 0.25 \dfrac{\text{Ast}_{lg}}{\text{FGM}_{lg}} \dfrac{\text{FTM}_{lg}}{\text{FGM}_{lg}}  \right)">
 
<img src="https://render.githubusercontent.com/render/math?math=v = \dfrac{\text{Pts}_{lg}}{\text{FGA}_{lg} - \text{OReb}_{lg} %2B \text{TO}_{lg} %2B 0.44 \text{FTA}_{lg}}">

<img src="https://render.githubusercontent.com/render/math?math=d = \dfrac{\text{DReb}_{lg}}{\text{Reb}_{lg}}">

Most other terms should be familiar to people with a decent experience in basketball, as they are all commonly registered in NBA box scores. The model looks torturous at first glance; however, it is not all that bad. Later, we will break it down term by term.

Secondly, a **pace adjustment** -- hereafter referred to as <img src="https://render.githubusercontent.com/render/math?math=\gamma"> for brevity -- is computed to allow for fair comparisons of the PER between up-tempo and down-tempo teams in the league. This adjustment is given by:

<img src="https://render.githubusercontent.com/render/math?math=\gamma = \dfrac{\text{Pace}_{lg}}{\text{Pace}_{tm}}">

which serves as a de-facto *stratified sampling correction*. This correction is intended to normalize players by standardizing the pace of their team to the league's: For example, without this adjustment it would be impossibile to compare the Golden State Warriors with the Philadelphia 76ers, as the former play at a much higher pace than the latter; thus generating much more game opportunities that would reflect in the PER. A value of <img src="https://render.githubusercontent.com/render/math?math=1"> indicates that the team plays at the league average. In our example, we would expect the GSW to have a rate higher than the league-average, as opposed to the 76ers: <img src="https://render.githubusercontent.com/render/math?math=\gamma_{\text{GSW}} > 1 > \gamma_{\text{76ers}}">. To calculate the league pace (LP), we simply count the # of possessions for every team in the NBA, divide that by the # of minutes played and multiply by 48 minutes. To calculate a team's pace (TP), we follow a slightly different formulation: We average the # of possessions for the team with their opponent's, and only then divide by the # of minutes played, and multiply by 48 minutes. You may ask "Why": LP is a **census of all possessions**, whereas TP is a **sample from the population of all possessions**.

The resulting PER is called **adjusted PER**, and is given by:

<img src="https://render.githubusercontent.com/render/math?math=\text{aPER} = \text{uPER} * \gamma">

Thirdly, and finally, a league adjustment is performed to allow fair comparisons across years. Such adjustment enforces a value of <img src="https://render.githubusercontent.com/render/math?math=15"> to always represent the mean of the league PER. As a result, the formula for PER is given by:

<img src="https://render.githubusercontent.com/render/math?math=\text{PER} = \text{aPER} \dfrac{15}{\text{aPER}_{lg}}">

where <img src="https://render.githubusercontent.com/render/math?math=\text{aPER}_{lg}"> is the league aPER given by weighted averaging the aPER of all the players in the league.

As we have seen, the PER model is long, but not complex. At least, for anything that is not called uPER. In the next section, we will dissect the uPER formula analyzing it term by term.

## Breakdown of the uPER Formula

Breakdown coming soon...
<!-- https://squared2020.com/2017/09/01/breaking-down-player-efficiency-rating/ -->
