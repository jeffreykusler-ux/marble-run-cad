import cadquery as cq

# FORM / ENVELOPE candidate only.
# Hardware-specific battery and control details are intentionally held for confirmation.
CEDAR_W = 139.7
TWO_BY_FOUR_W = 88.9
TWO_BY_FOUR_DEPTH = 38.1
POD_W = 122.0
POD_H = 92.0
POD_D = 42.0
WALL = 3.25

# Design intent:
# - rounded/tapered shield body behind the 2x4
# - side cheeks wrap forward beside the 2x4 and land on exposed cedar shoulders
# - direct rear-shell circular openings for rocker and PWM
# - lateral battery access
# - hidden wiring exits toward an internal cedar/2x4 wire channel
# - no inset control panel
#
# Exact hardware bores remain provisional until the user's proven dimensions are confirmed.
