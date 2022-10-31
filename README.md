# trainingprogram

Henter løbehistorikken fra Strava.
Baseret på en mindre analyse af disse data laves der et forslag til en trænignsplan.

Målet er en iterativ algoritme som først danner en plan for næste periode. 
Baseret på den antagelse at løberen så følger denne plan dannes den efterføgendee priode og så fremdeldes.
Dvs. at planen bliver en del af input til næste plan.
input H3,H2,H1 -> P0
input H2,H1, P0 -> P1
input H1, P0, P1 -> P2 
