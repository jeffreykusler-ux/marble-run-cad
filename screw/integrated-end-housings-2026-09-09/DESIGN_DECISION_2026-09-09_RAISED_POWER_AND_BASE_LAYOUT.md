# Screw Rev-U candidate direction — raised power pod + 12 x 10 base

Date: 2026-09-09
Status: ENGINEERING CANDIDATE — NOT PRINT AUTHORIZED

## New user-directed layout candidate

This is a proposed successor direction to Rev T. Preserve Rev T dimensions and R01 as lineage; do not silently overwrite them.

- Base candidate: **12 in left-right x 10 in rear-front**.
- Spine rear face candidate: **1 in / 25.40 mm forward of the rear base edge**.
- Measured cedar + 2x4 stack: **56.50 mm**, so the cedar front face lands about **81.90 mm from the rear edge**.
- Clear base depth in front of cedar: about **172.10 mm / 6.78 in**.
- Candidate screw centerline for envelope study: **45 mm forward of the cedar face**. This is not frozen; lower dry-fit and basin/loader geometry still control.

## Power location decision

Preferred architecture is to move the **2AA battery holder, rocker switch, and ZX-002 PWM board** off the base and into a separate rear service pod mounted on the 2x4 below the upper yoke.

Do **not** integrate electronics into the precision upper three-axis yoke.

Benefits:
1. Frees the base for the U-shaped marble basin and commercial-track inputs.
2. Rocker and PWM dial sit at hand height instead of near the floor.
3. Controls remain hidden from the normal front view.
4. Only one motor-output wire pair runs down the rear spine to the bottom motor.
5. Electronics changes cannot move the shaft/bearing/guide datums.
6. Lower motor/bearing pedestal becomes much smaller.

Costs:
- Longer low-voltage motor wire run.
- Small amount of mass moved upward. This is judged minor versus the wood/base structure, but remains a stability check.

## Rear service pod candidate

First envelope:
- cover approximately **94 W x 60 D x 98 H mm**
- backplate approximately **86 W x 47 D x 90 H mm**
- battery exits to the **left**
- PWM and rocker operate from the **right**
- mounting is to the rear face of the 2x4, below the upper bearing/yoke assembly

Hardware carried from controlled records:
- battery holder + plug 66.08 mm overall, <=34 W x 18 H
- open-ended battery bay: 70.50 mm useful length
- ZX-002 board 32.47 mm square; solder tails 2.45 mm below board
- PWM shaft axis 7.62 mm above board underside
- PWM board dial edge held 0.40 mm from control-panel inner face
- white PWM hole 8.20 modelled, local wall reduced to 1.60 under the M7 nut
- white rocker hole 20.21 modelled through exactly 3.25 mm snap web
- rocker body envelope 22.86 mm diameter x 25.40 mm deep

### Printability correction made during this pass

Do not cut the rocker and PWM holes directly into a large shell side wall if the shell is printed rear-face-down. Those become horizontal precision openings and create avoidable overhang/roundness risk.

Instead:
- the service cover has a control notch open to its front edge;
- a **separate flat 3.25 mm precision control panel** closes the notch;
- that panel prints flat so rocker and PWM holes are vertical to the bed;
- the battery access opening also runs to the shell's open/front edge, avoiding a bridge over the opening.

This follows CARRY-FORWARD: split precision/support-sensitive features into separately printable parts rather than supporting a large shell.

## Lower end after moving power

Lower assembly becomes a compact mechanical pedestal only:
- vertical N20
- flexible coupler
- lower R4 support
- common three-axis yoke
- two guide-rod sockets
- accessible base screws

The motor/coupler transmit torque only. Downward screw load is reacted through the lower bearing/housing into the wooden base; the motor must not be an axial stop.

## Upper/lower yoke family

Preferred direction remains one common yoke family used twice:
- lower yoke: sockets open upward
- same yoke flipped at the top: sockets open downward
- lower and upper share one bearing/guide datum definition
- replaceable guide-radius inserts preserve physical-fit calibration

## U-shaped basin candidate

The old Rev-T R01 annular basin remains historical/current-Rev-T lineage. Rev-U candidate is a broader U-shaped basin on the 12 x 10 base:
- open toward the spine/screw;
- left and right wings slope inward toward the two screw starts;
- front bridge provides visible reservoir volume;
- compact central notch clears the motor pedestal and helix;
- modular commercial-track interface pad at each outer wing.

Do not hard-code a DSHMIXIA/JOYIN connector into the basin body. The commercial connector winner is not frozen. Use replaceable adapter plates so the basin does not need reprinting when that interface is settled.

## Print gate

Before printing a large new yoke, use a small **white R4 pocket coupon** in the same flat/vertical-pocket orientation. Current coupon candidates are 15.80 / 15.96 / 16.12 mm model diameters at 4.90 mm depth. Pick by real bearing press test, not calipers.

