---
layout: publication
title: 'UIGR: Unified Interactive Garment Retrieval'
authors: Xiao Han, Sen He, Li Zhang, Yi-Zhe Song, Tao Xiang
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: han2022uigr
citations: 5
additional_links: [{name: Code, url: 'https://github.com/BrandonHanx/CompFashion'},
  {name: Paper, url: 'https://arxiv.org/abs/2204.03111'}]
tags: ["CVPR"]
short_authors: Han et al.
---
Interactive garment retrieval (IGR) aims to retrieve a target garment image
based on a reference garment image along with user feedback on what to change
on the reference garment. Two IGR tasks have been studied extensively:
text-guided garment retrieval (TGR) and visually compatible garment retrieval
(VCR). The user feedback for the former indicates what semantic attributes to
change with the garment category preserved, while the category is the only
thing to be changed explicitly for the latter, with an implicit requirement on
style preservation. Despite the similarity between these two tasks and the
practical need for an efficient system tackling both, they have never been
unified and modeled jointly. In this paper, we propose a Unified Interactive
Garment Retrieval (UIGR) framework to unify TGR and VCR. To this end, we first
contribute a large-scale benchmark suited for both problems. We further propose
a strong baseline architecture to integrate TGR and VCR in one model. Extensive
experiments suggest that unifying two tasks in one framework is not only more
efficient by requiring a single model only, it also leads to better
performance. Code and datasets are available at
https://github.com/BrandonHanx/CompFashion.