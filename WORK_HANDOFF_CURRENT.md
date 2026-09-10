# WORK_HANDOFF_CURRENT.md

**Project:** Marble Run — Archimedes Screw Rev-U development  
**Prepared:** 2026-09-09  
**Purpose:** Recovery handoff for ChatGPT Work / local CAD continuation  
**Repository:** `jeffreykusler-ux/marble-run-cad`  
**Development branch to continue:** `screw/integrated-end-housings-2026-09-09`  
**Existing draft PR:** #2 — Screw: integrated end-housing engineering candidate

> **READ THIS FILE FIRST.**
>
> This file is a recovery/control document. It does **not** itself release geometry to production.
> The finalized Marble Run Knowledge Pack remains the governing engineering baseline.
> Current physical/bench evidence and the newest dated controlled record beat older branch notes.
> Preserve conflicting values as lineage; do not silently reconcile them.

---

# 1. USER'S CURRENT OBJECTIVE

Take the Archimedes Screw design as far as practical toward a **single shop-handoff ZIP** that could be sent to a competent fabrication/3D-print shop to finalize and build.

The requested final package should include, at minimum:

- build sheets;
- overall plans;
- CAD source;
- STLs that have passed the design gates;
- STEP files where useful;
- part definitions and filenames;
- dimensions and datum chains;
- base/spine/wood cut plans;
- hardware/shop lists;
- confirmed measurements vs. unconfirmed measurements;
- assembly order;
- service/disassembly order;
- print orientations and print notes;
- fit-test coupons where required;
- unknowns still requiring physical measurement;
- pitfalls and likely failure modes;
- design-gate/audit results;
- exclusions list for candidate STLs that failed gates or remain unproven;
- clear status labels: CURRENT / CANDIDATE / HOLD / PHYSICAL TEST REQUIRED;
- one final ZIP containing the controlled handoff.

The user explicitly asked to spend substantial effort getting this package as far as possible, not merely discuss concepts.

**Do not include an STL in the final release folder unless it has passed the applicable automated geometry/design gates.**
Passing mesh checks does **not** mean a physical-fit gate is passed; distinguish those states.

---

# 2. GLOBAL AUTHORITY / ENGINEERING RULES

Use the finalized September 8, 2026 Marble Run Knowledge Pack as the governing project baseline.

Authority order:

1. current physical/bench result;
2. newest dated controlled/current record;
3. newest dated machine-specific record and CARRY-FORWARD;
4. current revision master/source;
5. older handoff/release/history.

Do not silently normalize conflicting dimensions.

Mandatory CARRY-FORWARD rules that matter particularly here:

- print production parts at **100% scale**;
- fix fit in CAD, not slicer scaling;
- coupon first before large fit-sensitive prints;
- same-color, same-orientation fit proof;
- verify built solids/meshes, not source constants;
- provide driver access to both ends of bolted joints;
- model actual tool access volume where practical;
- check fastener stack depth and insertion sequence;
- inspect unsupported spans in print orientation;
- split large unsupported geometry into keyed/pegged pieces where practical;
- use wood for simple structure and plastic for precision/interface geometry;
- enumerate all jobs a part performs before deleting/redesigning it;
- preserve assembly/service access;
- perform world-pose marble-envelope/interference checks;
- actual ball roll/drop tests remain required before final commissioning;
- folders/revision letters alone do not prove currency.

P1S baseline:
- Bambu P1S Combo;
- 0.4 mm nozzle;
- PLA with door open / lid off;
- approved structural process differs from stock Standard only by:
  - 3 walls;
  - gyroid infill;
  - Arachne wall generator;
- no unapproved temperature/fan/flow/speed changes;
- deliver STL, not 3MF, unless specifically justified;
- production print requires a fresh pre-print briefing/approval.

---

# 3. CURRENT SCREW BASELINE FROM REV T

Rev T remains the controlled production master until a later revision is explicitly promoted.

Core controlled facts:

