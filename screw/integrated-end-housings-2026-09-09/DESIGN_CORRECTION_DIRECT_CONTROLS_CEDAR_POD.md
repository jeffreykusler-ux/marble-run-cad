# Design correction — direct controls, cedar-mounted sculpted pod, hidden spine wiring

Date: 2026-09-09
Status: ENGINEERING DIRECTION — exact electronics geometry still gated by hardware confirmation

## User corrections carried forward

1. Do not use a separate inset control panel. The rocker and PWM are direct circular penetrations through the pod shell, consistent with the successful Belt/Ferris approach.
2. Do not repeat the boxy Ferris power-pod proportions.
3. The power pod should visually relate to the cedar width and mount into the back of the cedar, not merely hang from the rear face of the 2x4.
4. Do not leave a vulnerable exposed wire span down the machine.
5. Continue common mirrored yoke + lower motor-cradle development. N20 motor-specific fit remains provisional until the actual motor is remeasured.

## Preferred high-power architecture

Keep battery + rocker + PWM high on the rear of the spine because it preserves the 12 x 10 base for the U-shaped marble reservoir and puts controls at hand height.

The pod remains separate from the precision upper yoke.

### Pod form

Candidate envelope is approximately 122 mm wide x 92 mm high x 42 mm deep behind the rear face of the 2x4.

The body is a rounded/tapered shield rather than a rectangular project box. It bridges around the rear 2x4 and uses side cheeks that reach forward beside the 2x4 to the exposed cedar shoulders. Mounting screws enter the cedar shoulders.

The 122 mm width is:
- wider than the 88.9 mm rear 2x4,
- narrower than the 139.7 mm cedar,
- proportioned to read as part of the whole spine rather than an accessory stuck to the 2x4.

Rocker and PWM holes are cut directly into the rear shell surface. Exact hole values will be rechecked against the user's proven machine-specific hardware before print release.

Battery exits laterally from the pod; exact drawer/door geometry is held until the successful battery-tray dimensions are reintroduced.

## Hidden motor wiring

Preferred wire protection is inside the wood spine rather than an exposed printed raceway:

- route a shallow vertical groove in the rear face of the cedar where it will be covered by the centered 2x4;
- upper entry is hidden behind/below the power pod;
- lower exit is hidden near the motor;
- provide strain relief at both ends;
- keep the groove clear of tower fasteners;
- reassemble the reversible 2x4 over the groove.

This yields no exposed long wire span and mechanically protects the two-conductor motor lead.

If the wood groove is rejected later, a low-profile printed cedar-wing chase is the fallback, not loose clips alone.

## Lower load path / motor cradle direction

The lower support is an open portal:
- common three-axis yoke at top,
- two side legs transfer bearing load directly to a base shoe,
- N20 hangs between the legs,
- motor sled has vertical service travel so the motor can drop away from the coupler,
- flexible coupler transmits torque only,
- lower R4 bearing is the axial support.

Motor-specific clamp/insert remains modular so a motor remeasurement changes only the insert/sled details, not the bearing yoke or pedestal.

## Common yoke direction

One yoke geometry is used lower and upper, flipped so all three sockets face the screw span:
- center R4 bearing node,
- left guide-rod node,
- right guide-rod node,
- shallow connecting webs,
- replaceable guide bushings preserve radius calibration.

Outer guide-bushing stems are keyed, but their visible flange is round so the finished yoke reads as three circular mechanical nodes rather than rectangular pockets.

## Current print gate

Do not print the large yoke until the white R4 pocket coupon winner is known.
Do not print the motor-specific sled/clamp until the actual N20 is remeasured.
Do not print the upper carrier until its cosmetic form is refined.
