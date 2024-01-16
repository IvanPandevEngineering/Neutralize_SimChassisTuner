'''
This document defines the user-reported balance of the chassis at the initial setup, expressed in a matrix, to which tuning masks will be applied.

The user is prompted to qualitatively report all vehicle properties according to their scales, to form the initial vehicle state in the handling matrix below.
NeutralizeSimChassisTuning optimizes towards the ideal of each scale, 0.
Matrix form defined below:

    [  Initial braking, turn-in, mid-corner, corner-exit-inital, throttle-out
       Unstable(-5) <-----> Neutral(0) <-----> Stable(5)
        [ _, _, _, _, _,],  0-40 mph
        [ _, _, _, _, _,],  40-60 mph
        [ _, _, _, _, _,],  60-80 mph
        [ _, _, _, _, _,]  90+ mph
    ],
    [ _,], Suspension stiffness bias, Too Soft(-5) <-----> Neutral(0) <-----> Too Stiff(5)
    [ _,]  Downforce/drag bias, Insufficient Downforce(-5) <-----> Neutral(0) <-----> Excessive Drag(5)

How to fill each value:

Initial braking: This describes braking in a straight line, from initial brake application until the first steering action. Instability in this phase is felt as the rear brakes locking up before the fronts, sometimes described as 'the back stepping out'. Stability in this phase is the front brakes locking up before the rears. Even if the brakes don't lock fully, there might be partial brake locking in this phase, perhaps over rough road or curbs, felt as the car 'wiggling' or 'sliding' under braking.

Turn-in: This describes the trail-braking period of the corner, where braking and steering effects have significant overlap, generally before the apex of the corner. Although driving technique largely influences oversteer (instability) or understeer (stability) in this cornering phase, the driver will still have a perference for the chassis' willingness to rotate, and setup changes can define this behavior. Instability in this phase is felt as the chassis rotating too quickly for the user to control, stability is felt as the chassis needing excessive inputs to reach the desired rotation, or never reaching the desired rotation at all. Report on a scale of -5 to 5, 0 being ideal (neutral steer), for an array of speed ranges.

Mid-corner: This describes the phase of cornering near the apex, around the transition from braking inputs to throttle inputs. This phase shuold not be mistaken for 'coasting,' which is to be avoided in a driver's technique. Report on a scale of -5 to 5, 0 being ideal (neutral steer), for an array of speed ranges.

Corner-exit-intial: This describes the phase of cornering where throttle and steering effects have significant overlap, but before full throttle is ultiamtely applied. There is significant 'throttle-steer' in this phase, with gradual reduction of steering input back to straight. Instability in this phase is felt as the throttle causing too much rotation, stability is felt as the throttle transfering weight rearward, accelerating the car forward but with excessive understeer. Report on a scale of -5 to 5, 0 being ideal (neutral steer), for an array of speed ranges.

Throttle-out: This describes a phase of cornering which not all corners have; a full-throttle exit where significant rotation is still necessary, but the throttle input can (or should) be comfortably flat-out. Think of Monza's parabolica or Spa's Pouhon as examples. In this phase, instability is felt as the throttle input threatening to spin the car and causing the driver to lift, stability is felt as excessive steering input which overheats the front tires or causes the driver to lift. Report on a scale of -5 to 5, 0 being ideal (neutral steer), for an array of speed ranges.

Suspension stiffness bias: The driver must report if they desire to bias for tuning choices which stiffen or soften the suspension. In effect, the driver must compromise between consistency over bumps and curbs (softer settings), and chassis responsiveness (stiffer settings). There are aerodynamic implications for suspension stiffness as well, but those are beyond the scope of this tool. Report on a scale of -5 for wanting stiffer chassis tuning choices, 5 for wanting softer chassis tuning choices, 0 being the ideal compromise. As a personal note, I like to soften the chassis as much as possible without introducing response issues, such as not being able to take left-right transitions in chicanes well.

Downforce/drag bias: Not to be confused with aerodynamic over/understeer balance, which is optimized in the chassis balance matrix (in the speed dimension). The driver must report if they desire to bias towards tuning choices creating more or less downforce and drag. Report on a scale of -5 for desiring more downforce to 5 for desiring less drag, 0 being the ideal downforce/drag compromise. The user must decide for themselves what that ideal downforce/drag comporomise must be. As a personal note, I like to establish lap times for a sweep of compromises, and choose the lowest-drag setup which is within a tenth of the lowest overall lap time. This rule-of-thumb produces a chassis which is quick but less likely to be overtaken on long straights.
'''

import numpy as np

chassis_initial_state = [
    np.array([
        [ 0, 2, 2, 2, 2,],
        [ 0, 2, 2, 2, 2,],
        [ 0, 3, 3, 3, 3,],
        [ 0, 3, 3, 3, 3,],
    ]),
    0,
    0,
    None,
    None
]

def get_user_reported_balance():
    return