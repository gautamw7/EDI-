import numpy as np
from trafficSim import *

sim = Simulation()

# Play with these
n = 20
a = -2
b = 12
l = 48

NUM_OF_ROADS = 36
VEHICLE_RATE = 80
STEPS_PER_UPDATE = 150  # Adjust this value to slow down the simulation

# Nodes
WEST_RIGHT_START = (-b-l, a)
WEST_LEFT_START = (-b-l, -a)

SOUTH_RIGHT_START = (a, b+l)
SOUTH_LEFT_START = (-a, b+l)

EAST_RIGHT_START = (b+l, -a)
EAST_LEFT_START = (b+l, a)

NORTH_RIGHT_START = (-a, -b-l)
NORTH_LEFT_START = (a, -b-l)

WEST_RIGHT = (-b, a)
WEST_LEFT =	(-b, -a)

SOUTH_RIGHT = (a, b)
SOUTH_LEFT = (-a, b)

EAST_RIGHT = (b, -a)
EAST_LEFT = (b, a)

NORTH_RIGHT = (-a, -b)
NORTH_LEFT = (a, -b)

WEST_RIGHT_START2 = (WEST_RIGHT_START[0], WEST_RIGHT_START[1] - 4)
WEST_LEFT_START2 = (WEST_LEFT_START[0], WEST_LEFT_START[1] + 4)

SOUTH_RIGHT_START2 = (SOUTH_RIGHT_START[0] - 4, SOUTH_RIGHT_START[1])
SOUTH_LEFT_START2 = (SOUTH_LEFT_START[0] + 4, SOUTH_LEFT_START[1])

EAST_RIGHT_START2 = (EAST_RIGHT_START[0], EAST_RIGHT_START[1] + 4)
EAST_LEFT_START2 = (EAST_LEFT_START[0], EAST_LEFT_START[1] - 4)

NORTH_RIGHT_START2 = (NORTH_RIGHT_START[0] + 4, NORTH_RIGHT_START[1])
NORTH_LEFT_START2 = (NORTH_LEFT_START[0] - 4, NORTH_LEFT_START[1])

WEST_RIGHT_START3 = (WEST_RIGHT_START[0], WEST_RIGHT_START[1] - 8)
WEST_LEFT_START3 = (WEST_LEFT_START[0], WEST_LEFT_START[1] + 8)

SOUTH_RIGHT_START3 = (SOUTH_RIGHT_START[0] - 8, SOUTH_RIGHT_START[1])
SOUTH_LEFT_START3 = (SOUTH_LEFT_START[0] + 8, SOUTH_LEFT_START[1])

EAST_RIGHT_START3 = (EAST_RIGHT_START[0], EAST_RIGHT_START[1] + 8)
EAST_LEFT_START3 = (EAST_LEFT_START[0], EAST_LEFT_START[1] - 8)

NORTH_RIGHT_START3 = (NORTH_RIGHT_START[0] + 8, NORTH_RIGHT_START[1])
NORTH_LEFT_START3 = (NORTH_LEFT_START[0] - 8, NORTH_LEFT_START[1])

WEST_RIGHT2 = (WEST_RIGHT[0], WEST_RIGHT[1] - 4)
WEST_LEFT2 =	(WEST_LEFT[0], WEST_LEFT[1] + 4)

SOUTH_RIGHT2 = (SOUTH_RIGHT[0] - 4, SOUTH_RIGHT[1])
SOUTH_LEFT2 = (SOUTH_LEFT[0] + 4, SOUTH_LEFT[1])

EAST_RIGHT2 = (EAST_RIGHT[0], EAST_RIGHT[1] + 4)
EAST_LEFT2 = (EAST_LEFT[0], EAST_LEFT[1] - 4)

NORTH_RIGHT2 = (NORTH_RIGHT[0] + 4, NORTH_RIGHT[1])
NORTH_LEFT2 = (NORTH_LEFT[0] - 4, NORTH_LEFT[1])

WEST_RIGHT3 = (WEST_RIGHT[0], WEST_RIGHT[1] - 8)
WEST_LEFT3 = (WEST_LEFT[0], WEST_LEFT[1] + 8)

SOUTH_RIGHT3 = (SOUTH_RIGHT[0] - 8, SOUTH_RIGHT[1])
SOUTH_LEFT3 = (SOUTH_LEFT[0] + 8, SOUTH_LEFT[1])

EAST_RIGHT3 = (EAST_RIGHT[0], EAST_RIGHT[1] + 8)
EAST_LEFT3 = (EAST_LEFT[0], EAST_LEFT[1] - 8)

NORTH_RIGHT3 = (NORTH_RIGHT[0] + 8, NORTH_RIGHT[1])
NORTH_LEFT3 = (NORTH_LEFT[0] - 8, NORTH_LEFT[1])

