---
layout: publication
title: Streaming Similarity Self-join
authors: Morales Gianmarco de Francisci, Gionis Aristides
conference: Proceedings of the VLDB Endowment
year: 2016
bibkey: morales2016streaming
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.04814'}]
tags: [DATASETS, Tools & Libraries]
---
We introduce and study the problem of computing the similarity self-join in a
streaming context (SSSJ), where the input is an unbounded stream of items
arriving continuously. The goal is to find all pairs of items in the stream
whose similarity is greater than a given threshold. The simplest formulation of
the problem requires unbounded memory, and thus, it is intractable. To make the
problem feasible, we introduce the notion of time-dependent similarity: the
similarity of two items decreases with the difference in their arrival time. By
leveraging the properties of this time-dependent similarity function, we design
two algorithmic frameworks to solve the sssj problem. The first one, MiniBatch
(MB), uses existing index-based filtering techniques for the static version of
the problem, and combines them in a pipeline. The second framework, Streaming
(STR), adds time filtering to the existing indexes, and integrates new
time-based bounds deeply in the working of the algorithms. We also introduce a
new indexing technique (L2), which is based on an existing state-of-the-art
indexing technique (L2AP), but is optimized for the streaming case. Extensive
experiments show that the STR algorithm, when instantiated with the L2 index,
is the most scalable option across a wide array of datasets and parameters.