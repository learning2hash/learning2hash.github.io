---
layout: publication
title: 'Shapes And Context: In-the-wild Image Synthesis & Manipulation'
authors: Aayush Bansal, Yaser Sheikh, Deva Ramanan
conference: CVPR 2019
year: 2019
bibkey: bansal2019shapes
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.04728'}]
tags: ["CVPR"]
short_authors: Aayush Bansal, Yaser Sheikh, Deva Ramanan
---
We introduce a data-driven approach for interactively synthesizing
in-the-wild images from semantic label maps. Our approach is dramatically
different from recent work in this space, in that we make use of no learning.
Instead, our approach uses simple but classic tools for matching scene context,
shapes, and parts to a stored library of exemplars. Though simple, this
approach has several notable advantages over recent work: (1) because nothing
is learned, it is not limited to specific training data distributions (such as
cityscapes, facades, or faces); (2) it can synthesize arbitrarily
high-resolution images, limited only by the resolution of the exemplar library;
(3) by appropriately composing shapes and parts, it can generate an
exponentially large set of viable candidate output images (that can say, be
interactively searched by a user). We present results on the diverse COCO
dataset, significantly outperforming learning-based approaches on standard
image synthesis metrics. Finally, we explore user-interaction and
user-controllability, demonstrating that our system can be used as a platform
for user-driven content creation.