- base historically: 12 x 10 x ~1 in laminated plywood;
- current Rev-U candidate orientation is **12 in LEFT-RIGHT x 10 in FRONT-BACK**;
- cedar face: 48 in;
- rear 2x4: 46 in;
- cedar and 2x4 bottoms flush;
- 1/4 in / 6.35 mm rotor shaft;
- two 1/4 in / 6.35 mm stationary guide rods;
- two-start A01 screw sections;
- final Rev-T machine uses six matching A01 sections;
- first seam/phase fit must be proven before committing the remaining sections;
- two R4 bearings support rotor independently of motor coupler;
- motor coupler transmits torque only;
- A03 controls lower screw stack;
- A04 removes only light upper axial play;
- do not preload both bearings hard against each other;
- actual Rev-T D01/D02 discharge pieces exist and are substantial;
- loader and discharge placement is physically controlled by the actual assembled rotor/guide geometry, not an old ruler-only hole pattern.

Actual Rev-T A01 master was recovered from Google Drive:
`CURRENT - Screw Rev T - Labeled STL Package.zip`

A single first-test A01 copy was verified byte-for-byte against the controlled master earlier in this conversation.

Known SHA-256 for the exact A01 first-test STL:
`71ec31bca94b64b01cae2e94d566fdde81944926c8b629e2dbbfc3f7356bc2eb`

Do not regenerate the two-start helix from scratch unless absolutely necessary. The exact Rev-T mesh is the current screw-section authority.

---

# 4. VERY IMPORTANT DECISION LINEAGE — MOTOR LOCATION

The branch contains earlier notes preferring a **bottom coaxial motor**.

Those notes are **superseded as the current Rev-U direction** after a later geometry study.

## Earlier state — historical lineage

Earlier design logic preferred:
- lower R4 as thrust datum;
- bottom coaxial N20;
- coupler directly below lower bearing;
- motor + coupler cartridge;
- raised electronics pod;
- hidden wiring in spine.

This was mechanically clean but created a critical problem:

**The direct coaxial motor/coupler stack forced the lower screw datum too high.**

With:
- N20 body ~25.32 mm;
- N20 shaft protrusion ~10.75 mm;
- uxcell coupler 20 mm long;
- required bearing/yoke structure;

the screw entry region was being pushed roughly 50–60+ mm above the wooden base before providing the basin floor / loader approach.

That allowed the drive to dictate the marble-entry height, which is the wrong priority.

## Current preferred direction — TOP DIRECT DRIVE

The current Rev-U architecture study therefore **flipped to top direct drive**.

This decision is newer than the earlier bottom-motor notes and should control unless a later gate proves it unworkable.

Why top drive now wins:

1. lower yoke can sit almost directly on the wood base;
2. the screw/first flight can start much lower;
3. the basin can remain low, broad, and visually substantial;
4. marble loading geometry sets the lower datum rather than motor packaging;
5. existing 3 mm -> 6.35 mm uxcell coupler remains usable;
6. upper ~5.6 in of cedar above the guide-rod span appears sufficient for motor + coupler + service travel + cover;
7. power pod / motor / wiring can be integrated at the upper rear with short wiring;
8. a full removable upper cover can expose N20, wiring, coupler, and both coupler set-screw regions.

Top-drive costs to manage:
- top assembly becomes more crowded;
- discharge must coexist with motor/coupler;
- motor torque reacts into the upper spine;
- service must not disturb yoke alignment;
- upper structure must be reinforced and well fastened.

**Do not revert to bottom drive just because older branch docs say “motor at bottom.”**
Re-evaluate only if the current top-drive geometry fails a gate.

---

# 5. TOP-DRIVE SERVICE REQUIREMENT

The user explicitly requires:

> The removable cover should give access to the full assembly including both ends of the coupler and N20 and wiring.

Design accordingly.

Preferred service architecture:

- N20 and coupler form a removable top drive cartridge;
- cover is cosmetic/protective, not a structural bearing member;
- when cover is removed, the user can see/reach:
  - N20;
  - motor wires;
  - motor terminals / soldered connections;
  - motor-side coupler set screw;
  - rotor-side coupler set screw;
  - relevant shaft engagement areas;
  - cradle fasteners;
  - strain relief;
