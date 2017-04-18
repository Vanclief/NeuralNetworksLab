import fileinput
import re, copy

class Perceptron:
    def train(self):
        lines = Perceptron.process_input()
        d = int(lines[0])
        m = int(lines[1])
        n = int(lines[2])
        training_examples = Perceptron.parse_training_examples(lines, m)
        test_examples = Perceptron.parse_test_examples(lines, m)


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
                training_examples.append(line)

        return training_examples


    def parse_test_examples(lines, m):
        test_examples = []
        for index, line in enumerate(lines):
            if index > 2 + m:
                test_examples.append(line)

        return test_examples



def main():
    Perceptron().train()

if __name__ == '__main__':
    main()
