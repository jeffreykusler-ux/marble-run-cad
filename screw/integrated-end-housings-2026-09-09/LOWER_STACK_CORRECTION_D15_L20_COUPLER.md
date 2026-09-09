# Lower-stack correction after exact coupler identification

Date: 2026-09-09
Status: ENGINEERING DIRECTION

Exact coupler family supplied by Jeff:
uxcell 3 mm -> 6.35 mm flexible helical coupling, D15 x L20 mm.

Existing candidate lower-yoke underside Z = 47.0 mm is too low if the measured N20 body remains fully above the wooden base.

Measured working N20:
- body length without shaft: 25.32 mm
- shaft protrusion: 10.75 mm
- shaft tip with motor bottom at base plane: Z = 36.07 mm

For a 20.0 mm coupler:
- 4 mm motor-shaft engagement -> coupler bottom 32.07, top 52.07 mm
- 5 mm engagement -> bottom 31.07, top 51.07 mm
- 6 mm engagement -> bottom 30.07, top 50.07 mm
- 7 mm engagement -> bottom 29.07, top 49.07 mm

Therefore the previous 47.0 mm yoke underside conflicts with the coupler.

## Correction

Raise the lower common-yoke underside target to **54.0 mm above the wooden base** for the next candidate.

This provides:
- >=1.9 mm axial free space above a worst-case 4 mm motor engagement assumption,
- approximately 4.0 mm free space with 6 mm motor engagement,
- no need to recess the N20 into the laminated base,
- no need to hollow the bearing yoke underneath and weaken its bearing-support web.

Candidate yoke top becomes 64.0 mm with the existing 10 mm yoke thickness.

The exact motor sled Z remains adjustable and is not frozen until coupler bore depth/set-screw position is physically checked.

Do not use the coupler as an axial stop. Neither shaft should be intentionally bottomed in its bore.
