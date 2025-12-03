---
layout: publication
title: 'Fairclip: Social Bias Elimination Based On Attribute Prototype Learning And
  Representation Neutralization'
authors: Junyang Wang, Yi Zhang, Jitao Sang
conference: Arxiv
year: 2022
bibkey: wang2022fairclip
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.14562'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Junyang Wang, Yi Zhang, Jitao Sang
---
The Vision-Language Pre-training (VLP) models like CLIP have gained
popularity in recent years. However, many works found that the social biases
hidden in CLIP easily manifest in downstream tasks, especially in image
retrieval, which can have harmful effects on human society. In this work, we
propose FairCLIP to eliminate the social bias in CLIP-based image retrieval
without damaging the retrieval performance achieving the compatibility between
the debiasing effect and the retrieval performance. FairCLIP is divided into
two steps: Attribute Prototype Learning (APL) and Representation Neutralization
(RN). In the first step, we extract the concepts needed for debiasing in CLIP.
We use the query with learnable word vector prefixes as the extraction
structure. In the second step, we first divide the attributes into target and
bias attributes. By analysis, we find that both attributes have an impact on
the bias. Therefore, we try to eliminate the bias by using Re-Representation
Matrix (RRM) to achieve the neutralization of the representation. We compare
the debiasing effect and retrieval performance with other methods, and
experiments demonstrate that FairCLIP can achieve the best compatibility.
Although FairCLIP is used to eliminate bias in image retrieval, it achieves the
neutralization of the representation which is common to all CLIP downstream
tasks. This means that FairCLIP can be applied as a general debiasing method
for other fairness issues related to CLIP.