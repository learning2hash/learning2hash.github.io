---
layout: publication
title: 'Semdiff: Binary Similarity Detection By Diffing Key-semantics Graphs'
authors: Zian Liu, Zhi Zhang, Siqi Ma, Dongxi Liu, Jun Zhang, Chao Chen, Shigang Liu,
  Muhammad Ejaz Ahmed, Yang Xiang
conference: Arxiv
year: 2023
bibkey: liu2023semdiff
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.01463'}]
tags: ["Evaluation", "Graph Based ANN", "Tools & Libraries"]
short_authors: Liu et al.
---
Binary similarity detection is a critical technique that has been applied in
many real-world scenarios where source code is not available, e.g., bug search,
malware analysis, and code plagiarism detection. Existing works are ineffective
in detecting similar binaries in cases where different compiling optimizations,
compilers, source code versions, or obfuscation are deployed.
  We observe that all the cases do not change a binary's key code behaviors
although they significantly modify its syntax and structure. With this key
observation, we extract a set of key instructions from a binary to capture its
key code behaviors. By detecting the similarity between two binaries' key
instructions, we can address well the ineffectiveness limitation of existing
works. Specifically, we translate each extracted key instruction into a
self-defined key expression, generating a key-semantics graph based on the
binary's control flow. Each node in the key-semantics graph denotes a key
instruction, and the node attribute is the key expression. To quantify the
similarity between two given key-semantics graphs, we first serialize each
graph into a sequence of key expressions by topological sort. Then, we tokenize
and concatenate key expressions to generate token lists. We calculate the
locality-sensitive hash value for all token lists and quantify their
similarity. %We implement a prototype, called SemDiff, consisting of two
modules: graph generation and graph diffing. The first module generates a pair
of key-semantics graphs and the second module diffs the graphs. Our evaluation
results show that overall, SemDiff outperforms state-of-the-art tools when
detecting the similarity of binaries generated from different optimization
levels, compilers, and obfuscations. SemDiff is also effective for library
version search and finding similar vulnerabilities in firmware.