# Roads
WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)

WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)

WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

WEST_RIGHT_TURN = turn_road(WEST_RIGHT, SOUTH_LEFT, TURN_RIGHT, n)
WEST_LEFT_TURN = turn_road(WEST_RIGHT, NORTH_LEFT, TURN_LEFT, n)

SOUTH_RIGHT_TURN = turn_road(SOUTH_RIGHT, EAST_LEFT, TURN_RIGHT, n)
SOUTH_LEFT_TURN = turn_road(SOUTH_RIGHT, WEST_LEFT, TURN_LEFT, n)

EAST_RIGHT_TURN = turn_road(EAST_RIGHT, NORTH_LEFT, TURN_RIGHT, n)
EAST_LEFT_TURN = turn_road(EAST_RIGHT, SOUTH_LEFT, TURN_LEFT, n)

NORTH_RIGHT_TURN = turn_road(NORTH_RIGHT, WEST_LEFT, TURN_RIGHT, n)
NORTH_LEFT_TURN = turn_road(NORTH_RIGHT, EAST_LEFT, TURN_LEFT, n)

WEST_INBOUND2 = (WEST_RIGHT_START2, WEST_RIGHT2)
SOUTH_INBOUND2 = (SOUTH_RIGHT_START2, SOUTH_RIGHT2)
EAST_INBOUND2 = (EAST_RIGHT_START2, EAST_RIGHT2)
NORTH_INBOUND2 = (NORTH_RIGHT_START2, NORTH_RIGHT2)

WEST_OUTBOUND2 = (WEST_LEFT2, WEST_LEFT_START2)
SOUTH_OUTBOUND2 = (SOUTH_LEFT2, SOUTH_LEFT_START2)
EAST_OUTBOUND2 = (EAST_LEFT2, EAST_LEFT_START2)
NORTH_OUTBOUND2 = (NORTH_LEFT2, NORTH_LEFT_START2)

WEST_STRAIGHT2 = (WEST_RIGHT2, EAST_LEFT2)
SOUTH_STRAIGHT2 = (SOUTH_RIGHT2, NORTH_LEFT2)
EAST_STRAIGHT2 = (EAST_RIGHT2, WEST_LEFT2)
NORTH_STRAIGHT2 = (NORTH_RIGHT2, SOUTH_LEFT2)

WEST_RIGHT_TURN2 = turn_road(WEST_RIGHT2, SOUTH_LEFT2, TURN_RIGHT, n)
WEST_LEFT_TURN2 = turn_road(WEST_RIGHT2, NORTH_LEFT2, TURN_LEFT, n)

SOUTH_RIGHT_TURN2 = turn_road(SOUTH_RIGHT2, EAST_LEFT2, TURN_RIGHT, n)
SOUTH_LEFT_TURN2 = turn_road(SOUTH_RIGHT2, WEST_LEFT2, TURN_LEFT, n)

EAST_RIGHT_TURN2 = turn_road(EAST_RIGHT2, NORTH_LEFT2, TURN_RIGHT, n)
EAST_LEFT_TURN2 = turn_road(EAST_RIGHT2, SOUTH_LEFT2, TURN_LEFT, n)

NORTH_RIGHT_TURN2 = turn_road(NORTH_RIGHT2, WEST_LEFT2, TURN_RIGHT, n)
NORTH_LEFT_TURN2 = turn_road(NORTH_RIGHT2, EAST_LEFT2, TURN_LEFT, n)

WEST_INBOUND3 = (WEST_RIGHT_START3, WEST_RIGHT3)
SOUTH_INBOUND3 = (SOUTH_RIGHT_START3, SOUTH_RIGHT3)
EAST_INBOUND3 = (EAST_RIGHT_START3, EAST_RIGHT3)
NORTH_INBOUND3 = (NORTH_RIGHT_START3, NORTH_RIGHT3)

WEST_OUTBOUND3 = (WEST_LEFT3, WEST_LEFT_START3)
SOUTH_OUTBOUND3 = (SOUTH_LEFT3, SOUTH_LEFT_START3)
EAST_OUTBOUND3 = (EAST_LEFT3, EAST_LEFT_START3)
NORTH_OUTBOUND3 = (NORTH_LEFT3, NORTH_LEFT_START3)

WEST_STRAIGHT3 = (WEST_RIGHT3, EAST_LEFT3)
SOUTH_STRAIGHT3 = (SOUTH_RIGHT3, NORTH_LEFT3)
EAST_STRAIGHT3 = (EAST_RIGHT3, WEST_LEFT3)
NORTH_STRAIGHT3 = (NORTH_RIGHT3, SOUTH_LEFT3)