- the cover must not be required to support the rotor, guide rods, discharge, or motor alignment;
- cover removal must not require disturbing yoke/spine alignment;
- the coupler needs a broad service window, not tiny guessed holes aimed at set-screw positions.

Preferred assembly sequence concept at top:

1. install/alignment of lower yoke and rods;
2. align/fix upper yoke;
3. insert rotor shaft through upper bearing;
4. install motor + coupler cartridge in its cradle;
5. slide/couple shaft cleanly;
6. orient coupler to access both set screws;
7. tighten motor-side and rotor-side screws;
8. preserve deliberate shaft-end clearance so coupler is not an axial stop;
9. hand-rotate;
10. install removable cover after verification.

Exact sequence may change after final CAD, but both coupler ends must remain practically serviceable.

---

# 6. COUPLER HARDWARE

User supplied:
uxcell 4-piece flexible coupling, Amazon ASIN `B0G48ZZ6ZK`

Matching published family specification:
- 3.00 mm motor-side bore;
- 6.35 mm rotor-side bore;
- 15.00 mm outside diameter;
- 20.00 mm overall length;
- aluminum flexible/helical-beam style.

Treat:
- 15 x 20 outer envelope = SPEC / working hardware definition;
- exact usable bore depth at each end = PHYSICAL CONFIRMATION REQUIRED;
- exact internal stop/web geometry = PHYSICAL CONFIRMATION REQUIRED;
- exact set-screw axial positions = PHYSICAL CONFIRMATION REQUIRED if needed.

Do not let printed structure touch/support the rotating coupling.

Reserve at least ~17 mm diameter free-rotation cylinder around a 15 mm OD coupler, preferably more where service allows.

Because exact set-screw positions remain unmeasured, use a broad open service zone.

---

# 7. N20 HARDWARE

Working measured record for the Screw/Tramway 15 RPM N20 from 2026-08-27:
- gearbox width: 11.90 mm;
- gearbox height: 9.93 mm;
- body length without shaft: 25.32 mm;
- length including shaft: 36.07 mm;
- shaft protrusion: 10.75 mm.

**Re-measure the exact motor physically before freezing a tight cradle pocket.**

Preferred motor-cradle rules:
- motor-specific fit should be modular/replaceable;
- cradle should not depend on a micron-tight printed N20 cavity;
- provide positive axial seating and anti-rotation retention;
- motor service must not disturb upper bearing/yoke alignment;
- allow cartridge removal after cover removal;
- do not let motor carry rotor axial load.

---

# 8. BEARINGS — USER ALLOWS SEVERAL

User explicitly said:

> We can use several bearings in this unit.

Do not artificially constrain the redesign to only the two historical R4 bearings if additional bearings materially improve:
- motor/coupler cartridge alignment;
- radial shaft control;
- thrust isolation;
- serviceability;
- stiffness.

However:
- avoid overconstraining a long shaft with multiple misaligned rigid radial bearings;
- distinguish **rotor support bearings** from **drive-cartridge alignment bearings**;
- if adding a third/fourth bearing, define its exact mechanical job;
- do not preload multiple bearings unintentionally;
- keep the actual axial load path explicit.

Current R4 physical evidence:
- measured R4 OD: 15.86 mm;
- measured width: 4.99 mm;
- a later audit proposed pocket 15.96 mm diameter x 4.90 mm depth;
- that correction had not yet been promoted into a new controlled master.

A white R4 coupon family was generated:
- 15.80;
- 15.96;
- 16.12 mm;
all at 4.90 mm depth.

This remains a **physical test gate** before freezing a large yoke pocket.

Guide-rod white coupon family was also generated:
- 6.50;
- 6.65;
- 6.80 mm modeled bores.

Again: physical slip-fit winner required before freezing large yokes.

---

# 9. COMMON YOKE CONCEPT

Current preferred visual/mechanical concept:

