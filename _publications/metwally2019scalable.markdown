---
layout: publication
title: Scalable Similarity Joins Of Tokenized Strings
authors: Ahmed Metwally, Chun-Heng Huang
conference: 2019 IEEE 35th International Conference on Data Engineering (ICDE)
year: 2019
bibkey: metwally2019scalable
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.09238'}]
tags: ["Efficiency"]
short_authors: Ahmed Metwally, Chun-Heng Huang
---
This work tackles the problem of fuzzy joining of strings that naturally
tokenize into meaningful substrings, e.g., full names. Tokenized-string joins
have several established applications in the context of data integration and
cleaning. This work is primarily motivated by fraud detection, where attackers
slightly modify tokenized strings, e.g., names on accounts, to create numerous
identities that she can use to defraud service providers, e.g., Google, and
LinkedIn. To detect such attacks, all the accounts are pair-wise compared, and
the resulting similar accounts are considered suspicious and are further
investigated. Comparing the tokenized-string features of a large number of
accounts requires an intuitive tokenized-string distance that can detect subtle
edits introduced by an adversary, and a very scalable algorithm. This is not
achievable by existing distance measure that are unintuitive, hard to tune, and
whose join algorithms are serial and hence unscalable. We define a novel
intuitive distance measure between tokenized strings, Normalized Setwise
Levenshtein Distance (NSLD). To the best of our knowledge, NSLD is the first
metric proposed for comparing tokenized strings. We propose a scalable
distributed framework, Tokenized-String Joiner (TSJ), that adopts existing
scalable string-join algorithms as building blocks to perform NSLD-joins. We
carefully engineer optimizations and approximations that dramatically improve
the efficiency of TSJ. The effectiveness of the TSJ framework is evident from
the evaluation conducted on tens of millions of tokenized-string names from
Google accounts. The superiority of the tokenized-string-specific TSJ framework
over the general-purpose metric-spaces joining algorithms has been established.