WEST_RIGHT_TURN3 = turn_road(WEST_RIGHT3, SOUTH_LEFT3, TURN_RIGHT, n)
WEST_LEFT_TURN3 = turn_road(WEST_RIGHT3, NORTH_LEFT3, TURN_LEFT, n)

SOUTH_RIGHT_TURN3 = turn_road(SOUTH_RIGHT3, EAST_LEFT3, TURN_RIGHT, n)
SOUTH_LEFT_TURN3 = turn_road(SOUTH_RIGHT3, WEST_LEFT3, TURN_LEFT, n)

EAST_RIGHT_TURN3 = turn_road(EAST_RIGHT3, NORTH_LEFT3, TURN_RIGHT, n)
EAST_LEFT_TURN3 = turn_road(EAST_RIGHT3, SOUTH_LEFT3, TURN_LEFT, n)

NORTH_RIGHT_TURN3 = turn_road(NORTH_RIGHT3, WEST_LEFT3, TURN_RIGHT, n)
NORTH_LEFT_TURN3 = turn_road(NORTH_RIGHT3, EAST_LEFT3, TURN_LEFT, n)

# Trying second intersection to the right of the original one
o2 = (2*b+l, 0)

b_WEST_RIGHT_START = (o2[0] + WEST_RIGHT_START[0], EAST_LEFT[1])
b_WEST_LEFT_START = (o2[0] + WEST_LEFT_START[0], EAST_RIGHT[1])

b_SOUTH_RIGHT_START = (o2[0] + SOUTH_RIGHT_START[0], SOUTH_RIGHT_START[1])
b_SOUTH_LEFT_START = (o2[0] + SOUTH_LEFT_START[0], SOUTH_LEFT_START[1])

b_EAST_RIGHT_START = (o2[0] + EAST_RIGHT_START[0], EAST_RIGHT_START[1])
b_EAST_LEFT_START = (o2[0] + EAST_LEFT_START[0], EAST_LEFT_START[1])

b_NORTH_RIGHT_START = (o2[0] + NORTH_RIGHT_START[0], NORTH_RIGHT_START[1])
b_NORTH_LEFT_START = (o2[0] + NORTH_LEFT_START[0], NORTH_LEFT_START[1])

b_WEST_RIGHT = (o2[0] + WEST_RIGHT[0], EAST_LEFT_START[1])
b_WEST_LEFT = (o2[0] + WEST_LEFT[0], EAST_RIGHT_START[1])

b_SOUTH_RIGHT = (o2[0] + SOUTH_RIGHT[0], SOUTH_RIGHT[1])
b_SOUTH_LEFT = (o2[0] + SOUTH_LEFT[0], SOUTH_LEFT[1])

b_EAST_RIGHT = (o2[0] + EAST_RIGHT[0], EAST_RIGHT[1])
b_EAST_LEFT = (o2[0] + EAST_LEFT[0], EAST_LEFT[1])

b_NORTH_RIGHT = (o2[0] + NORTH_RIGHT[0], NORTH_LEFT[1])
b_NORTH_LEFT = (o2[0] + NORTH_LEFT[0], NORTH_LEFT[1])

b_WEST_RIGHT_START2 = (b_WEST_RIGHT_START[0], b_WEST_RIGHT_START[1] - 4)
b_WEST_LEFT_START2 = (b_WEST_LEFT_START[0], b_WEST_LEFT_START[1] + 4)

b_SOUTH_RIGHT_START2 = (b_SOUTH_RIGHT_START[0] - 4, b_SOUTH_RIGHT_START[1])
b_SOUTH_LEFT_START2 = (b_SOUTH_LEFT_START[0] + 4, b_SOUTH_LEFT_START[1])

b_EAST_RIGHT_START2 = (b_EAST_RIGHT_START[0], b_EAST_RIGHT_START[1] + 4)
b_EAST_LEFT_START2 = (b_EAST_LEFT_START[0], b_EAST_LEFT_START[1] - 4)

b_NORTH_RIGHT_START2 = (b_NORTH_RIGHT_START[0] + 4, b_NORTH_RIGHT_START[1])
b_NORTH_LEFT_START2 = (b_NORTH_LEFT_START[0] - 4, b_NORTH_LEFT_START[1])

b_WEST_RIGHT_START3 = (b_WEST_RIGHT_START[0], b_WEST_RIGHT_START[1] - 8)
b_WEST_LEFT_START3 = (b_WEST_LEFT_START[0], b_WEST_LEFT_START[1] + 8)

b_SOUTH_RIGHT_START3 = (b_SOUTH_RIGHT_START[0] - 8, b_SOUTH_RIGHT_START[1])
b_SOUTH_LEFT_START3 = (b_SOUTH_LEFT_START[0] + 8, b_SOUTH_LEFT_START[1])