**one common yoke geometry used at lower and upper ends, flipped.**

It visually reads as:
- round guide node;
- round central bearing node;
- round guide node;
- shallow structural webs.

The same CAD definition should control:
- left guide-rod center;
- shaft/bearing center;
- right guide-rod center.

Replaceable keyed guide inserts / bushings should permit guide-radius calibration without reprinting the full yoke.

Working provisional guide radius from Rev-T G02 geometry:
~33.25 mm from shaft center to each guide rod.

Candidate guide-radius offsets generated/considered:
- -1.50 mm;
- -0.75 mm;
- nominal;
- +0.75 mm;
- +1.50 mm.

Do not freeze this radius purely from historical geometry if the real A01 / marbles / guide rods indicate otherwise.

---

# 10. LOWER END — CURRENT TOP-DRIVE DIRECTION

Because the motor moved to the top, the lower end should become very low and mechanically simple.

Current study result:

- common yoke can sit nearly directly on the wooden base;
- candidate yoke height around 10–12 mm;
- with a conservative A03 stack above it, first A01 entry region may begin around ~32 mm / ~1.26 in above the base rather than ~64 mm / ~2.52 in.

This is the **core reason for top drive**.

Lower-yoke jobs:
- carry lower R4 / thrust datum;
- locate two guide rods;
- establish the fixed lower three-axis datum;
- transfer rotor weight into base;
- remain narrow enough not to consume loader sectors;
- allow basin to wrap around it.

Lower end should be fixed to the wooden base, not redundantly rigidly tied to both base and spine.

The basin is not the structural support.

---

# 11. BASIN / MARBLE ENTRY — CRITICAL

The user explicitly emphasized:

> The marbles have to enter the base of the screw and we can only make the screw as low as whatever we put under the axle and the basin has to be above that.

This requirement controls the lower architecture.

## Base orientation

Current candidate:
- 12 in wide LEFT-RIGHT;
- 10 in deep FRONT-BACK;
- spine rear face approximately 1 in forward of rear edge;
- cedar + rear 2x4 stack measured around 56.50 mm;
- cedar front face then approximately 81.90 mm from rear edge;
- about 172.10 mm / 6.78 in usable depth remains in front of cedar.

Screw should remain relatively close to cedar, not projected unnecessarily far forward.

## Basin concept

Preferred Rev-U basin is a **U-shaped reservoir**, not necessarily the historical Rev-T annular R01.

Concept:
- left wing;
- right wing;
- front bridge;
- slopes/valleys toward the two screw starts;
- open around a compact central lower yoke;
- broad enough to look proportionate to a 48 in machine;
- modular commercial-track entry adapters at outer wing starts;
- commercial connector geometry is replaceable, not molded permanently into the large basin body.

The user wants marbles to be able to enter the U-shaped basin from either side and roll inward toward the screw.

The basin should be low and substantial, not perched high on a drive pedestal.

## Modular / printable construction

User explicitly approved:
> We can use pegs and holes to join pieces instead of single large unsupported pieces.

Current interrupted work had already moved toward:
- four modular open-top basin pieces;
- left wing;
- right wing;
- front bridge split into two halves;
- vertical drop-pin / peg-and-hole joints;
- flat-printable undersides;
- shallow sloped floors;
- avoiding a single 11+ in unsupported part.

Intermediate local audit reportedly showed:
- left/right wings about 78 x 83 mm;
- front bridge split;
- each candidate under ~150 mm longest print dimension;
- meshes watertight / connected at that stage.

**Those local files may not exist in the new Work environment. Recreate them from the design intent and re-run gates before release.**

Do not rely on memory that they passed; regenerate and audit.

---

# 12. LOADER KEEPOUT

Reserve real geometry for:
- first A01 flight;
- lower A03;
- two guide rods;
- two tangential loader noses;
- accepted marble envelope 13.5–14.5 mm;
- left and right basin-to-loader roll paths.

Pedestal/yoke ribs, fastener bosses, basin pins, and guards must not occupy the left/right loading sectors.

