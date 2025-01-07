import argparse
from itertools import permutations, product

if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(description="Script to combine rules for Hashcat. The result is the cartesian product of the rules.")
    parser.add_argument("-t", "--type", choices=["sequential", "permutational"], default="sequential", action="store", help="How to combine rules; '1.rule 2.rule 3.rule' passed to 'sequential' will produce '1 2 3' only, whereas 'permutational' will produce '1 2 3', '1 3 2', etc")
    parser.add_argument("-r", "--rules", action="append", help="Rule file to use; can be used multiple times")
    args = parser.parse_args()

    combineType: str = args.type
    ruleFiles = args.rules

    # Read all files
    rulesArr = [] # rulesArr = [ [rule-1-i, rule-1-ii], [rule-2-i, rule-2-ii] ]
    for ruleFile in ruleFiles:
        file = open(ruleFile, "r")

        rules = file.readlines()
        rulesToUse = []
        for rule in rules:
            rule = rule.rstrip()
            if (not rule.startswith("#")) and rule not in [":", ""]:
                rulesToUse.append(rule)
        rulesArr.append(rulesToUse)

        file.close()

    # Passthrough rule
    print(":")

    # Combine rules
    if combineType == "sequential":
        for combinedRule in product(*rulesArr): # combinedRule = rule-1-i rule-2-i rule-3-ii
            print(" ".join(combinedRule))
            pass
    else:
        numOfRuleFiles = len(rulesArr)
        for ruleFileIndices in permutations(range(0, numOfRuleFiles), numOfRuleFiles): # ruleFileIndices = [1 2 3, 1 3 2]
            rulesArrPermuted = [] # rulesArrPermuted = [ [rule-1-i, rule-1-ii], [rule-3-i, rule-3-ii], [rule-2-i, rule-2-ii] ]
            for ruleFileIndex in ruleFileIndices:
                rulesArrPermuted.append(rulesArr[ruleFileIndex])
                
            for combinedRule in product(*rulesArrPermuted): # combinedRule = rule-1-i rule-2-i rule-3-ii
                print(" ".join(combinedRule))
            