import numpy as np

DATAPACK_PATH = 'datapacks/deepmine/data/deepmine/functions/'
SCALE_FACTOR = 1000

if __name__ == "__main__":
    """
    Generate picture reading function
    """

    txt = ""

    for i in range(256):
        x_pos = i % 16
        y_pos = 16 - i // 16

        txt += f'scoreboard players set logits[{i}] deepmine.vars 0\n'
        txt += f'execute if block ~{x_pos} ~{y_pos} ~ minecraft:black_concrete run scoreboard players set logits[{i}] deepmine.vars {SCALE_FACTOR}\n'

    with open(DATAPACK_PATH + "entity/read.mcfunction", 'w') as f:
        f.write(txt)

