import argparse

if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(description="Script to generate additive number rules for Hashcat")
    parser.add_argument("-y", "--years", default=None, action="store", help="Range of years to use; format: '1950-2020'; optional")
    parser.add_argument("-d", "--digits", default=None, action="store", help="Range of number of digits; to generate 00-999 (includes 000), use '2-3'; optional")
    parser.add_argument("-a", "--append", default=False, action="store_true", help="To append the numbers; optional; can use with --prepend")
    parser.add_argument("-p", "--prepend", default=False, action="store_true", help="To prepend the numbers; optional; can use with --append")
    args = parser.parse_args()

    yearsRange: str = args.years
    numOfDigitsRange = args.digits
    isAppend = args.append
    isPrepend = args.prepend

    # Passthrough rule
    print(":")

    # Generate rules for years
    if yearsRange is not None:
        if yearsRange.find("-") == -1:
            print("-y/--years must be of format '1950-2020'")
            exit(1)
        else:
            [yearMin, yearMax] = map(lambda x: int(x), yearsRange.split("-"))

            if yearMin > yearMax:
                yearMin, yearMax = yearMax, yearMin

            for year in range(yearMin, yearMax + 1):
                if isAppend:
                    print("${}".format(year))
                if isPrepend:
                    print("^{}".format(year))
                if isAppend and isPrepend:
                    print("^{} ${}".format(year, year))

    # Generate rules for numbers
    if numOfDigitsRange is not None:
        if numOfDigitsRange.find("-") == -1:
            print("-r/--range must be of format '2-3'")
            exit(1)
        else:
            [numOfDigitsMin, numOfDigitsMax] = map(lambda x: int(x), numOfDigitsRange.split("-"))
            if numOfDigitsMin > numOfDigitsMax:
                numOfDigitsMin, numOfDigitsMax = yearMax, numOfDigitsMin

            for numOfDigits in range(numOfDigitsMin, numOfDigitsMax + 1):
                for num in range(0, int("9" * numOfDigits) + 1):
                    numStr = str(num).rjust(numOfDigits, "0")
                    if isAppend:
                        print("${}".format(numStr))
                    if isPrepend:
                        print("^{}".format(numStr))
                    if isAppend and isPrepend:
                        print("^{} ${}".format(numStr, numStr))

