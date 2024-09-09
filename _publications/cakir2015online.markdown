---
layout: publication
title: "Online Supervised Hashing for Ever-Growing Datasets"
authors: Cakir Fatih, Bargal Sarah Adel, Sclaroff Stan
conference: Arxiv
year: 2015
bibkey: cakir2015online
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1511.03257"}
tags: ['ARXIV', 'Supervised', 'Unsupervised']
---
Supervised hashing methods are widely-used for nearest neighbor search in
computer vision applications. Most state-of-the-art supervised hashing
approaches employ batch-learners. Unfortunately, batch-learning strategies can
be inefficient when confronted with large training datasets. Moreover, with
batch-learners, it is unclear how to adapt the hash functions as a dataset
continues to grow and diversify over time. Yet, in many practical scenarios the
dataset grows and diversifies; thus, both the hash functions and the indexing
must swiftly accommodate these changes. To address these issues, we propose an
online hashing method that is amenable to changes and expansions of the
datasets. Since it is an online algorithm, our approach offers linear complexity
with the dataset size. Our solution is supervised, in that we incorporate
available label information to preserve the semantic neighborhood. Such an
adaptive hashing method is attractive; but it requires recomputing the hash
table as the hash functions are updated. If the frequency of update is high,
then recomputing the hash table entries may cause inefficiencies in the system,
especially for large indexes. Thus, we also propose a framework to reduce hash
table updates. We compare our method to state-of-the-art solutions on two
benchmarks and demonstrate significant improvements over previous work.
