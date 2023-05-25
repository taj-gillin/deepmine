import numpy as np
import tensorflow as tf

class NumberClassifier(tf.keras.Model):
    def __init__(self, decoder, **kwargs):
        super().__init__(**kwargs)

        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(),
            # tf.keras.layers.Dense(100, activation='relu'),
            # tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(10, activation='sigmoid')
        ])

        self.optimizer = tf.keras.optimizers.Adam(0.001)
        self.loss_function = tf.keras.losses.CategoricalCrossentropy()
        self.accuracy_function = tf.keras.metrics.CategoricalAccuracy()

    @tf.function
    def call(self, inputs):
        return self.model(inputs) 

    def train(self, inputs, labels, batch_size=256):
        """
        Runs through one epoch - all training examples.

        :param model: the initialized model to use for forward and backward pass
        :param inputs: train images of shape (num_inputs, 28, 28)
        :param train_images: train labels of shape (num_inputs, 10) 
        :return: None
        """

        num_batches = int(len(inputs)/ batch_size)

        total_loss = total_seen = total_correct = 0


        for index, end in enumerate(range(batch_size, len(inputs)+1, batch_size)):
            start = end - batch_size
            batch_inputs = inputs[start:end]
            batch_labels = labels[start:end]

            

            with tf.GradientTape() as tape:
                pred = self.call(batch_inputs)
                loss = self.loss_function(batch_labels, pred)
                accuracy = self.accuracy_function(batch_labels, pred)

            gradients = tape.gradient(loss, self.trainable_variables)
            self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))


            total_loss += loss

            total_seen += batch_size
            total_correct += batch_size * accuracy

            avg_acc = float(total_correct / total_seen)
            print(f"\r[Train {index+1}/{num_batches}]\t loss={total_loss:.3f}\t acc: {avg_acc:.3f}", end='')
        
        print()
        return total_loss, avg_acc

    def test(self, inputs, labels):
        """
        Runs through test data, calculates loss and accuracy

        :param model: the initialized model to use for forward and backward pass
        :param inputs: test images of shape (num_inputs, 28, 28)
        :param train_images: test labels of shape (num_inputs, 10) 
        :return: None
        """
         
        pred = self.call(inputs)
        loss = self.loss_function(labels, pred)
        accuracy = self.accuracy_function(labels, pred)

        total_count = len(inputs)

        avg_loss = float(loss)
        avg_acc = accuracy
        
        print()
        return avg_loss, avg_acc

def train_model(model, inputs, labels, epochs=1):
    '''Trains model and returns model statistics'''
    stats = []

    for epoch in range(epochs):
        print(f"Epoch {epoch+1}/{epochs}")
        stats += [model.train(inputs, labels)]
        print()

    return stats

def test_model(model, inputs, labels):
    '''Tests model and returns model statistics'''
    loss, accuracy = model.test(inputs, labels)
    return loss, accuracy

def export_model(model, folder_path='model'):
    '''Exports model to json file for later conversion to mcfunction'''
    weights = model.get_weights()

    for i in range(len(weights)):
        shape = weights[i].shape

        # Activation functions
        if i == len(weights) - 1:
            # print(f'Layer {i} (Sigmoid): {weights[i].shape}')
            # path = f'{folder_path}/{i}_sigmoid.txt'
            continue
        elif len(shape) == 1: 
            # print(f'Layer {i} (ReLU): {weights[i].shape}')
            # path = f'{folder_path}/{i}_relu.txt'
            continue
        else:
            print(f'Layer {i} (Dense): {weights[i].shape}')
            path = f'{folder_path}/{i}_dense.txt'

        np.savetxt(path, weights[i])

        # with open(path, 'r') as f:
        #     txt = f.read()
        
        # with open(path, 'w') as f:
        #     f.write(str(shape) + "\n" + txt)


if __name__ == "__main__":
    """
    Read in MNIST data, train and test model.
    """
    from preprocess import load_and_preprocess_data

    ## Read in MNIST data from preprocess.py
    train_inputs, train_labels, test_inputs, test_labels = load_and_preprocess_data()

    ## Initialize model
    model = NumberClassifier(None)

    ## Train Model
    train_agg_metrics = train_model(model, train_inputs, train_labels, epochs=2)

    export_model(model.model)

    ## Test Model
    test_agg_metrics = test_model(model, test_inputs, test_labels)
    print(f"\r Testing:\t loss={test_agg_metrics[0]:.3f}\t acc: {test_agg_metrics[1]:.3f}", end='\n')


    ## Visualize Results
    from visualize import visualize_images, visualize_metrics
    # visualize_metrics(train_agg_metrics["loss"], train_agg_metrics["acc"])
    # visualize_images(model, train_inputs, train_labels)

    
