---
layout: publication
title: Joint Visual-textual Embedding For Multimodal Style Search
authors: Gil Sadeh, Lior Fritz, Gabi Shalev, Eduard Oks
conference: Arxiv
year: 2019
bibkey: sadeh2019joint
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.06620'}]
tags: [Evaluation, Distance Metric Learning]
short_authors: Sadeh et al.
---
We introduce a multimodal visual-textual search refinement method for fashion
garments. Existing search engines do not enable intuitive, interactive,
refinement of retrieved results based on the properties of a particular
product. We propose a method to retrieve similar items, based on a query item
image and textual refinement properties. We believe this method can be
leveraged to solve many real-life customer scenarios, in which a similar item
in a different color, pattern, length or style is desired. We employ a joint
embedding training scheme in which product images and their catalog textual
metadata are mapped closely in a shared space. This joint visual-textual
embedding space enables manipulating catalog images semantically, based on
textual refinement requirements. We propose a new training objective function,
Mini-Batch Match Retrieval, and demonstrate its superiority over the commonly
used triplet loss. Additionally, we demonstrate the feasibility of adding an
attribute extraction module, trained on the same catalog data, and demonstrate
how to integrate it within the multimodal search to boost its performance. We
introduce an evaluation protocol with an associated benchmark, and compare
several approaches.