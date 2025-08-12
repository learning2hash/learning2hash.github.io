---
layout: publication
title: 'Fuzzingdriver: The Missing Dictionary To Increase Code Coverage In Fuzzers'
authors: Arash Ale Ebrahim, Mohammadreza Hazhirpasand, Oscar Nierstrasz, Mohammad
  Ghafari
conference: Arxiv
year: 2022
bibkey: ebrahim2022fuzzingdriver
citations: 0
additional_links: [{name: Code, url: 'https://www.youtube.com/watch?v=Y8j_KvfRrI8'},
  {name: Paper, url: 'https://arxiv.org/abs/2201.04853'}]
tags: ["Efficiency", "Tools & Libraries"]
short_authors: Ebrahim et al.
---
We propose a tool, called FuzzingDriver, to generate dictionary tokens for
coverage-based greybox fuzzers (CGF) from the codebase of any target program.
FuzzingDriver does not add any overhead to the fuzzing job as it is run
beforehand. We compared FuzzingDriver to Google dictionaries by fuzzing six
open-source targets, and we found that FuzzingDriver consistently achieves
higher code coverage in all tests. We also executed eight benchmarks on
FuzzBench to demonstrate how utilizing FuzzingDriver's dictionaries can
outperform six widely-used CGF fuzzers. In future work, investigating the
impact of FuzzingDriver's dictionaries on improving bug coverage might prove
important. Video demonstration: https://www.youtube.com/watch?v=Y8j_KvfRrI8