Loader position must be adjustable or at least delayed until real A01/guide geometry is assembled.

Do not drill/freeze loader positions from old templates.

---

# 13. COMMERCIAL TRACK INPUT

There is no universal frozen DSHMIXIA/JOYIN connector winner.

Do not invent one.

Each basin wing should therefore have a replaceable adapter interface:
- flat/keyed landing;
- screw or peg retention;
- small replaceable adapter part;
- basin itself remains unchanged if connector geometry changes.

Preserve historical connector measurements by identity; do not merge them.

---

# 14. UPPER YOKE / SPINE MOUNT

Earlier work established the right alignment philosophy:

- lower end = primary fixed datum;
- upper end = adjustable follower.

Continue this principle under top drive.

The upper yoke should reference the actual shaft + guide rods, not a theoretical ruler dimension.

Preferred carrier:
- attaches structurally to the wood spine;
- uses cedar + rear 2x4 together where possible;
- allows vertical / fore-aft adjustment during alignment;
- once aligned, tightens without moving yoke centers;
- does not block bearing-cap/A04/coupler access.

Earlier candidate ranges were roughly:
- vertical ±6 mm;
- fore/aft ±4 mm;
- small lateral compliance/slot allowance.

These are CANDIDATE values, not sacred.

The upper carrier must now also coexist with:
- top motor cartridge;
- removable service cover;
- discharge-wing supports;
- upper R4/A04;
- potentially additional drive-support bearings.

---

# 15. DISCHARGE — MUST BE DESIGNED INTO UPPER UNIT

User asked whether upper unit must hold any part of discharge.

Answer: **yes, contemplate it now.**

Actual Rev-T D01/D02 meshes were inspected:
- each roughly 32 mm wide;
- ~119.9 mm long;
- ~32.2 mm deep.

They are substantial downhill receivers, not tiny lips.

Preferred architecture:

- common upper yoke remains a precision bearing/guide part;
- do **not** merge D01/D02 into the yoke;
- upper carrier provides independent left/right discharge-wing interfaces;
- discharge wings follow the final upper yoke pose;
- D01/D02 or Rev-U successors mount to those wings;
- each side has independent adjustment;
- central zone remains open for:
  - shaft insertion/removal;
  - upper R4;
  - F02/cap access;
  - A04;
  - coupler access;
  - motor cartridge;
- discharge loads must not distort the bearing pocket or guide centers;
- receivers remain downhill;
- outgoing track is established only after real roll tests.

Preferred order:
1. lower datum;
2. rods/shaft;
3. upper-yoke alignment;
4. free hand rotation;
5. A04 light axial control;
6. top drive installation/alignment;
7. discharge wings;
8. D01/D02 or successors;
9. real marble roll test;
10. outgoing track adapters.

---

# 16. POWER / SWITCH / PWM DIRECTION

User rejected the inset control-panel concept.

Do **not** use a separate inset control panel.

Preferred control style:
- direct circular shell penetrations;
- rocker snaps directly into shell;
- PWM bushing/shaft mounts directly through shell;
- use successful machine-specific hole/wall values once confirmed.

User also disliked the Ferris power pod:
- too boxy;
- too square;
- wrong proportions;
- visually hung off the 2x4.

If a separate upper power/service enclosure remains part of top-drive design:
- visually relate it to the cedar width, not just the 2x4;
- sculpt/taper/round it;
- mount into/through the cedar/spine appropriately;
- do not repeat a rectangular project box;
- controls should be accessible but visually discreet.

Because top drive now places motor near power, wiring may remain compact and protected.

---

# 17. REMOVABLE COVER — REQUIRED

This requirement is explicit and must survive redesign.

The upper service cover should be removable independently and expose:

- entire N20 body;
- motor wiring;
- coupler;
- both coupler set-screw zones;
- shaft engagement;
- motor cradle;
- any additional drive bearing(s);
- strain relief / wiring service area.

