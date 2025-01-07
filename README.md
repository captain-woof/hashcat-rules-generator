# How to use

Rulesets are divided into 2 categories:
    - mutators
    - additives

These rules are meant to be used in a [pipeline](#pipeline-approach) for most effective results.

# How to use rule

```
hashcat -a 0 -r some.rule --force --stdout wordlist_base.txt
```

# Rule types

## Mutators

These rules take a word and mutate something in it. The total length of the word is unchanged.

As an example, these rules can make "california" into "California" or "cal!forn!a"

## Additives

These rules take a word and prepend/append something to it. The total length of the word is changed.

As an example, these rules can make "California" into "California1969"

# Pipeline approach

To generate most effective wordlists, it's essential to follow these steps:

1. Generate a base wordlist comprising of only lowercase words; no gimmicks.
2. Feed this base wordlist to a mutator rule to generate mutated wordlist.
3. Feed the mutated wordlist to an additive wordlist to generate final wordlist.

# Rule generators

Additionally, there are some rule generating scripts included to generate your own rules. Each generator has a specific purpose. In addition, there is a combining script that can combine multiple rule files.

# Contribution

Generating effective wordlists can be a pain. If you have any ideas, scripts, rules to add, please feel free to contribute them here.

# References

- [https://hashcat.net/wiki/doku.php?id=rule_based_attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack)
- [https://en.wikipedia.org/wiki/Leet](https://en.wikipedia.org/wiki/Leet)