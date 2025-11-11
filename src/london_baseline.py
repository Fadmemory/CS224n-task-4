# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import random
import argparse


# random.seed(0)

def main():
    accuracy = 0.0
    count=0
    bingo=0
    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    for line,line2 in zip(open("birth_dev.tsv", encoding='utf-8'),open("vanilla.nopretrain.dev.predictions", encoding='utf-8')):
        x = line.split('?')[1].strip()
        y = line2
        # print(x,y)
        if x == "London":
            count+=1
            if y=="London":
                bingo+=1
    accuracy = (bingo/count)*100
    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
