import os
import numpy as np

SCALE_FACTOR = 1000


def generate_call(paths):
    """
    Generates main call function
    """

    txt = ""

    for path in paths:
        path = path.replace('.mcfunction', '')
        txt += f'function deepmine:call/{path}\n'

    txt += f'function deepmine:functions/argmax\n'

    return txt

def generate_relu(layer_number, weights):
    """
    Generates relu layer
    """

    txt = ""

    for i in range(weights.shape[1]):
        txt += f'execute if score logits[{i}] deepmine.vars matches ..0 run scoreboard players set logits[{i}] deepmine.vars 0\n'

    return txt

def generate_dense(layer_number, weights):
    """
    Generates dense layer
    """
    num_inputs = weights.shape[0]
    num_outputs = weights.shape[1]

    initialize_txt = ""

    # Set weight values
    for i in range(num_inputs):
        for j in range(num_outputs):
            initialize_txt += f'scoreboard players set weight_{layer_number}[{i}][{j}] deepmine.vars {int(SCALE_FACTOR * weights[i][j])}\n'

    # Calculate output values
    calculate_txt = ""

    for j in range(num_outputs):
        calculate_txt += f'scoreboard players set output[{j}] deepmine.vars 0\n'

        for i in range(num_inputs):
            calculate_txt += f'scoreboard players operation temp deepmine.vars = logits[{i}] deepmine.vars\n'
            calculate_txt += f'scoreboard players operation temp deepmine.vars *= weight_{layer_number}[{i}][{j}] deepmine.vars\n'
            calculate_txt += f'scoreboard players operation output[{j}] deepmine.vars += temp deepmine.vars\n'

        calculate_txt += f'scoreboard players operation output[{j}] deepmine.vars /= {SCALE_FACTOR} deepmine.consts\n'

    for j in range(num_outputs):
        calculate_txt += f'scoreboard players operation logits[{j}] deepmine.vars = output[{j}] deepmine.vars\n'

    return initialize_txt, calculate_txt

if __name__ == "__main__":
    """
    Read in model, create mcfunction files to call the model in Minecraft
    """

    paths = sorted(os.listdir("model"))

    call_paths = []

    for i, path in enumerate(paths):
        weights = np.loadtxt(f"model/{path}")

        path_mcfunction = path.split(".")[0] + ".mcfunction"
        call_paths.append(path_mcfunction)

        index = int(path.split("_")[0])

        # Generate dense mcfunction files
        initialize_txt, calculate_txt = generate_dense(index, weights)

        with open(f"mcfunction/init/{path_mcfunction}", 'w') as f:
            f.write(initialize_txt)
        with open(f"mcfunction/call/{path_mcfunction}", 'w') as f:
            f.write(calculate_txt)

        # Generate relu mcfunction files
        if i == len(paths) - 1:
            continue

        relu_txt = generate_relu(index, weights)

        relu_path = f'{index + 1}_relu.mcfunction'
        call_paths.append(relu_path)

        with open(f"mcfunction/call/{relu_path}", 'w') as f:
            f.write(relu_txt)

    # Generate main call function
    call_txt = generate_call(call_paths)

    with open(f"mcfunction/call.mcfunction", 'w') as f:
            f.write(call_txt)