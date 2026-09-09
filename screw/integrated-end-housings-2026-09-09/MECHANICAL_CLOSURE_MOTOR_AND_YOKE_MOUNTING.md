# Mechanical closure — motor location, yoke mounting, and lower drive stack

Date: 2026-09-09
Status: ENGINEERING DIRECTION — motor/coupler dimensions still require physical confirmation before production release

## Motor location decision

**Preferred: motor at the bottom.**

With motor type, direct flexible coupling, two-bearing rotor support, and power system held constant, bottom drive is mechanically preferable.

### Why bottom wins

1. **The lower bearing is already the natural thrust datum.** Rev T uses A03 at the lower stack and A04 only to remove light upper axial play. The rotor weight therefore wants to resolve downward into the lower R4 and the base.
2. **Torque reaction goes into the base**, not into the top of a 48 in tower.
3. **The top remains clear for two-lane discharge geometry.** A direct-drive vertical motor at the top occupies the same central volume where the upper bearing, A04 and D01/D02 receiver development need access.
4. **Lower motor service does not disturb the upper alignment carrier.**
5. **Center of gravity stays lower.**
6. The only material disadvantage — the long two-conductor motor lead from a raised power pod — is removed by routing it in a protected groove between cedar and the rear 2x4.

Do not move the motor to the top merely to shorten wiring. A top motor is only worth revisiting if the design abandons direct axial coupling or the upper discharge architecture changes materially.

## Datum / mounting hierarchy

The machine should not hard-fix both end frames independently and hope the 42 in rods agree.

### Lower end = primary fixed datum

The lower common yoke bolts to the open-portal pedestal through the same four-hole yoke interface.

The pedestal base shoe is positioned during dry-fit and then screwed to the laminated plywood base. The lower pedestal does **not** also attach rigidly to the spine in the baseline design.

Reason: tying the lower end simultaneously to both base and spine overconstrains the alignment and steals basin space. The base is structurally adequate for the lower thrust/torque reaction; the upper support controls the long-span alignment.

Load path:
A01/A03 + rotor weight -> inner-race washer -> lower R4 -> common yoke -> four M4 yoke fasteners -> two pedestal legs -> base shoe -> laminated plywood base.

The yoke remains replaceable independently of the pedestal.

### Upper end = adjustable follower datum

The upper common yoke uses the same four-hole interface but is flipped so the R4 pocket and guide sockets face downward into the screw span.

The upper yoke bolts beneath a two-arm carrier.

The carrier mounts against the **front face of the cedar**, with its main fasteners passing through the cedar and rear 2x4 so the complete wood spine carries the load rather than the 19 mm cedar alone.

Recommended carrier adjustment before final lock:
- vertical: approximately +/-6 mm at the carrier-to-spine slots;
- lateral: approximately +/-1 mm allowed by slot width/washer envelope;
- fore/aft: approximately +/-4 mm at the yoke-to-carrier arm slots.

Assembly alignment procedure:
1. install/freeze the lower pedestal and yoke only after basin/loader dry-fit;
2. leave upper carrier bolts loose;
3. insert the rotor shaft and both guide rods through the lower yoke;
4. slide the upper yoke onto all three rods;
5. let the actual rods establish upper X/Y alignment;
6. hand-rotate the rotor;
7. adjust upper carrier until there is no rod bow, bearing bind or guide spreading;
8. tighten upper yoke-to-carrier fasteners;
9. tighten carrier-to-spine fasteners;
10. recheck several full hand rotations.

This makes the lower assembly the datum and the upper assembly the alignment follower rather than creating two competing datums.

## Upper axial condition

The upper R4 is primarily radial/alignment support.

A04 removes only light axial play. Do **not** clamp A04 hard enough to preload the two R4 bearings against each other. Rotor gravity is reacted at the lower bearing.

## Lower vertical drive stack

Current geometric datum:
- wood base top: Z = 0
- candidate pedestal yoke underside: Z = 47.0 mm
- yoke thickness: 10.0 mm
- yoke top / screw-span face: Z = 57.0 mm
- R4 pocket opens from the top face
- candidate R4 pocket depth: 4.90 mm pending white coupon
- lower bearing bottom plane is therefore approximately Z = 52.10 mm
- coupler must remain below the yoke/pocket and must not touch the bearing

Current measured Screw/Tramway 15 rpm N20 record (2026-08-27, Jeff calipers):
- gearbox width: 11.90 mm
- gearbox height: 9.93 mm
- body length without shaft: 25.32 mm
- length including shaft: 36.07 mm
- shaft protrusion: 10.75 mm

These measurements are valid working inputs but the hardware record itself says to confirm before freezing a pocket depth.

### Coupler stack rule

The actual flexible 3 mm -> 6.35 mm coupler length and usable bore depths are still unknown and must be measured.

Production motor Z is therefore not frozen as one dimension. It is solved from:
- coupler overall length C;
- motor-side insertion Em;
- rotor-side insertion Er;
- deliberate internal shaft-tip air gap G;
- minimum external clearance between coupler and lower yoke.

Required relationship:
**Em + Er + G <= C**

Use a deliberate shaft-tip air gap; neither shaft may bottom in the coupler.

The motor sled provides at least 10 mm downward service travel (18 mm candidate slot length currently reserved), enough to disengage the motor-side shaft without dismantling the rotor.

### Motor cradle topology

Do not depend on a micron-tight printed N20 pocket.

The cradle should:
- positively seat the gearbox face axially on a shoulder;
- support the motor/gearbox in a sized channel;
- use a strap only for anti-rotation/retention;
- provide vertical sled travel;
- keep the motor centerline coaxial with the lower R4;
- allow the motor/coupler to be removed without removing the common yoke.

The final motor-specific channel/strap is gated by remeasurement of the exact 15 rpm N20.

## Fastener accessibility

- lower yoke bolts: heads accessible from the screw side; nuts/captive nut pockets accessible from the open portal below;
- pedestal-to-base screws: straight vertical driver access from above, outside the motor legs;
- upper yoke bolts: accessible from below; nuts accessible above the hanging yoke in the open carrier arms;
- upper carrier spine fasteners: heads accessible from front; washers/nuts accessible behind the 2x4;
- raised power pod must sit low enough that it does not cover the upper-carrier rear nuts.

No hidden one-sided bolted joint is approved.
