---
layout: publication
title: 'Ganzzle: Reframing Jigsaw Puzzle Solving As A Retrieval Task Using A Generative
  Mental Image'
authors: Davide Talon, Alessio del Bue, Stuart James
conference: 2022 IEEE International Conference on Image Processing (ICIP)
year: 2022
bibkey: talon2022ganzzle
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.05634'}]
tags: [Scalability, Neural Hashing, Datasets, Robustness]
short_authors: Davide Talon, Alessio del Bue, Stuart James
---
Puzzle solving is a combinatorial challenge due to the difficulty of matching
adjacent pieces. Instead, we infer a mental image from all pieces, which a
given piece can then be matched against avoiding the combinatorial explosion.
Exploiting advancements in Generative Adversarial methods, we learn how to
reconstruct the image given a set of unordered pieces, allowing the model to
learn a joint embedding space to match an encoding of each piece to the cropped
layer of the generator. Therefore we frame the problem as a R@1 retrieval task,
and then solve the linear assignment using differentiable Hungarian attention,
making the process end-to-end. In doing so our model is puzzle size agnostic,
in contrast to prior deep learning methods which are single size. We evaluate
on two new large-scale datasets, where our model is on par with deep learning
methods, while generalizing to multiple puzzle sizes.