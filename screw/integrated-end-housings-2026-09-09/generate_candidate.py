import cadquery as cq
from cadquery import exporters
from pathlib import Path
import json

OUT = Path("generated")
OUT.mkdir(parents=True, exist_ok=True)

P = {
    "status": "ENGINEERING CANDIDATE - NOT PRINT AUTHORIZED",
    "units": "mm",
    "filament_candidate": "WHITE PLA",
    "shaft_diameter": 6.35,
    "guide_rod_diameter": 6.35,
    "r4_measured_od": 15.86,
    "r4_measured_width": 4.99,
    "r4_pocket_model_diameter": 15.96,
    "r4_pocket_depth": 4.90,
    "f02_cap_hole_pitch": 30.00,
    "f02_cap_hole_model_diameter": 2.65,
    "guide_nominal_radius": 33.25,
    "guide_insert_adjustment_family": [-1.50, -0.75, 0.0, 0.75, 1.50],
    "guide_bore_model_diameter": 6.65,
    "r01_inner_min_radius_mesh": 44.92,
    "n20_body_envelope": [11.90, 9.93, 25.32],
    "n20_output_shaft_protrusion": 10.75,
    "motor_coupler_clearance_envelope_diameter": 16.0,
    "motor_coupler_clearance_height": 24.0,
}

def union_all(parts):
    out = parts[0]
    for p in parts[1:]:
        out = out.union(p)
    return out

def yoke():
    t = 8.0
    center = cq.Workplane("XY").box(40.0, 28.0, t, centered=(True, True, False))
    left = cq.Workplane("XY").box(22.0, 18.0, t, centered=(True, True, False)).translate((-30,0,0))
    right = cq.Workplane("XY").box(22.0, 18.0, t, centered=(True, True, False)).translate((30,0,0))
    body = union_all([center,left,right])
    body = body.cut(cq.Workplane("XY").circle(P["r4_pocket_model_diameter"]/2).extrude(P["r4_pocket_depth"]).translate((0,0,t-P["r4_pocket_depth"])))
    body = body.cut(cq.Workplane("XY").circle(4.0).extrude(t))
    for x in (-15.0,15.0):
        body = body.cut(cq.Workplane("XY").center(x,0).circle(P["f02_cap_hole_model_diameter"]/2).extrude(t))
    for x in (-P["guide_nominal_radius"],P["guide_nominal_radius"]):
        body = body.cut(cq.Workplane("XY").box(12.2,14.2,t,centered=(True,True,False)).translate((x,1.5,0)))
        body = body.cut(cq.Workplane("XY").center(x,-6).circle(1.325).extrude(t))
    return body

def guide_insert(offset=0.0):
    body = cq.Workplane("XY").box(11.8,13.8,8.0,centered=(True,True,False)).translate((0,1.5,0))
    flange = cq.Workplane("XY").box(16,18,2.6,centered=(True,True,False)).translate((0,0,8))
    part = body.union(flange)
    part = part.cut(cq.Workplane("XY").center(offset,1.5).circle(P["guide_bore_model_diameter"]/2).extrude(10.6))
    part = part.cut(cq.Workplane("XY").center(0,-6).circle(1.675).extrude(10.6))
    return part

def lower_motor_tower():
    base_t=5.0; tower_h=43.0
    base = cq.Workplane("XY").box(58,58,base_t,centered=(True,True,False))
    cols=[]
    for x in (-20.5,20.5):
        for y in (-20.5,20.5):
            cols.append(cq.Workplane("XY").box(7,7,tower_h-base_t,centered=(True,True,False)).translate((x,y,base_t)))
    frame=union_all([base]+cols)
    frame=frame.union(cq.Workplane("XY").box(46,34,5,centered=(True,True,False)).translate((0,0,tower_h-0.2)))
    frame=frame.cut(cq.Workplane("XY").circle(P["motor_coupler_clearance_envelope_diameter"]/2).extrude(tower_h+5))
    for x,y in [(-24,0),(24,0),(0,-24),(0,24)]:
        frame=frame.cut(cq.Workplane("XY").center(x,y).circle(2.325).extrude(base_t))
        frame=frame.cut(cq.Workplane("XY").center(x,y).circle(5.1).extrude(2.6).translate((0,0,base_t-2.6)))
    for x,y in [(-15,-12),(-15,12),(15,-12),(15,12)]:
        frame=frame.cut(cq.Workplane("XY").center(x,y).circle(1.325).extrude(5).translate((0,0,tower_h-0.2)))
    return frame

parts={
    "SC-IH01_white_QTY01_Common_ThreeAxis_Bearing_Yoke.stl":yoke(),
    "SC-IH02_white_QTY01_Lower_Motor_Bearing_Tower.stl":lower_motor_tower(),
    "SC-IH04_white_QTY04_Guide_Insert_Nominal.stl":guide_insert(0),
}
for name, part in parts.items():
    exporters.export(part,str(OUT/name),tolerance=0.02,angularTolerance=0.1)
for off in P["guide_insert_adjustment_family"]:
    label=("m" if off<0 else "p")+str(abs(off)).replace(".","p") if off else "0p00"
    exporters.export(guide_insert(off),str(OUT/f"SC-IH04_CAL_{label}_Guide_Insert.stl"),tolerance=0.02,angularTolerance=0.1)
