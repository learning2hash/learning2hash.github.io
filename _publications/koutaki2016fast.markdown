---
layout: publication
title: Fast Supervised Discrete Hashing And Its Analysis
authors: Gou Koutaki, Keiichiro Shirai, Mitsuru Ambai
conference: Arxiv
year: 2016
bibkey: koutaki2016fast
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.10017'}]
tags: ["Evaluation", "Hashing Methods", "Quantization", "Scalability", "Supervised"]
short_authors: Gou Koutaki, Keiichiro Shirai, Mitsuru Ambai
---
In this paper, we propose a learning-based supervised discrete hashing
method. Binary hashing is widely used for large-scale image retrieval as well
as video and document searches because the compact representation of binary
code is essential for data storage and reasonable for query searches using
bit-operations. The recently proposed Supervised Discrete Hashing (SDH)
efficiently solves mixed-integer programming problems by alternating
optimization and the Discrete Cyclic Coordinate descent (DCC) method. We show
that the SDH model can be simplified without performance degradation based on
some preliminary experiments; we call the approximate model for this the "Fast
SDH" (FSDH) model. We analyze the FSDH model and provide a mathematically exact
solution for it. In contrast to SDH, our model does not require an alternating
optimization algorithm and does not depend on initial values. FSDH is also
easier to implement than Iterative Quantization (ITQ). Experimental results
involving a large-scale database showed that FSDH outperforms conventional SDH
in terms of precision, recall, and computation time.