from chassis_balance import chassis_initial_state
from tuning_masks import tuning_options

def check_dims(mat1, mat2):

    assert len(mat2) == len(mat1)
    assert len(mat2[0]) == len(mat1[0])

def loss_to_neutral(state):

    balance_loss =  sum(sum((state[0]**2)))
    stiffness_loss = state[1]**2
    drag_loss = state[2]**2

    return balance_loss + stiffness_loss + drag_loss

def make_adjustment(initial, tuning):

    new_state = [
    initial[0] + tuning[0],
    initial[1] + tuning[1],
    initial[2] + tuning[2],
    tuning[3],
    tuning[4]
    ]

    check_dims(mat1=initial, mat2=new_state)

    return new_state

def chose_tuning_option(initial_state, all_tuning_options):
    
    best_loss = loss_to_neutral(initial_state)

    for option in all_tuning_options:
        option_loss = loss_to_neutral(make_adjustment(initial=initial_state, tuning=option))
        if option_loss <= best_loss:
            best_tuning_option = option
            best_loss = option_loss

    check_dims(mat1=initial_state, mat2=best_tuning_option)

    return best_tuning_option

def neutralize(iterations, initial_state, tuning_options):

    new_state = initial_state
    masks=[]
    steps=[]
    descriptions=[]

    for i in range(iterations):
        tuning_option = chose_tuning_option(initial_state=new_state, all_tuning_options=tuning_options)
        if tuning_option[3] == None:
            print('''
########## Optimizer Complete. Please READ BELOW TIPS for applying tuning changes. ########## \n
We typically encourage to make the most significant changes (Iteration 1 and 2) first, then assess the change in handling, update the handling matrix, and perform the optimization again until the car is optimized to the driver's liking (near-0 handling matrix). Since Neutralize is agnostic to the sensitivities of any simulated car to its tuning parameters, each successive result (Iterations 3, 4...) loses accuracy. Applying multiple changes at once might be appropriate only if the chassis is significantly difficult to drive, inconsistent, or slow.

Decide for yourself what a significant "step" is by paying attention to the sensitivity of each recommended change. For example, increasing a sway bar's stiffness "one step" might be very significant in a Porsche Cup Car which has 7 possible adjustments, but less significant in an Aston Martin DBR9 which has 30 possible adjustments, and so you might change the setting by two "steps" at a time on the Aston Martin. The point is to make a small but noticeable change.

Allow time for the driver to adjust to the new vehcile parameters after each change before updating the handling matrix. Some changes might 'feel' better but actually be slower; always refer to lap times as the ultimate measure of a good tuning setup.
            ''')
            break
        else:
            masks.append((tuning_option[0], tuning_option[1], tuning_option[2]))
            new_state = make_adjustment(initial=new_state, tuning=tuning_option)
            steps.append(new_state[3])
            descriptions.append(new_state[4])
            print(f'''
########## In iteration {i+1}, ##########\n
The tuning step: "{new_state[3]}" was the most effective in reducing the handling matrix loss. Description: "{new_state[4]}" \n
Tuning step delta:\n {tuning_option[:3]} \n
Handling matrix after tuning step is applied will be approximately:\n {new_state[:3]}
            ''')

    return new_state[:3], masks, steps, descriptions

neutralize(iterations=100, initial_state=chassis_initial_state, tuning_options=tuning_options)
