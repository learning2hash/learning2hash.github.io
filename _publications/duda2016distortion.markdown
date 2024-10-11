---
layout: publication
title: Distortion-resistant Hashing For Rapid Search Of Similar DNA Subsequence
authors: Duda Jarek
conference: "Arxiv"
year: 2016
bibkey: duda2016distortion
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1602.05889"}
tags: ['ARXIV', 'Independent']
---
One of the basic tasks in bioinformatics is localizing a short subsequence $S$, read while sequencing, in a long reference sequence $R$, like the human geneome. A natural rapid approach would be finding a hash value for $S$ and compare it with a prepared database of hash values for each of length $|S|$ subsequences of $R$. The problem with such approach is that it would only spot a perfect match, while in reality there are lots of small changes: substitutions, deletions and insertions. This issue could be repaired if having a hash function designed to tolerate some small distortion accordingly to an alignment metric (like Needleman-Wunch): designed to make that two similar sequences should most likely give the same hash value. This paper discusses construction of Distortion-Resistant Hashing (DRH) to generate such fingerprints for rapid search of similar subsequences. The proposed approach is based on the rate distortion theory: in a nearly uniform subset of length $|S|$ sequences, the hash value represents the closest sequence to $S$. This gives some control of the distance of collisions: sequences having the same hash value.
