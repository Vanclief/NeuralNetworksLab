import fileinput
import re, copy
import random

class Perceptron:
    def train(self):

        lines = Perceptron.process_input()

        d = int(lines[0]) # Size of input
        m = int(lines[1]) # Size of training set
        n = int(lines[2]) # Size of test set
        learning_rate = 0.2

        training_examples = Perceptron.parse_training_examples(lines, m)
        test_examples = Perceptron.parse_test_examples(lines, m)

        weights = Perceptron.initialize_weights(d)

        for x in range(0, 100):
            for training_vector in training_examples:

                inputs = training_vector[:d+1]
                target = training_vector[-1]

                output = Perceptron.calculate_output(
                        inputs,
                        weights
                        )
                if abs(target - output) > 0.0001:
                    weights = Perceptron.update_weights(
                            inputs,
                            target,
                            weights,
                            output,
                            learning_rate
                            )


    def process_input():
        lines = []

        for line in fileinput.input():
            lines.append(line)

        lines = list(map(lambda x: x.strip('').rstrip('\n').rstrip('\r').replace(' ', ''), lines))

        return lines

    def parse_training_examples(lines, m):
        training_examples = []
        for index, line in enumerate(lines):
            if index > 2 and index < 3 + m:
                inputs = [int(x) for x in line.split(',')]
                inputs = Perceptron.add_bias(inputs)
                training_examples.append(inputs)

        return training_examples


    def parse_test_examples(lines, m):
        test_examples = []

        for index, line in enumerate(lines):
            if index > 2 + m:
                inputs = [int(x) for x in line.split(',')]
                inputs = Perceptron.add_bias(inputs)
                test_examples.append(inputs)

        return test_examples

    def add_bias(example):
        example.insert(0, 1)
        return example

    def initialize_weights(d):
        weights = []
        for i in range(d + 1):
            weights.append(random.uniform(-1.0, 1.0))
        return weights

    def calculate_output(vector, weights):
        output = 0

        for i, x in enumerate(vector):
            output += x * weights[i]

        return output

    def update_weights(inputs, target, weights, output, learning_rate):

        for i, weight in enumerate(weights):
            weights[i] = learning_rate * (target - output) * inputs[i]

        return weights


def main():
    Perceptron().train()

if __name__ == '__main__':
    main()
