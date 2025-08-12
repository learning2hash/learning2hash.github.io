---
layout: publication
title: 'Tokenlearner: What Can 8 Learned Tokens Do For Images And Videos?'
authors: Michael S. Ryoo, Aj Piergiovanni, Anurag Arnab, Mostafa Dehghani, Anelia
  Angelova
conference: NeurIPS 2021
year: 2021
bibkey: ryoo2021tokenlearner
citations: 50
additional_links: [{name: Code, url: 'https://github.com/google-research/scenic/tree/main/scenic/projects/token_learner'},
  {name: Paper, url: 'https://arxiv.org/abs/2106.11297'}]
tags: ["NEURIPS"]
short_authors: Ryoo et al.
---
In this paper, we introduce a novel visual representation learning which
relies on a handful of adaptively learned tokens, and which is applicable to
both image and video understanding tasks. Instead of relying on hand-designed
splitting strategies to obtain visual tokens and processing a large number of
densely sampled patches for attention, our approach learns to mine important
tokens in visual data. This results in efficiently and effectively finding a
few important visual tokens and enables modeling of pairwise attention between
such tokens, over a longer temporal horizon for videos, or the spatial content
in images. Our experiments demonstrate strong performance on several
challenging benchmarks for both image and video recognition tasks. Importantly,
due to our tokens being adaptive, we accomplish competitive results at
significantly reduced compute amount. We obtain comparable results to the
state-of-the-arts on ImageNet while being computationally more efficient. We
also confirm the effectiveness of the approach on multiple video datasets,
including Kinetics-400, Kinetics-600, Charades, and AViD.
  The code is available at:
https://github.com/google-research/scenic/tree/main/scenic/projects/token_learner