The cover should:
- not be structural;
- not set bearing alignment;
- not carry discharge loads;
- not require removal of yoke or discharge calibration to access motor/coupler;
- print without hidden large unsupported roofs.

Earlier local work found a one-piece service cowl had unacceptable unsupported regions in intended print orientation.

**Do not include that STL in the release.**

Redesign as:
- split shells;
- keyed/pegged panels;
- open-backed sculpted halves;
- or another support-safe modular arrangement.

Use pegs/holes where helpful.

---

# 18. INTERRUPTED SHOP-PACKAGE WORK — RECOVERY NOTES

Immediately before Work/local handoff failed, the following progress had occurred in the chat environment:

1. shop-handoff directory structure had been started locally;
2. revised top-drive CAD concepts were being generated;
3. modular basin geometry had been created and iterated;
4. a bridge wedge geometry had been updated for printability;
5. service-shell candidate had been reviewed for overhang risk;
6. STL candidates had been audited;
7. automated design gates were explicitly separated from physical fit gates;
8. several candidate meshes reportedly passed:
   - watertight;
   - one connected body;
   - P1S build envelope;
9. two candidate items were explicitly rejected from the intended release set:
   - one-piece service cowl;
   - first battery drawer;
   because they had large unsupported regions in intended print geometry;
10. basin direction was changed toward modular open-top pieces with drop pins.

The local interrupted files are **not authoritative unless recovered in the new Work environment and re-audited**.

If they are absent, recreate them from this handoff rather than assuming they exist.

---

# 19. REQUIRED DESIGN GATES BEFORE AN STL ENTERS RELEASE

Create an explicit audit report for every release STL.

Minimum automated gates:

## Mesh integrity
- file exports successfully;
- watertight;
- expected connected-body count;
- no accidental floating bodies;
- no non-manifold edges if detectable;
- positive volume;
- expected bounding box;
- within P1S build envelope;
- reasonable triangle count;
- no corrupted normals / invalid faces.

## Dimensional / functional
- key centers match source parameters;
- bearing pocket dimension is as intended;
- guide-rod centers match the yoke datum;
- fastener pitch correct;
- mating peg/hole geometry correct;
- required clearance envelopes exist;
- marble envelope does not collide with structural ribs in modeled path;
- discharge keepouts respected;
- coupler free-rotation/service envelope respected;
- tool access volume checked where practical.

## Printability
- intended orientation stated;
- first-layer footprint acceptable;
- large unsupported roofs/spans identified;
- unsupported spans >15 mm require redesign or explicit approved support strategy;
- large shells should be split if that materially reduces supports/risk;
- slender/curl-risk pieces flagged for brim where appropriate;
- precision bores oriented consistently with proving coupons where possible;
- no hidden bridge over a service opening merely for cosmetics.

## Assembly/service
- both ends of bolted joints accessible;
- actual driver/hex-key insertion path exists;
- insertion order works;
- removable cover can come off without disturbing alignment;
- motor/coupler service sequence works;
- basin can install/remove without disturbing lower datum;
- discharge pieces can install after free-rotation check;
- no cross-bolt intrudes into marble path.

## Status gate
Each STL must be marked one of:
- RELEASE CANDIDATE — AUTOMATED GATES PASS;
- HOLD — PHYSICAL FIT REQUIRED;
- EXCLUDED — FAILED DESIGN GATE;
- HISTORICAL / REFERENCE ONLY.

Do not place EXCLUDED parts in the shop's print-ready STL folder.

---

# 20. PHYSICAL GATES THAT CANNOT BE FAKED

Record these clearly in the final package.

Still requiring actual physical proof:

- R4 pocket coupon winner;
- 1/4 in guide-rod slip-fit coupon winner;
- exact N20 remeasurement;
- exact coupler usable bore depths;
- exact coupler set-screw positions if final service geometry depends on them;
- first A01 marble-motion test;
- two-A01 seam/phase test before full six-section print;
- final guide radius;
- actual basin-to-loader transfer;
- actual marble roll path;
- actual upper discharge release into D01/D02 or Rev-U receiver;
- commercial-track adapter winner;
- final top-drive hand-rotation and powered test;
- stability of 12 x 10 base with upper drive mass.