b_EAST_RIGHT_START3 = (b_EAST_RIGHT_START[0], b_EAST_RIGHT_START[1] + 8)
b_EAST_LEFT_START3 = (b_EAST_LEFT_START[0], b_EAST_LEFT_START[1] - 8)

b_NORTH_RIGHT_START3 = (b_NORTH_RIGHT_START[0] + 8, b_NORTH_RIGHT_START[1])
b_NORTH_LEFT_START3 = (b_NORTH_LEFT_START[0] - 8, b_NORTH_LEFT_START[1])

b_WEST_RIGHT2 = (b_WEST_RIGHT[0], b_WEST_RIGHT[1] - 4)
b_WEST_LEFT2 =	(b_WEST_LEFT[0], b_WEST_LEFT[1] + 4)

b_SOUTH_RIGHT2 = (b_SOUTH_RIGHT[0] - 4, b_SOUTH_RIGHT[1])
b_SOUTH_LEFT2 = (b_SOUTH_LEFT[0] + 4, b_SOUTH_LEFT[1])

b_EAST_RIGHT2 = (b_EAST_RIGHT[0], b_EAST_RIGHT[1] + 4)
b_EAST_LEFT2 = (b_EAST_LEFT[0], b_EAST_LEFT[1] - 4)

b_NORTH_RIGHT2 = (b_NORTH_RIGHT[0] + 4, b_NORTH_RIGHT[1])
b_NORTH_LEFT2 = (b_NORTH_LEFT[0] - 4, b_NORTH_LEFT[1])

b_WEST_RIGHT3 = (b_WEST_RIGHT[0], b_WEST_RIGHT[1] - 8)
b_WEST_LEFT3 =	(b_WEST_LEFT[0], b_WEST_LEFT[1] + 8)

b_SOUTH_RIGHT3 = (b_SOUTH_RIGHT[0] - 8, b_SOUTH_RIGHT[1])
b_SOUTH_LEFT3 = (b_SOUTH_LEFT[0] + 8, b_SOUTH_LEFT[1])

b_EAST_RIGHT3 = (b_EAST_RIGHT[0], b_EAST_RIGHT[1] + 8)
b_EAST_LEFT3 = (b_EAST_LEFT[0], b_EAST_LEFT[1] - 8)

b_NORTH_RIGHT3 = (b_NORTH_RIGHT[0] + 8, b_NORTH_RIGHT[1])
b_NORTH_LEFT3 = (b_NORTH_LEFT[0] - 8, b_NORTH_LEFT[1])

# Intersection b - Roads
b_WEST_INBOUND = (b_WEST_RIGHT_START, b_WEST_RIGHT)
b_SOUTH_INBOUND = (b_SOUTH_RIGHT_START, b_SOUTH_RIGHT)
b_EAST_INBOUND = (b_EAST_RIGHT_START, b_EAST_RIGHT)
b_NORTH_INBOUND = (b_NORTH_RIGHT_START, b_NORTH_RIGHT)

b_WEST_OUTBOUND = (b_WEST_LEFT, b_WEST_LEFT_START)
b_SOUTH_OUTBOUND = (b_SOUTH_LEFT, b_SOUTH_LEFT_START)
b_EAST_OUTBOUND = (b_EAST_LEFT, b_EAST_LEFT_START)
b_NORTH_OUTBOUND = (b_NORTH_LEFT, b_NORTH_LEFT_START)

b_WEST_STRAIGHT = (b_WEST_RIGHT, b_EAST_LEFT)
b_SOUTH_STRAIGHT = (b_SOUTH_RIGHT, b_NORTH_LEFT)
b_EAST_STRAIGHT = (b_EAST_RIGHT, b_WEST_LEFT)
b_NORTH_STRAIGHT = (b_NORTH_RIGHT, b_SOUTH_LEFT)

b_WEST_RIGHT_TURN = turn_road(b_WEST_RIGHT, b_SOUTH_LEFT, TURN_RIGHT, n)
b_WEST_LEFT_TURN = turn_road(b_WEST_RIGHT, b_NORTH_LEFT, TURN_LEFT, n)

b_SOUTH_RIGHT_TURN = turn_road(b_SOUTH_RIGHT, b_EAST_LEFT, TURN_RIGHT, n)
b_SOUTH_LEFT_TURN = turn_road(b_SOUTH_RIGHT, b_WEST_LEFT, TURN_LEFT, n)

b_EAST_RIGHT_TURN = turn_road(b_EAST_RIGHT, b_NORTH_LEFT, TURN_RIGHT, n)
b_EAST_LEFT_TURN = turn_road(b_EAST_RIGHT, b_SOUTH_LEFT, TURN_LEFT, n)

