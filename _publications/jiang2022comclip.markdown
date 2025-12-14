---
layout: publication
title: 'Comclip: Training-free Compositional Image And Text Matching'
authors: Kenan Jiang, Xuehai He, Ruize Xu, Xin Eric Wang
conference: Arxiv
year: 2022
bibkey: jiang2022comclip
citations: 2
additional_links: [{name: Code, url: 'https://github.com/eric-ai-lab/ComCLIP'}, {
    name: Paper, url: 'https://arxiv.org/abs/2211.13854'}]
tags: [Text Retrieval, Evaluation, Few-shot & Zero-shot, Datasets]
short_authors: Jiang et al.
---
Contrastive Language-Image Pretraining (CLIP) has demonstrated great
zero-shot performance for matching images and text. However, it is still
challenging to adapt vision-lanaguage pretrained models like CLIP to
compositional image and text matching -- a more challenging image and text
matching task requiring the model understanding of compositional word concepts
and visual components. Towards better compositional generalization in zero-shot
image and text matching, in this paper, we study the problem from a causal
perspective: the erroneous semantics of individual entities are essentially
confounders that cause the matching failure. Therefore, we propose a novel
\textbf\{\textit\{training-free\}\} compositional CLIP model (ComCLIP). ComCLIP
disentangles input images into subjects, objects, and action sub-images and
composes CLIP's vision encoder and text encoder to perform evolving matching
over compositional text embedding and sub-image embeddings. In this way,
ComCLIP can mitigate spurious correlations introduced by the pretrained CLIP
models and dynamically evaluate the importance of each component. Experiments
on four compositional image-text matching datasets: SVO, ComVG, Winoground, and
VL-checklist, and two general image-text retrieval datasets: Flick30K, and
MSCOCO demonstrate the effectiveness of our plug-and-play method, which boosts
the \textbf\{\textit\{zero-shot\}\} inference ability of CLIP, SLIP, and BLIP2 even
without further training or fine-tuning. Our codes can be found at
https://github.com/eric-ai-lab/ComCLIP.