Do not represent these as “passed” merely because CAD looks correct.

---

# 21. WOOD / SHOP PLAN BASELINE

Current candidate wood structure:

- laminated plywood base: 12 in wide x 10 in deep x ~1 in;
- cedar face: 1x6 x 48 in;
- rear 2x4: 46 in;
- cedar and 2x4 bottoms flush;
- rear 2x4 centered left-right behind cedar;
- candidate spine rear face ~1 in forward of base rear edge;
- final tower-to-base relationship remains subject to real lower-yoke/basin dry-fit;
- do not notch wood to force printed geometry.

If routing/wire channels are needed, define:
- exact face;
- depth;
- width;
- start/stop;
- fastener keepouts;
- strain relief;
- whether the reversible cedar/2x4 joint covers the channel.

Top-drive may reduce need for a full-length motor-wire channel relative to earlier high-power/bottom-motor concept.

---

# 22. DELIVERABLE FOLDER STRUCTURE REQUEST

A good final ZIP structure would be:

```text
SCREW-REV-U-SHOP-HANDOFF/
├── 00-READ-ME-FIRST.md
├── 01-CURRENT-DESIGN-BASIS.md
├── 02-CHANGE-LINEAGE-REV-T-TO-REV-U.md
├── 03-OPEN-UNKNOWNS-AND-PHYSICAL-GATES.md
├── 04-BUILD-SHEET.md
├── 05-ASSEMBLY-ORDER.md
├── 06-SERVICE-AND-DISASSEMBLY.md
├── 07-SHOP-CUT-LIST.md
├── 08-HARDWARE-AND-SHOPPING-LIST.md
├── 09-PRINT-RUNBOOK.md
├── 10-DESIGN-GATE-REPORT.md
├── 11-PART-MANIFEST.csv
├── 12-DIMENSION-REGISTER.csv
├── 13-FAILURE-MODES-AND-PITFALLS.md
├── SOURCE/
│   ├── CadQuery/
│   ├── parameters/
│   └── audits/
├── STEP/
├── STL-RELEASE-CANDIDATES/
├── STL-FIT-COUPONS/
├── STL-HOLD-PHYSICAL-TEST/
├── REFERENCE-REV-T/
│   └── exact-A01-reference-or-pointer
├── DRAWINGS/
│   ├── overall/
│   ├── lower-end/
│   ├── upper-drive/
│   ├── basin/
│   └── discharge/
└── EXCLUDED-CANDIDATES/
    └── README explaining why excluded
```

The final root README must make it impossible for a shop to confuse:
- release candidates;
- physical-test holds;
- historical Rev-T reference;
- excluded failed candidates.

---

# 23. GITHUB / BRANCHING INSTRUCTIONS FOR WORK

Start from:
`screw/integrated-end-housings-2026-09-09`

Do not silently treat every note on that branch as current. In particular:
- older “motor at bottom” decisions are historical lineage;
- this handoff's newer **top direct-drive** direction controls unless later geometry disproves it.

Recommended next branch:
`screw/rev-u-shop-handoff-top-drive`

Keep:
- source;
- parameters;
- audit scripts;
- markdown decision records;
- manifests;
under Git.

Large binary STL/STEP outputs can be built locally for the final ZIP; commit only when appropriate.

Do not merge Rev-U to `main` merely because the shop package exists.
Bench verification is still required.

---

# 24. WHAT TO DO NEXT — EXECUTION ORDER

Work should continue without stopping after each substep.

## Phase A — Recover / re-ground
1. checkout the development branch;
2. read all Screw branch files;
3. identify which intermediate motor-bottom records are superseded;
4. recover any local CAD if available;
5. if not available, recreate from source/this handoff;
6. inspect actual Rev-T reference meshes if accessible.

