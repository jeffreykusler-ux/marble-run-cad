# Service-access and discharge integration closure

Date: 2026-09-09
Status: ENGINEERING DIRECTION — exact coupler set-screw axial positions still require physical confirmation

## Coupler assembly/service sequence

Preferred assembly sequence follows the user's proposed cartridge logic:

1. On the bench, install the 15 x 20 mm uxcell coupler onto the N20 output shaft to a controlled engagement depth.
2. Tighten the motor-side coupler set screw while the motor/coupler is outside the machine.
3. Insert the **motor + coupler as one cartridge** into the vertically sliding motor cradle.
4. Leave the cradle vertically loose within its service range.
5. Install the lower R4 bearing/yoke.
6. Lower the 6.35 mm rotor shaft through the bearing into the upper bore of the coupler.
7. Rotate the rotor/coupler so the rotor-side set screw faces the service opening.
8. Tighten the rotor-side set screw through the open portal.
9. Set motor/cradle Z so the two shafts have a deliberate internal air gap and neither shaft bottoms in the coupler.
10. Lock the motor cradle.
11. Hand-rotate and verify that the coupler has full radial/axial freedom and the motor carries no rotor weight.
12. Fit a removable safety guard only after both set screws and alignment are confirmed.

For service, remove the safety guard, loosen the rotor-side screw, drop the motor/coupler cartridge at least 10 mm, and remove it. The motor-side screw is then fully exposed. The pedestal must also permit in-place tool access to both coupler screw zones where practical.

## Coupler tool-access envelope

Do not enclose the 20 mm coupler inside a narrow tube.

Reserve an open service bay around the complete coupling:
- coupler OD: 15 mm SPEC
- free-rotation cylinder: >=17 mm
- open radial tool-access width across portal: >=30 mm
- open vertical service window: cover the complete 20 mm coupler plus at least 5 mm above and below
- no pedestal rib, basin wall, loader, or guard may permanently occupy the radial hex-key approach zone
- removable guard must come off without moving motor or yoke

Until exact set-screw positions are measured, design for the screw to occur anywhere in either end region rather than creating a tiny targeted hole.

## Basin and lower service relationship

The new U-basin is **not structural** and must not trap the motor/coupler.

The lower fixed datum remains the pedestal bolted to the wood base.

Basin requirements:
- wraps around the lower pedestal but does not fasten through the pedestal/yoke interface;
- provides a central pedestal clearance pocket larger than the lower structural envelope;
- does not cover pedestal-to-base screws;
- remains removable independently for deep motor/coupler service;
- initial rotor/coupler assembly occurs before final basin installation;
- a normal Allen-key approach to the rotor-side coupler screw should remain possible with the basin installed if practical; if not, basin removal must require only its own accessible retainers and must not disturb the mechanical datum.

Current base candidate remains 12 in left-right x 10 in rear-front.

The basin owns the remaining base area outside the central pedestal keepout. Marble-entry adapters belong at the outer ends of the two U wings. Commercial connectors remain replaceable adapter modules; do not hard-code an unfrozen DSHMIXIA/JOYIN interface into the large basin.

## Loading keepout

The lower yoke/pedestal design must reserve the screw-facing region for:
- first A01 flight;
- two guide rods;
- two tangential loader noses;
- accepted-marble path from each basin wing into its screw start.

Do not extend motor-pedestal ribs, fastener bosses, or coupler guards outward into the left/right loader sectors. Keep the pedestal narrow in X above the base shoe and place service structure below the marble-loading elevation wherever possible.

Final loader placement is physically controlled by actual first-flight geometry and real marbles, so basin-to-loader interfaces remain adjustable/removable.

## Upper discharge integration

The actual Rev-T D01/D02 STL meshes were inspected:
- each receiver envelope is approximately 32.0 mm wide x 119.9 mm long x 32.2 mm deep;
- they are substantial downhill receiver/chute modules, not small lips.

The upper assembly therefore must reserve discharge volume and provide a mounting strategy.

### Architecture

Do **not** make D01/D02 part of the bearing yoke.

Instead, develop a **removable discharge bridge / left-right accessory wings** attached to the upper carrier/yoke assembly.

Requirements:
- discharge support follows the final upper rotor/guide pose;
- D01 and D02 remain separate removable modules;
- each side has independent position adjustment;
- discharge loads do not distort the R4 pocket or guide-rod centers;
- central top remains open for shaft insertion, F02/R4 service, and A04 access;
- no discharge bracket blocks the three rod sockets or yoke fasteners;
- both receivers remain downhill after release and can be positioned only after the complete rotor turns freely.

Preferred datum relationship:
- common upper yoke establishes shaft + guide geometry;
- discharge bridge references the upper yoke/carrier pose;
- left/right receiver brackets use slots for final calibration to the actual release point;
- outgoing commercial track connects downstream of the receiver, not directly to the bearing yoke.

## Assembly order at top

1. align and lock lower yoke/pedestal;
2. insert shaft and guide rods;
3. slide/align upper yoke and carrier;
4. prove free hand rotation;
5. establish A04 light axial control;
6. attach discharge bridge/wings;
7. fit D01/D02 or their Rev-U successors;
8. roll-test each lane;
9. only then establish outgoing-track adapters.

This preserves the controlled Rev-T rule that discharge is located after the rotor/guide system is free-running.
