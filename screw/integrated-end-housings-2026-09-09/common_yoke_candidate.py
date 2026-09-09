import cadquery as cq
from cadquery import exporters
from pathlib import Path

# Engineering candidate only. Exact production values remain gated by coupon/bench results.
SHAFT_D = 6.35
GUIDE_ROD_D = 6.35
GUIDE_RADIUS_NOMINAL = 33.25
R4_POCKET_CANDIDATE_D = 15.96
R4_POCKET_DEPTH = 4.90
YOKE_T = 10.0
CENTER_BOSS_OD = 26.0
GUIDE_BOSS_OD = 22.0
F02_PITCH = 30.0

def union(parts):
    out = parts[0]
    for part in parts[1:]:
        out = out.union(part)
    return out

def common_yoke():
    r = GUIDE_RADIUS_NOMINAL
    c = cq.Workplane("XY").circle(CENTER_BOSS_OD/2).extrude(YOKE_T)
    l = cq.Workplane("XY").center(-r,0).circle(GUIDE_BOSS_OD/2).extrude(YOKE_T)
    rr = cq.Workplane("XY").center(r,0).circle(GUIDE_BOSS_OD/2).extrude(YOKE_T)
    web_l = cq.Workplane("XY").box(r,10,YOKE_T,centered=(False,True,False)).translate((-r,0,0))
    web_r = cq.Workplane("XY").box(r,10,YOKE_T,centered=(False,True,False))
    y = union([c,l,rr,web_l,web_r])

    # Rotor support: pocket opens toward the screw span.
    y = y.cut(cq.Workplane("XY").circle(3.5).extrude(YOKE_T+1))
    y = y.cut(cq.Workplane("XY").circle(R4_POCKET_CANDIDATE_D/2)
              .extrude(R4_POCKET_DEPTH+0.02)
              .translate((0,0,YOKE_T-R4_POCKET_DEPTH)))

    # Current F02 cap pitch.
    for x in (-F02_PITCH/2,F02_PITCH/2):
        y = y.cut(cq.Workplane("XY").center(x,0).circle(1.675).extrude(YOKE_T+1))

    # Keyed replaceable guide-bushing pockets.
    for x in (-r,r):
        y = y.cut(cq.Workplane("XY").center(x,0).rect(10.25,12.25)
                  .extrude(7.55).translate((0,0,YOKE_T-7.5)))
        y = y.cut(cq.Workplane("XY").center(x,0).circle(17.25/2)
                  .extrude(2.45).translate((0,0,YOKE_T-2.4)))
    return y

def guide_bushing(offset=0.0):
    stem = cq.Workplane("XY").rect(10,12).extrude(7.5)
    flange = cq.Workplane("XY").circle(8.5).extrude(2.4).translate((0,0,7.5))
    b = stem.union(flange)
    b = b.cut(cq.Workplane("XY").center(offset,0).circle(6.65/2).extrude(11))
    return b