b_NORTH_RIGHT_TURN = turn_road(b_NORTH_RIGHT, b_WEST_LEFT, TURN_RIGHT, n)
b_NORTH_LEFT_TURN = turn_road(b_NORTH_RIGHT, b_EAST_LEFT, TURN_LEFT, n)

b_WEST_INBOUND2 = (b_WEST_RIGHT_START2, b_WEST_RIGHT2)
b_SOUTH_INBOUND2 = (b_SOUTH_RIGHT_START2, b_SOUTH_RIGHT2)
b_EAST_INBOUND2 = (b_EAST_RIGHT_START2, b_EAST_RIGHT2)
b_NORTH_INBOUND2 = (b_NORTH_RIGHT_START2, b_NORTH_RIGHT2)

b_WEST_OUTBOUND2 = (b_WEST_LEFT2, b_WEST_LEFT_START2)
b_SOUTH_OUTBOUND2 = (b_SOUTH_LEFT2, b_SOUTH_LEFT_START2)
b_EAST_OUTBOUND2 = (b_EAST_LEFT2, b_EAST_LEFT_START2)
b_NORTH_OUTBOUND2 = (b_NORTH_LEFT2, b_NORTH_LEFT_START2)

b_WEST_STRAIGHT2 = (b_WEST_RIGHT2, b_EAST_LEFT2)
b_SOUTH_STRAIGHT2 = (b_SOUTH_RIGHT2, b_NORTH_LEFT2)
b_EAST_STRAIGHT2 = (b_EAST_RIGHT2, b_WEST_LEFT2)
b_NORTH_STRAIGHT2 = (b_NORTH_RIGHT2, b_SOUTH_LEFT2)

b_WEST_RIGHT_TURN2 = turn_road(b_WEST_RIGHT2, b_SOUTH_LEFT2, TURN_RIGHT, n)
b_WEST_LEFT_TURN2 = turn_road(b_WEST_RIGHT2, b_NORTH_LEFT2, TURN_LEFT, n)

b_SOUTH_RIGHT_TURN2 = turn_road(b_SOUTH_RIGHT2, b_EAST_LEFT2, TURN_RIGHT, n)
b_SOUTH_LEFT_TURN2 = turn_road(b_SOUTH_RIGHT2, b_WEST_LEFT2, TURN_LEFT, n)

b_EAST_RIGHT_TURN2 = turn_road(b_EAST_RIGHT2, b_NORTH_LEFT2, TURN_RIGHT, n)
b_EAST_LEFT_TURN2 = turn_road(b_EAST_RIGHT2, b_SOUTH_LEFT2, TURN_LEFT, n)

b_NORTH_RIGHT_TURN2 = turn_road(b_NORTH_RIGHT2, b_WEST_LEFT2, TURN_RIGHT, n)
b_NORTH_LEFT_TURN2 = turn_road(b_NORTH_RIGHT2, b_EAST_LEFT2, TURN_LEFT, n)

b_WEST_INBOUND3 = (b_WEST_RIGHT_START3, b_WEST_RIGHT3)
b_SOUTH_INBOUND3 = (b_SOUTH_RIGHT_START3, b_SOUTH_RIGHT3)
b_EAST_INBOUND3 = (b_EAST_RIGHT_START3, b_EAST_RIGHT3)
b_NORTH_INBOUND3 = (b_NORTH_RIGHT_START3, b_NORTH_RIGHT3)

b_WEST_OUTBOUND3 = (b_WEST_LEFT3, b_WEST_LEFT_START3)
b_SOUTH_OUTBOUND3 = (b_SOUTH_LEFT3, b_SOUTH_LEFT_START3)
b_EAST_OUTBOUND3 = (b_EAST_LEFT3, b_EAST_LEFT_START3)
b_NORTH_OUTBOUND3 = (b_NORTH_LEFT3, b_NORTH_LEFT_START3)

b_WEST_STRAIGHT3 = (b_WEST_RIGHT3, b_EAST_LEFT3)
b_SOUTH_STRAIGHT3 = (b_SOUTH_RIGHT3, b_NORTH_LEFT3)
b_EAST_STRAIGHT3 = (b_EAST_RIGHT3, b_WEST_LEFT3)
b_NORTH_STRAIGHT3 = (b_NORTH_RIGHT3, b_SOUTH_LEFT3)

b_WEST_RIGHT_TURN3 = turn_road(b_WEST_RIGHT3, b_SOUTH_LEFT3, TURN_RIGHT, n)
b_WEST_LEFT_TURN3 = turn_road(b_WEST_RIGHT3, b_NORTH_LEFT3, TURN_LEFT, n)

b_SOUTH_RIGHT_TURN3 = turn_road(b_SOUTH_RIGHT3, b_EAST_LEFT3, TURN_RIGHT, n)
b_SOUTH_LEFT_TURN3 = turn_road(b_SOUTH_RIGHT3, b_WEST_LEFT3, TURN_LEFT, n)

