from itertools import combinations, product
import argparse

# Leet substitute maps
substituteMapSimple = {
    "a": ["4", "@"],
    "e": ["3"],
    "g": ["6"],
    "h": ["#"],
    "i": ["1", "!"],
    "o": ["0"],
    "s": ["$", "5"],
    "t": ["+", "7"],
    "z": ["2"]
}
substituteMapFull = {
    "a": ["4", "@"],
    "b": ["8", "6"],
    "c": ["[", "x", "X"],
    "e": ["3", "£", "€"],
    "g": ["6", "9", "&"],
    "h": ["#"],
    "i": ["|", "1", "!"],
    "j": ["]"],
    "k": ["x", "X"],
    "l": ["|", "1", "7", "£"],
    "o": ["0", "Ø"],
    "p": ["9"],
    "q": ["&"],
    "r": ["Я"],
    "s": ["$", "5"],
    "t": ["+", "7"],
    "z": ["2"]
}

# Function to generate rules
# substituteMap = substitute map to use
# numOfSubstitutions = number of substitutions to perform
def generateRules(substituteMap, numOfSubstitutions):
    for combination in combinations(list(substituteMap.keys()), numOfSubstitutions): # combination = characters that can be substituted; abc, abd, abe...
        rule = []

        substitutions = [] # [ [4, @], [8, 6], [[, x, X] ] for combination=abc
        for characterToSubstitute in combination:
            substitutions.append(substituteMap[characterToSubstitute])

        for combinationSubstituted in product(*substitutions): # combinationSubstituted=@8[ for combination=abc
            rule.clear()
            for i in range(len(combination)):
                rule.append("s{}{}".format(combination[i], combinationSubstituted[i]))
            print(" ".join(rule))

if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(description="Script to generate mutator leet rules for Hashcat")
    parser.add_argument("-t", "--type", choices=["simple", "full"], default="simple", action="store", help="Type of rules to generate; default is 'simple', i.e, most popular substitutions only")
    parser.add_argument("--all", action="store_true", default=False, help="Whether to generate rules for all possible substitutions (in addition to --minmax); default = false")
    parser.add_argument("--minmax", action="store_true", default=False, help="Whether to generate rules for min-max number of substitutions (in addition to --all); default = false")
    parser.add_argument("--min", type=int, action="store", default=1, help="Minimum number of substitutions to perform; for example, 'sa@ so0' is 2 substitutions")
    parser.add_argument("--max", type=int, action="store", default=3, help="Maximum number of substitutions to perform; for example, 'sa@ so0 sz2' is 3 substitutions")
    args = parser.parse_args()

    type = args.type
    all = args.all
    minmax = args.minmax
    minNumOfSubstitutions = args.min
    maxNumOfSubstitutions = args.max

    # Generate rules
    ## Passthrough rule
    print(":")
    ## Generate rules for all substitutions (complete leek, leaving nothing not converted)
    if all:
        generateRules(
            substituteMapFull if type == "full" else substituteMapSimple,
            len(substituteMapFull.keys()) if type == "full" else len(substituteMapSimple.keys()),
        )
    ## Generate rules for min to max number of substitutions
    if minmax:
        for numOfSubstitutions in range(minNumOfSubstitutions, maxNumOfSubstitutions + 1):
            generateRules(substituteMapFull if type == "full" else substituteMapSimple, numOfSubstitutions)

