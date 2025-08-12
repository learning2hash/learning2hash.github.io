---
layout: publication
title: Few-shot Font Generation By Learning Style Difference And Similarity
authors: Xiao He, Mingrui Zhu, Nannan Wang, Xinbo Gao, Heng Yang
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2024
bibkey: he2023few
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.10008'}]
tags: ["Few Shot & Zero Shot"]
short_authors: He et al.
---
Few-shot font generation (FFG) aims to preserve the underlying global
structure of the original character while generating target fonts by referring
to a few samples. It has been applied to font library creation, a personalized
signature, and other scenarios. Existing FFG methods explicitly disentangle
content and style of reference glyphs universally or component-wisely. However,
they ignore the difference between glyphs in different styles and the
similarity of glyphs in the same style, which results in artifacts such as
local distortions and style inconsistency. To address this issue, we propose a
novel font generation approach by learning the Difference between different
styles and the Similarity of the same style (DS-Font). We introduce contrastive
learning to consider the positive and negative relationship between styles.
Specifically, we propose a multi-layer style projector for style encoding and
realize a distinctive style representation via our proposed Cluster-level
Contrastive Style (CCS) loss. In addition, we design a multi-task patch
discriminator, which comprehensively considers different areas of the image and
ensures that each style can be distinguished independently. We conduct
qualitative and quantitative evaluations comprehensively to demonstrate that
our approach achieves significantly better results than state-of-the-art
methods.