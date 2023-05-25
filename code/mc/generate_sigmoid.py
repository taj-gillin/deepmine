import numpy as np

SCALE_FACTOR = 1000

if __name__ == "__main__":
    """
    Generate sigmoid function
    """

    txt = f'execute if score input deepmine.vars matches ..-{7 * SCALE_FACTOR} run scoreboard players set output deepmine.vars {5 * SCALE_FACTOR}\n'

    for i in range(-7 * SCALE_FACTOR, 7 * SCALE_FACTOR + 1):
        txt += f'execute if score input deepmine.vars matches {i} run scoreboard players set output deepmine.vars {int(SCALE_FACTOR / (1 + np.exp(-i / SCALE_FACTOR)))}\n'

    with open("mcfunction/functions/sigmoid.mcfunction", 'w') as f:
        f.write(txt)