b_EAST_RIGHT_TURN3 = turn_road(b_EAST_RIGHT3, b_NORTH_LEFT3, TURN_RIGHT, n)
b_EAST_LEFT_TURN3 = turn_road(b_EAST_RIGHT3, b_SOUTH_LEFT3, TURN_LEFT, n)

b_NORTH_RIGHT_TURN3 = turn_road(b_NORTH_RIGHT3, b_WEST_LEFT3, TURN_RIGHT, n)
b_NORTH_LEFT_TURN3 = turn_road(b_NORTH_RIGHT3, b_EAST_LEFT3, TURN_LEFT, n)

sim.create_roads([
    WEST_INBOUND,   #0
    SOUTH_INBOUND,  #1
    EAST_INBOUND,   #2
    NORTH_INBOUND,  #3

    WEST_OUTBOUND,  #4
    SOUTH_OUTBOUND, #5
    EAST_OUTBOUND,  #6
    NORTH_OUTBOUND, #7

    WEST_STRAIGHT,  #8
    SOUTH_STRAIGHT, #9
    EAST_STRAIGHT,  #10
    NORTH_STRAIGHT, #11

    WEST_INBOUND2,  #12
    SOUTH_INBOUND2, #13
    EAST_INBOUND2,  #14
    NORTH_INBOUND2, #15

    WEST_OUTBOUND2, #16
    SOUTH_OUTBOUND2, #17
    EAST_OUTBOUND2, #18
    NORTH_OUTBOUND2, #19

    WEST_STRAIGHT2, #20
    SOUTH_STRAIGHT2, #21
    EAST_STRAIGHT2, #22
    NORTH_STRAIGHT2, #23

    WEST_INBOUND3,  #24
    SOUTH_INBOUND3, #25
    EAST_INBOUND3,  #26
    NORTH_INBOUND3, #27

    WEST_OUTBOUND3, #28
    SOUTH_OUTBOUND3, #29
    EAST_OUTBOUND3, #30
    NORTH_OUTBOUND3, #31

    WEST_STRAIGHT3, #32
    SOUTH_STRAIGHT3, #33
    EAST_STRAIGHT3, #34
    NORTH_STRAIGHT3, #35

    *WEST_RIGHT_TURN, #36
    *WEST_LEFT_TURN, #56

    *SOUTH_RIGHT_TURN, #76
    *SOUTH_LEFT_TURN, #96

    *EAST_RIGHT_TURN, #116
    *EAST_LEFT_TURN, #136

    *NORTH_RIGHT_TURN, #156
    *NORTH_LEFT_TURN, #176

    *WEST_RIGHT_TURN2, #196
    *WEST_LEFT_TURN2, #216

    *SOUTH_RIGHT_TURN2, #236
    *SOUTH_LEFT_TURN2, #256

    *EAST_RIGHT_TURN2, #276
    *EAST_LEFT_TURN2, #296

    *NORTH_RIGHT_TURN2, #316
    *NORTH_LEFT_TURN2, #336

    *WEST_RIGHT_TURN3, #356
    *WEST_LEFT_TURN3, #376

    *SOUTH_RIGHT_TURN3, #396
    *SOUTH_LEFT_TURN3, #416

    *EAST_RIGHT_TURN3, #436
    *EAST_LEFT_TURN3, #456

    *NORTH_RIGHT_TURN3, #476
    *NORTH_LEFT_TURN3, #496

    b_WEST_INBOUND, #516
    b_SOUTH_INBOUND, #517
    b_EAST_INBOUND, #518
    b_NORTH_INBOUND, #519

    b_WEST_OUTBOUND, #520
    b_SOUTH_OUTBOUND, #521
    b_EAST_OUTBOUND, #522
    b_NORTH_OUTBOUND, #523

    b_WEST_STRAIGHT, #524
    b_SOUTH_STRAIGHT, #525
    b_EAST_STRAIGHT, #526
    b_NORTH_STRAIGHT, #527

    b_WEST_INBOUND2, #528
    b_SOUTH_INBOUND2, #529
    b_EAST_INBOUND2, #530
    b_NORTH_INBOUND2, #531

    b_WEST_OUTBOUND2, #532
    b_SOUTH_OUTBOUND2, #533
    b_EAST_OUTBOUND2, #534
    b_NORTH_OUTBOUND2, #535

    b_WEST_STRAIGHT2, #536
    b_SOUTH_STRAIGHT2, #537
    b_EAST_STRAIGHT2, #538
    b_NORTH_STRAIGHT2, #539

    b_WEST_INBOUND3, #540
    b_SOUTH_INBOUND3, #541
    b_EAST_INBOUND3, #542
    b_NORTH_INBOUND3, #543

    b_WEST_OUTBOUND3, #544
    b_SOUTH_OUTBOUND3, #545
    b_EAST_OUTBOUND3, #546
    b_NORTH_OUTBOUND3, #547

    b_WEST_STRAIGHT3, #548
    b_SOUTH_STRAIGHT3, #549
    b_EAST_STRAIGHT3, #550
    b_NORTH_STRAIGHT3, #551

    *b_WEST_RIGHT_TURN, #552
    *b_WEST_LEFT_TURN, #572

    *b_SOUTH_RIGHT_TURN, #592
    *b_SOUTH_LEFT_TURN, #612

    *b_EAST_RIGHT_TURN, #632
    *b_EAST_LEFT_TURN, #652

    *b_NORTH_RIGHT_TURN, #672
    *b_NORTH_LEFT_TURN, #692

    *b_WEST_RIGHT_TURN2, #712
    *b_WEST_LEFT_TURN2, #732

    *b_SOUTH_RIGHT_TURN2, #752
    *b_SOUTH_LEFT_TURN2, #772

    *b_EAST_RIGHT_TURN2, #792
    *b_EAST_LEFT_TURN2, #812

    *b_NORTH_RIGHT_TURN2, #832
    *b_NORTH_LEFT_TURN2, #852

    *b_WEST_RIGHT_TURN3, #872
    *b_WEST_LEFT_TURN3, #892

    *b_SOUTH_RIGHT_TURN3, #912
    *b_SOUTH_LEFT_TURN3, #932

    *b_EAST_RIGHT_TURN3, #952
    *b_EAST_LEFT_TURN3, #972

    *b_NORTH_RIGHT_TURN3, #992
    *b_NORTH_LEFT_TURN3, #1012
])

