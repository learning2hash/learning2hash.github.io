---
layout: publication
title: Contextualizing Meta-learning Via Learning To Decompose
authors: Han-Jia Ye, da-Wei Zhou, Lanqing Hong, Zhenguo Li, Xiu-Shen Wei, de-Chuan
  Zhan
conference: Arxiv
year: 2021
bibkey: ye2021contextualizing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.08112'}]
tags: [Evaluation, Few-shot & Zero-shot]
short_authors: Ye et al.
---
Meta-learning has emerged as an efficient approach for constructing target
models based on support sets. For example, the meta-learned embeddings enable
the construction of target nearest-neighbor classifiers for specific tasks by
pulling instances closer to their same-class neighbors. However, a single
instance can be annotated from various latent attributes, making visually
similar instances inside or across support sets have different labels and
diverse relationships with others. Consequently, a uniform meta-learned
strategy for inferring the target model from the support set fails to capture
the instance-wise ambiguous similarity. To this end, we propose Learning to
Decompose Network (LeadNet) to contextualize the meta-learned
``support-to-target'' strategy, leveraging the context of instances with one or
mixed latent attributes in a support set. In particular, the comparison
relationship between instances is decomposed w.r.t. multiple embedding spaces.
LeadNet learns to automatically select the strategy associated with the right
attribute via incorporating the change of comparison across contexts\} with
polysemous embeddings. We demonstrate the superiority of LeadNet in various
applications, including exploring multiple views of confusing data,
out-of-distribution recognition, and few-shot image classification.