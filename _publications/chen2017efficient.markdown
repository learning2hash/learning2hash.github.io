---
layout: publication
title: Efficient Parallel Connected Components Labeling With A Coarse-to-fine Strategy
authors: Jun Chen, Keisuke Nonaka, Ryosuke Watanabe, Hiroshi Sankoh, Houari Sabirin,
  Sei Naito
conference: IEEE Access
year: 2018
bibkey: chen2017efficient
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.09789'}]
tags: ["Efficiency"]
short_authors: Chen et al.
---
This paper proposes a new parallel approach to solve connected components on
a 2D binary image implemented with CUDA. We employ the following strategies to
accelerate neighborhood exploration after dividing an input image into
independent blocks. In the local labeling stage, a coarse-labeling algorithm,
including row-column connection and label-equivalence list unification, is
applied first to sort out the mess of an initialized local label map; a
refinement algorithm is then introduced to merge separated sub-regions from a
single component. In the block merge stage, we scan the pixels located on the
boundary of each block instead of solving the connectivity of all the pixels.
With the proposed method, the length of label-equivalence lists is compressed,
and the number of memory accesses is reduced. Thus, the efficiency of connected
components labeling is improved. Experimental results show that our method
outperforms the other approaches between \\(29%\\) and \\(80%\\) on average.