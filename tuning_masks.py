'''
This document defines the tuning masks; a matrix of the expected effects for a step of each tuning option described.
Each value in a tuning mask will represent a delta of the chassis balance matrix, as defined in chassis_balance.py.

    [  Initial braking, turn-in, mid-corner, corner-exit-inital, throttle-out
       Unstable(-5) <-----> Neutral(0) <-----> Stable(5)
        [ _, _, _, _, _,],  0-40 mph
        [ _, _, _, _, _,],  40-60 mph
        [ _, _, _, _, _,],  60-80 mph
        [ _, _, _, _, _,]  90+ mph
    ],
    [ _,], Suspension stiffness bias, Too Soft(-5) <-----> Neutral(0) <-----> Too Stiff(5)
    [ _,]  Downforce/drag bias, Insufficient Downforce(-5) <-----> Neutral(0) <-----> Excessive Drag(5)
'''

import numpy as np

null = [
    np.array([
        [ 0, 0, 0, 0, 0,],
        [ 0, 0, 0, 0, 0,],
        [ 0, 0, 0, 0, 0,],
        [ 0, 0, 0, 0, 0,],
    ]),
    0,
    0,
    None,
    None
]

### BRAKE TUNING PARAMTERS ###

brake_bias_forward = [
    np.array([
        [ 1, 1, 0, 0, 0,],
        [ 1, 1, 0, 0, 0,],
        [ 1, 1, 0, 0, 0,],
        [ 1, 1, 0, 0, 0,],
    ]),
    0,
    0,
    str('One step increasing brake bias forward %.'),
    str('Reduces rear brake lockup on initial brake application. Decreases rotation during trail-braking.')
]

brake_bias_rearward = [
    np.array([
        [ -1, -1, 0, 0, 0,],
        [ -1, -1, 0, 0, 0,],
        [ -1, -1, 0, 0, 0,],
        [ -1, -1, 0, 0, 0,],
    ]),
    0,
    0,
    str('One step decreasing brake bias forward %.'),
    str('Reduces front brake lockup on initial brake application. Increases rotation during trail-braking.')
]

### SUSPENSION TUNING PARAMETERS ###

stiffen_front_ARB = [
    np.array([
        [ .25, 1, 1, 1, 1,],
        [ .25, 1, 1, 1, 1,],
        [ .25, 1, 1, 1, 1,],
        [ .25, 1, 1, 1, 1,]
    ]),
    1,
    0,
    str('One step stiffening front sway bar. (Increase bar diamater or shorten arm length).'),
    str('Increases understeer in all corner phases.')
]

soften_front_ARB = [
    np.array([
        [ -.25, -1, -1, -1, -1],
        [ -.25, -1, -1, -1, -1],
        [ -.25, -1, -1, -1, -1],
        [ -.25, -1, -1, -1, -1]
    ]),
    -1,
    0,
    str('One step softening front sway bar. (Decrease bar diamater or lengthen arm).'),
    str('Increases oversteer in all corner phases.')
]

stiffen_rear_ARB = [
    np.array([
        [ -.25, -1, -1, -1, -1,],
        [ -.25, -1, -1, -1, -1,],
        [ -.25, -1, -1, -1, -1,],
        [ -.25, -1, -1, -1, -1,]
    ]),
    1,
    0,
    str('One step stiffening rear sway bar. (Increase bar diamater or shorten arm length).'),
    str('Increases oversteer in all corner phases.')
]

soften_rear_ARB = [
    np.array([
        [ .25, 1, 1, 1, 1,],
        [ .25, 1, 1, 1, 1,],
        [ .25, 1, 1, 1, 1,],
        [ .25, 1, 1, 1, 1,]
    ]),
    -1,
    0,
    str('One step softening rear sway bar. (Decrease bar diamater or lengthen arm).'),
    str('Increases understeer in all corner phases.')
]

increase_front_negative_camber = [
    np.array([
        [ .5, 0, -.5, -.5, -.5],
        [ .5, 0, -.5, -.5, -.5],
        [ .5, 0, -.5, -.5, -.5],
        [ .5, 0, -.5, -.5, -.5]
    ]),
    0,
    0,
    str('Increase front negative camber ~0.25 degrees.'),
    str('On most suspensions and tires, increasing negative camber until about -5 degrees should continue to increase front tire lateral grip potential, at the cost of front tire braking grip potential.  ')
]

### DIFFERENTIAL TUNING PARAMETERS ###

increase_diff_preload = [
    np.array([
        [ 0.5, 1, 0, -1, -1,],
        [ 0.5, 1, 0, -1, -1,],
        [ 0.5, 1, 0, -1, -1,],
        [ 0.5, 1, 0, -1, -1,]
    ]),
    0,
    0,
    str('Increase differential preload one step.'),
    str('Increases stability during braking and turn-in in corner entry phases, but also increases throttle-steer and oversteer in corner exit phases.')
]

decrease_diff_preload = [
    np.array([
        [ -0.5, -1, 0, 1, 1,],
        [ -0.5, -1, 0, 1, 1,],
        [ -0.5, -1, 0, 1, 1,],
        [ -0.5, -1, 0, 1, 1,]
    ]),
    0,
    0,
    str('Decrease differential preload one step.'),
    str('Decreases stability during braking and turn-in in corner entry phases (quicker rotation), but also decreases throttle-steer and oversteer in corner exit phases. Lowering this parameter too much can cause "one-tire-fires" akin to an open differential during power application.')
]

### AERODYNAMIC TUNING PARAMETERS ###

increase_wingAOA = [
    np.array([
        [ 0, 0, 0, 0, 0,],
        [ 0.25, 0.25, 0.25, 0.25, 0.25,],
        [ 0.5, 0.5, 0.5, 0.5, 0.5,],
        [ 1, 1, 1, 1, 1,]
    ]),
    0,
    1,
    str('Increase rear wing angle of attack one position.'),
    str('Increases rear grip and understeer during all corner phases at the expense of straight-line speed. Downforce effects increase exponentially with vehicle speed, and should not be used to fix low-speed behaviors.')
]

decrease_wingAOA = [
    np.array([
        [ 0, 0, 0, 0, 0,],
        [ -0.25, -0.25, -0.25, -0.25, -0.25,],
        [ -0.5, -0.5, -0.5, -0.5, -0.5,],
        [ -1, -1, -1, -1, -1,]
    ]),
    0,
    -1,
    str('Decrease rear wing angle of attack one position.'),
    str('Decreases rear grip and understeer during all corner phases while increasing straight-line speed. Downforce effects increase exponentially with vehicle speed, and should not be used to fix low-speed behaviors.')
]

#decrease_wingAOA = -increase_wingAOA

tuning_options = [
    null,
    brake_bias_forward, brake_bias_rearward,
    stiffen_front_ARB, soften_front_ARB,
    stiffen_rear_ARB, soften_rear_ARB,
    increase_front_negative_camber,
    increase_diff_preload, decrease_diff_preload,
    increase_wingAOA, decrease_wingAOA
]