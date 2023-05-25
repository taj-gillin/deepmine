import tensorflow as tf

DATAPACK_PATH = 'datapacks/deepmine/data/deepmine/functions/'
SCALE_FACTOR = 1000

def generate_test(test_input, test_label, placeNumber=False):
    test_input = tf.reshape(test_input, (-1, 1))
    test_input = tf.cast(test_input, tf.int32) * SCALE_FACTOR

    output = tf.argmax(test_label)

    txt = ""

    if placeNumber:
        txt += 'execute at @e[tag=deepmine.number_board] run fill ~ ~ ~ ~16 ~16 ~ air\n'
    
    # Set inputs`
    for i in range(len(test_input)):
        txt += f'scoreboard players set logits[{i}] deepmine.vars {int(test_input[i])}\n'

        if int(test_input[i]) != 0 and placeNumber:
            x_pos = i % 16
            y_pos = 16 - i // 16
            txt += f"execute at @e[tag=deepmine.number_board] run setblock ~{x_pos} ~{y_pos} ~ minecraft:black_concrete\n"

    txt += "function deepmine:call"
    txt += '\ntellraw @a [{"text": "True: ' + str(int(output)) + ' Pred: "}, {"score":{"objective": "deepmine.vars", "name": "output"}}]'

    return txt
    

if __name__ == "__main__":
    """
    Generate test input
    """
    from preprocess import load_and_preprocess_data

     ## Read in MNIST data from preprocess.py
    train_inputs, train_labels, test_inputs, test_labels = load_and_preprocess_data()

    for i in range(200):
        path = DATAPACK_PATH + f'test/{i}.mcfunction'

        txt = generate_test(test_inputs[i], test_labels[i], placeNumber=True)
        
        with open(path, 'w') as f:
            f.write(txt)

