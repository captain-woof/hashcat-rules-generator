import argparse
from string import punctuation
from itertools import permutations

punctuation_simple = ["@", ".", "_", "!", "-", "#", "$", "*", "/", "+"]

if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(description="Script to generate additive special characters rules for Hashcat")
    parser.add_argument("-t", "--type", action="store", default="simple", choices=["simple", "full"], help="Type of special characters to choose; 'simple' = only most commonly used characters in password; default 'simple'")
    parser.add_argument("-n", "--number", action="store", default="1-1", help="Range of number of special characters to use; format: '1-3'; default: 1-1")
    parser.add_argument("-a", "--append", default=False, action="store_true", help="To append the characters; optional; can use with --prepend")
    parser.add_argument("-p", "--prepend", default=False, action="store_true", help="To prepend the characters; optional; can use with --append")
    args = parser.parse_args()

    typeOfCharacter = args.type
    numRange: str = args.number
    isAppend = args.append
    isPrepend = args.prepend

    # Passthrough rule
    print(":")

    # Special characters rule
    if numRange.find("-") == -1:
        print("-n/--number must be of format '1-3'")
        exit(1)
    else:
        [numRangeMin, numRangeMax] = map(lambda x: int(x), numRange.split("-"))
        if numRangeMin > numRangeMax:
            numRangeMin, numRangeMax = numRangeMax, numRangeMin
        for num in range(numRangeMin, numRangeMax + 1):
            for sequence in permutations(punctuation if typeOfCharacter == "full" else punctuation_simple, num): # sequence = (! @ %)
                if isAppend:
                    print(" ".join(["${}".format(character) for character in sequence]))
                if isPrepend:
                    print(" ".join(["^{}".format(character) for character in sequence]))
                if isAppend and isPrepend:
                    print(" ".join(["^{} ${}".format(character, character) for character in sequence]))



