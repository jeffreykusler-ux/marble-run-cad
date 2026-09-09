# Marble Run CAD

Controlled parametric CAD repository for Jeffrey Kusler's Marble Run project.

## Purpose

This repository stores the **working CAD source, engineering audits, revision history, and release metadata** for the Marble Run machines:

- Belt Lift
- Ferris Wheel
- Archimedes Screw
- Tramway
- Shared interfaces, coupons, and engineering utilities

The finalized Marble Run Knowledge Pack remains the governing engineering handoff. GitHub is the working CAD/revision system; an STL is a generated release artifact, not the source of truth.

## Authority

When records conflict, use this order:

1. Current physical/bench result
2. Newest dated controlled/current record
3. Newest dated machine-specific record and CARRY-FORWARD
4. Current CAD source / revision master
5. Older release, handoff, or historical material

Do not silently reconcile conflicting dimensions. Preserve superseded values as historical lineage.

## Core CAD rules

- Model functional parts parametrically.
- Print production parts at **100% scale**.
- Correct fit in CAD, not by slicer scaling.
- Use same-material, same-orientation coupons where fit matters.
- Verify built solids and exported meshes, not just source constants.
- Bench results outrank modeled assumptions.

## Branching

`main` contains accepted/current source. New or modified geometry is developed on a branch and is not considered current merely because it exists in the repository. Bench-tested changes are promoted through review and merge.

## Repository layout

- `standards/` — engineering rules, material compensation, interface conventions
- `common/` — reusable CadQuery/audit utilities
- `belt/`
- `ferris/`
- `screw/`
- `tramway/`

