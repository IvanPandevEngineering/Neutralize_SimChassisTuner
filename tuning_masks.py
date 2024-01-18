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
        [ -.25, -1, -1, -1, -1,],
        [ -.25, -1, -1, -1, -1,],
        [ -.25, -1, -1, -1, -1,],
        [ -.25, -1, -1, -1, -1,]
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

### DIFFERENTIAL TUNING PARAMETERS ###

increase_preload = [
    [
        [ 0.5, 1, 0, -1, -1,],
        [ 0.5, 1, 0, -1, -1,],
        [ 0.5, 1, 0, -1, -1,],
        [ 0.5, 1, 0, -1, -1,]
    ],
    [0],
    [0]
]

#decrease_preload = -increase_preload

### AERODYNAMIC TUNING PARAMETERS ###

increase_wingAOA = [
    [
        [ 0, 0, 0, 0, 0,],
        [ 0.25, 0.25, 0.25, 0.25, 0.25,],
        [ 0.5, 0.5, 0.5, 0.5, 0.5,],
        [ 1, 1, 1, 1, 1,]
    ],
    [0],
    [1]
]

#decrease_wingAOA = -increase_wingAOA

tuning_options = [
    brake_bias_forward,
    stiffen_front_ARB, soften_front_ARB,
    stiffen_rear_ARB, soften_rear_ARB
]