## Phase B — Freeze architecture
1. model top direct-drive world pose;
2. determine lowest feasible lower-yoke height from bearing/A03/loader needs;
3. reserve full marble loading envelope before basin floor is frozen;
4. model upper N20 + 15x20 coupler + service travel;
5. provide broad tool access to both coupler set-screw zones;
6. evaluate whether an extra bearing materially improves top drive;
7. integrate independent discharge-wing mounts;
8. preserve center access.

## Phase C — Modularize
1. split service cover into support-safe pieces;
2. use pins/holes/keyed joints where appropriate;
3. modularize U-basin;
4. keep commercial-track adapters replaceable;
5. ensure no large unsupported roof is introduced.

## Phase D — Audit
1. automated geometry audit for every part;
2. print-orientation audit;
3. tool-access audit;
4. marble-envelope audit;
5. assembly-sequence audit;
6. service-sequence audit;
7. output explicit PASS/HOLD/EXCLUDED status.

## Phase E — Produce shop package
1. create all requested documents;
2. include only gate-passing STLs in release-candidate folder;
3. keep fit-sensitive pieces in HOLD where appropriate;
4. include exact unknowns and required measurements;
5. create one ZIP;
6. provide a concise shop-facing README;
7. preserve all sources.

---

# 25. DO NOT LOSE THESE USER PREFERENCES

- Mechanism should be visually understandable.
- Wood should do simple structural work; plastic should do precision/interface work.
- User strongly dislikes boxy, square “project box” housings.
- Power/service housing should feel sculpted and proportionate to the cedar/spine.
- Rocker/PWM should mount directly through shell circles; no inset panel.
- Controls should be accessible but visually discreet.
- Full removable cover should expose N20, coupler, both coupler ends/set screws, and wiring.
- Use pegs/holes to break large pieces into printable modules.
- Basin should be substantial enough not to look comically small relative to a 48 in tower.
- Screw should stay relatively close to the cedar face.
- Marble loading geometry should determine lower screw height.
- Commercial track input should be modular.
- Do not waste filament on large candidate parts before small fit gates are proven.
- User wants a package close enough that a shop could finalize/build from it.

---

# 26. COPY/PASTE START PROMPT FOR CHATGPT WORK

Use this exact prompt or equivalent:

> Open the private GitHub repository `jeffreykusler-ux/marble-run-cad`. Read `WORK_HANDOFF_CURRENT.md` first and treat it as the newest recovery/control handoff for the Archimedes Screw Rev-U work. Then inspect the branch `screw/integrated-end-housings-2026-09-09` and continue the project from there.
>
> The finalized Marble Run Knowledge Pack remains the engineering authority. Preserve historical conflicts and do not silently reconcile them. Important: the newer top-direct-drive direction in `WORK_HANDOFF_CURRENT.md` supersedes earlier motor-bottom notes on the development branch unless your geometry/audit proves top drive unworkable.
>
> Carry the design as far as possible toward one shop-ready ZIP containing build sheets, plans, sources, STLs/STEP, dimensions, cut plans, shop/hardware lists, unconfirmed measurements, assembly/service instructions, pitfalls, physical-test gates, and design-gate reports. The removable upper cover must expose the N20, wiring, the whole coupler, and both coupler set-screw zones. The lower screw/basin geometry must be driven by marble-entry height, not by motor packaging. Contemplate and design the upper left/right discharge-wing interfaces. Modularize large pieces with pegs/holes where useful.
>
> Do not include an STL in the release-candidate folder unless it passes the automated design/mesh/printability/access gates. Keep physical-fit-dependent pieces clearly in HOLD. Do not stop at concept discussion; generate, audit, document, and package the work.

---

# 27. FINAL STATUS AT HANDOFF

The project had made meaningful progress before local Work failed.

The major architectural insight to preserve is:

> **The lower marble-entry requirement is more important than preserving the earlier bottom direct-drive layout. The current Rev-U direction is therefore a low lower-bearing/yoke with the motor and direct coupler moved to a serviceable top-drive cartridge, while the upper carrier also reserves independent left/right discharge support.**

This file exists so the next Work session can continue from that point without reconstructing the design conversation.
