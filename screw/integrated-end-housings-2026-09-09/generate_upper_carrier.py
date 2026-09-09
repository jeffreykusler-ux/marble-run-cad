import cadquery as cq
from cadquery import exporters
from pathlib import Path

OUT = Path("generated")
OUT.mkdir(parents=True, exist_ok=True)

def union_all(parts):
    out=parts[0]
    for p in parts[1:]:
        out=out.union(p)
    return out

def upper_spine_carrier():
    back=cq.Workplane("XY").box(112.0,6.0,70.0,centered=(True,False,False))
    shelf=cq.Workplane("XY").box(92.0,72.0,7.0,centered=(True,False,False)).translate((0,6.0,31.0))
    brace_l=cq.Workplane("XY").box(8.0,58.0,30.0,centered=(True,False,False)).translate((-38,6,4))
    brace_r=cq.Workplane("XY").box(8.0,58.0,30.0,centered=(True,False,False)).translate((38,6,4))
    part=union_all([back,shelf,brace_l,brace_r])
    for x in (-38,38):
        for zc in (18,52):
            for z in (zc-6,zc+6):
                part=part.cut(cq.Workplane("XZ").center(x,z).circle(2.4).extrude(6.2))
            part=part.cut(cq.Workplane("XZ").center(x,zc).rect(4.8,12.0).extrude(6.2))
    z0=31.0
    for x in (-15.0,15.0):
        for yy in (31.0,55.0):
            part=part.cut(cq.Workplane("XY").center(x,yy).circle(1.675).extrude(7.2).translate((0,0,z0)))
        part=part.cut(cq.Workplane("XY").center(x,43.0).rect(3.35,24.0).extrude(7.2).translate((0,0,z0)))
    return part

exporters.export(
    upper_spine_carrier(),
    str(OUT/"SC-IH03_white_QTY01_Upper_Adjustable_Spine_Carrier.stl"),
    tolerance=0.02,
    angularTolerance=0.1
)
