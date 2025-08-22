---
layout: publication
title: Compact Neural Graphics Primitives With Learned Hash Probing
authors: "Towaki Takikawa, Thomas M\xFCller, Merlin Nimier-David, Alex Evans, Sanja\
  \ Fidler, Alec Jacobson, Alexander Keller"
conference: SIGGRAPH Asia 2023 Conference Papers
year: 2023
bibkey: takikawa2023compact
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.17241'}]
tags: ["Evaluation", "Memory Efficiency", "Quantization", "Tools & Libraries"]
short_authors: Takikawa et al.
---
Neural graphics primitives are faster and achieve higher quality when their
neural networks are augmented by spatial data structures that hold trainable
features arranged in a grid. However, existing feature grids either come with a
large memory footprint (dense or factorized grids, trees, and hash tables) or
slow performance (index learning and vector quantization). In this paper, we
show that a hash table with learned probes has neither disadvantage, resulting
in a favorable combination of size and speed. Inference is faster than unprobed
hash tables at equal quality while training is only 1.2-2.6x slower,
significantly outperforming prior index learning approaches. We arrive at this
formulation by casting all feature grids into a common framework: they each
correspond to a lookup function that indexes into a table of feature vectors.
In this framework, the lookup functions of existing data structures can be
combined by simple arithmetic combinations of their indices, resulting in
Pareto optimal compression and speed.