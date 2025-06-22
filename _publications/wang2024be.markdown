---
layout: publication
title: To Be Continuous, Or To Be Discrete, Those Are Bits Of Questions
authors: Yiran Wang, Masao Utiyama
conference: Arxiv
year: 2024
citations: 1
bibkey: wang2024be
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.07812'}]
tags: [Hashing Methods, Loss Functions, ANN Search]
---
Recently, binary representation has been proposed as a novel representation
that lies between continuous and discrete representations. It exhibits
considerable information-preserving capability when being used to replace
continuous input vectors. In this paper, we investigate the feasibility of
further introducing it to the output side, aiming to allow models to output
binary labels instead. To preserve the structural information on the output
side along with label information, we extend the previous contrastive hashing
method as structured contrastive hashing. More specifically, we upgrade CKY
from label-level to bit-level, define a new similarity function with span
marginal probabilities, and introduce a novel contrastive loss function with a
carefully designed instance selection strategy. Our model achieves competitive
performance on various structured prediction tasks, and demonstrates that
binary representation can be considered a novel representation that further
bridges the gap between the continuous nature of deep learning and the discrete
intrinsic property of natural languages.