def road(a): return range(a, a+n)

sim.create_gen({
    'vehicle_rate': VEHICLE_RATE,
    'vehicles': [
        # West to South, East, North
        [1, {'path': [0, *road(36), 5]}],
        [2, {'path': [0, *road(36), 6]}],
        [3, {'path': [0, *road(36), 7]}],

        # West_INBOUND2 to South_OUTBOUND2, East_OUTBOUND2, North_OUTBOUND2
        [1, {'path': [12, *road(36), 17]}],
        [2, {'path': [12, *road(36), 18]}],
        [3, {'path': [12, *road(36), 19]}],

        # NORTH_INBOUND3 to SOUTH_OUTBOUND3, EAST_OUTBOUND3, NORTH_OUTBOUND3
        [1, {'path': [24, *road(36), 29]}],
        [2, {'path': [24, *road(36), 30]}],
        [3, {'path': [24, *road(36), 31]}],

        # Similarly for other directions
        [0, {'path': [4, *road(36), 9]}],  # South to West, East, North
        [2, {'path': [4, *road(36), 10]}],
        [3, {'path': [4, *road(36), 11]}],

        [0, {'path': [16, *road(36), 21]}],  # SOUTH_INBOUND2 to WEST_OUTBOUND2, EAST_OUTBOUND2, NORTH_OUTBOUND2
        [2, {'path': [16, *road(36), 22]}],
        [3, {'path': [16, *road(36), 23]}],

        [0, {'path': [28, *road(36), 33]}],  # SOUTH_INBOUND3 to WEST_OUTBOUND3, EAST_OUTBOUND3, NORTH_OUTBOUND3
        [2, {'path': [28, *road(36), 34]}],
        [3, {'path': [28, *road(36), 35]}],

        [2, {'path': [6, *road(36), 1]}],  # East to South, West, North
        [0, {'path': [6, *road(36), 4]}],
        [3, {'path': [6, *road(36), 3]}],

        [2, {'path': [18, *road(36), 13]}],  # EAST_INBOUND2 to SOUTH_OUTBOUND, WEST_OUTBOUND, NORTH_OUTBOUND
        [0, {'path': [18, *road(36), 12]}],
        [3, {'path': [18, *road(36), 15]}],

        [2, {'path': [30, *road(36), 25]}],  # EAST_INBOUND3 to SOUTH_OUTBOUND3, WEST_OUTBOUND3, NORTH_OUTBOUND3
        [0, {'path': [30, *road(36), 24]}],
        [3, {'path': [30, *road(36), 27]}],

        [3, {'path': [7, *road(36), 2]}],  # North to South, East, West
        [1, {'path': [7, *road(36), 1]}],
        [2, {'path': [7, *road(36), 0]}],

        [3, {'path': [19, *road(36), 14]}],  # NORTH_INBOUND2 to SOUTH_OUTBOUND2, EAST_OUTBOUND2, WEST_OUTBOUND2
        [1, {'path': [19, *road(36), 13]}],
        [2, {'path': [19, *road(36), 16]}],

        [3, {'path': [31, *road(36), 26]}],  # NORTH_INBOUND3 to SOUTH_OUTBOUND3, EAST_OUTBOUND3, WEST_OUTBOUND3
        [1, {'path': [31, *road(36), 25]}],
        [2, {'path': [31, *road(36), 28]}],

[1, {'path': [516, *road(36), 521]}],  # b_WEST_INBOUND to b_SOUTH_OUTBOUND, b_EAST_OUTBOUND, b_NORTH_OUTBOUND
        [2, {'path': [516, *road(36), 522]}],
        [3, {'path': [516, *road(36), 523]}],

        [1, {'path': [528, *road(36), 533]}],  # b_WEST_INBOUND2 to b_SOUTH_OUTBOUND2, b_EAST_OUTBOUND2, b_NORTH_OUTBOUND2
        [2, {'path': [528, *road(36), 534]}],
        [3, {'path': [528, *road(36), 535]}],

        [1, {'path': [540, *road(36), 545]}],  # b_NORTH_INBOUND3 to b_SOUTH_OUTBOUND3, b_EAST_OUTBOUND3, b_NORTH_OUTBOUND3
        [2, {'path': [540, *road(36), 546]}],
        [3, {'path': [540, *road(36), 547]}],

        [0, {'path': [518, *road(36), 525]}],  # b_SOUTH_INBOUND to b_WEST_OUTBOUND, b_EAST_OUTBOUND, b_NORTH_OUTBOUND
        [2, {'path': [518, *road(36), 526]}],
        [3, {'path': [518, *road(36), 527]}],

        [0, {'path': [530, *road(36), 537]}],  # b_SOUTH_INBOUND2 to b_WEST_OUTBOUND2, b_EAST_OUTBOUND2, b_NORTH_OUTBOUND2
        [2, {'path': [530, *road(36), 538]}],
        [3, {'path': [530, *road(36), 539]}],

        [0, {'path': [542, *road(36), 549]}],  # b_SOUTH_INBOUND3 to b_WEST_OUTBOUND3, b_EAST_OUTBOUND3, b_NORTH_OUTBOUND3
        [2, {'path': [542, *road(36), 550]}],
        [3, {'path': [542, *road(36), 551]}],

        [2, {'path': [520, *road(36), 517]}],  # b_EAST_INBOUND to b_SOUTH_INBOUND, b_WEST_INBOUND, b_NORTH_INBOUND
        [0, {'path': [520, *road(36), 516]}],
        [3, {'path': [520, *road(36), 519]}],

        [2, {'path': [532, *road(36), 529]}],  # b_EAST_INBOUND2 to b_SOUTH_INBOUND2, b_WEST_INBOUND2, b_NORTH_INBOUND2
        [0, {'path': [532, *road(36), 528]}],
        [3, {'path': [532, *road(36), 531]}],

        [2, {'path': [544, *road(36), 541]}],  # b_EAST_INBOUND3 to b_SOUTH_INBOUND3, b_WEST_INBOUND3, b_NORTH_INBOUND3
        [0, {'path': [544, *road(36), 540]}],
        [3, {'path': [544, *road(36), 543]}],

        [3, {'path': [522, *road(36), 517]}],  # b_NORTH_INBOUND to b_SOUTH_INBOUND, b_WEST_INBOUND, b_EAST_INBOUND
        [1, {'path': [522, *road(36), 516]}],
        [2, {'path': [522, *road(36), 519]}],

        [3, {'path': [534, *road(36), 529]}],  # b_NORTH_INBOUND2 to b_SOUTH_INBOUND2, b_WEST_INBOUND2, b_EAST_INBOUND2
        [1, {'path': [534, *road(36), 528]}],
        [2, {'path': [534, *road(36), 531]}],

        [3, {'path': [546, *road(36), 541]}],  # b_NORTH_INBOUND3 to b_SOUTH_INBOUND3, b_WEST_INBOUND3, b_EAST_INBOUND3
        [1, {'path': [546, *road(36), 540]}],
        [2, {'path': [546, *road(36), 543]}],
    ]
})



sim.create_signal([[0], [1], [2], [3]])
sim.create_signal([[12], [13], [14], [15]])

# Create Green Light for 3rd Lane
sim.create_signal([[24]])
sim.create_signal([[25]])
sim.create_signal([[26]])
sim.create_signal([[27]])

sim.create_signal([[516], [517], [518], [519]])
sim.create_signal([[528], [529], [530], [531]])

sim.create_signal([[540]])
sim.create_signal([[541]])
sim.create_signal([[542]])
sim.create_signal([[543]])

# Start simulation
win = Window(sim)
win.zoom = 10
if(sim.isPaused == False):
    win.run(steps_per_update=STEPS_PER_UPDATE)