---
layout: publication
title: Towards Flexible Perception With Visual Memory
authors: Robert Geirhos, Priyank Jaini, Austin Stone, Sourabh Medapati, Xi Yi, George
  Toderici, Abhijit Ogale, Jonathon Shlens
conference: Arxiv
year: 2024
bibkey: geirhos2024towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.08172'}]
tags: ["Large Scale Search", "Memory Efficiency", "Scalability", "Similarity Search"]
short_authors: Geirhos et al.
---
Training a neural network is a monolithic endeavor, akin to carving knowledge
into stone: once the process is completed, editing the knowledge in a network
is nearly impossible, since all information is distributed across the network's
weights. We here explore a simple, compelling alternative by marrying the
representational power of deep neural networks with the flexibility of a
database. Decomposing the task of image classification into image similarity
(from a pre-trained embedding) and search (via fast nearest neighbor retrieval
from a knowledge database), we build a simple and flexible visual memory that
has the following key capabilities: (1.) The ability to flexibly add data
across scales: from individual samples all the way to entire classes and
billion-scale data; (2.) The ability to remove data through unlearning and
memory pruning; (3.) An interpretable decision-mechanism on which we can
intervene to control its behavior. Taken together, these capabilities
comprehensively demonstrate the benefits of an explicit visual memory. We hope
that it might contribute to a conversation on how knowledge should be
represented in deep vision models -- beyond carving it in "stone" weights.