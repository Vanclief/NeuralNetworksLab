import fileinput
import re, copy

class Perceptron:
    def train(self):
        lines = Perceptron.process_input()
        print (lines)

    def process_input():
        lines = []

        for line in fileinput.input():
            lines.append(line)

        lines = list(map(lambda x: x.strip('').rstrip('\n').rstrip('\r').replace(' ', ''), lines))

        return lines


def main():
    Perceptron().train()

if __name__ == '__main__':
    main()
