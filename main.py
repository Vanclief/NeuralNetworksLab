import fileinput
import re, copy
import random

class Perceptron:
    def train(self):

        lines = Perceptron.process_input()

        d = int(lines[0]) # Size of input
        m = int(lines[1]) # Size of training set
        n = int(lines[2]) # Size of test set

        training_examples = Perceptron.parse_training_examples(lines, m)
        test_examples = Perceptron.parse_test_examples(lines, m)

        weights = Perceptron.initialize_weights(d)
        print(weights)


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

    # def calculate_output():
        # print()

    # def update_weight():
        # print()


def main():
    Perceptron().train()

if __name__ == '__main__':
    main()
