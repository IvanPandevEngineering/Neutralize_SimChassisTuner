from chassis_balance import chassis_initial_state
from tuning_masks import tuning_options

def check_dims(initial, new_state):

    assert len(new_state) == len(initial)
    assert len(new_state[0]) == len(initial[0])

def loss_to_neutral(state):

    balance_loss =  sum(sum((state[0]**2)))
    stiffness_loss = state[1]**2
    drag_loss =  state[2]**2

    return balance_loss + stiffness_loss + drag_loss

def make_adjustment(initial, tuning):

    new_state = [
    initial[0] + tuning[0],
    initial[1] + tuning[1],
    initial[2] + tuning[2],
    None,
    None
    ]

    check_dims(initial=initial, new_state=new_state)

    return new_state

def chose_tuning_option(initial_state, tuning_options):
    
    best_loss = loss_to_neutral(initial_state)

    for option in tuning_options:
        option_loss = loss_to_neutral(make_adjustment(initial=initial_state, tuning=option))
        if option_loss < best_loss:
            best_tuning_option = option
            best_loss = option_loss
    
    return best_tuning_option

def neutralize(iterations, initial_state, tuning_options):

    new_state = initial_state

    for all in range(iterations):
        new_state = make_adjustment(initial=new_state, tuning=chose_tuning_option(initial_state=new_state, tuning_options=tuning_options))

    return new_state

print(neutralize(iterations=2, initial_state=chassis_initial_state, tuning_options=tuning_options))
