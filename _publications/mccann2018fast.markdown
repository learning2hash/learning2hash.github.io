---
layout: publication
title: Fast Rotational Sparse Coding
authors: Michael T. McCann, Vincent Andrearczyk, Michael Unser, Adrien Depeursinge
conference: Arxiv
year: 2018
bibkey: mccann2018fast
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.04374'}]
tags: []
short_authors: McCann et al.
---
We propose an algorithm for rotational sparse coding along with an efficient
implementation using steerability. Sparse coding (also called dictionary
learning) is an important technique in image processing, useful in inverse
problems, compression, and analysis; however, the usual formulation fails to
capture an important aspect of the structure of images: images are formed from
building blocks, e.g., edges, lines, or points, that appear at different
locations, orientations, and scales. The sparse coding problem can be
reformulated to explicitly account for these transforms, at the cost of
increased computation. In this work, we propose an algorithm for a rotational
version of sparse coding that is based on K-SVD with additional rotation
operations. We then propose a method to accelerate these rotations by learning
the dictionary in a steerable basis. Our experiments on patch coding and
texture classification demonstrate that the proposed algorithm is fast enough
for practical use and compares favorably to standard sparse coding.