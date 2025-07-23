---
layout: publication
title: Stochastic Generative Hashing
authors: Dai Bo, Guo Ruiqi, Kumar Sanjiv, He Niao, Song Le
conference: Arxiv
year: 2017
bibkey: dai2017stochastic
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.02815'}]
tags: ["Efficiency", "Hashing Methods", "Neural Hashing", "Scalability", "Similarity Search"]
short_authors: Dai et al.
---
Learning-based binary hashing has become a powerful paradigm for fast search
and retrieval in massive databases. However, due to the requirement of discrete
outputs for the hash functions, learning such functions is known to be very
challenging. In addition, the objective functions adopted by existing hashing
techniques are mostly chosen heuristically. In this paper, we propose a novel
generative approach to learn hash functions through Minimum Description Length
principle such that the learned hash codes maximally compress the dataset and
can also be used to regenerate the inputs. We also develop an efficient
learning algorithm based on the stochastic distributional gradient, which
avoids the notorious difficulty caused by binary output constraints, to jointly
optimize the parameters of the hash function and the associated generative
model. Extensive experiments on a variety of large-scale datasets show that the
proposed method achieves better retrieval results than the existing
state-of-the-art methods.