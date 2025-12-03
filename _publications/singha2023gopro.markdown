---
layout: publication
title: 'Gopro: Generate And Optimize Prompts In CLIP Using Self-supervised Learning'
authors: Mainak Singha, Ankit Jha, Biplab Banerjee
conference: Arxiv
year: 2023
bibkey: singha2023gopro
citations: 1
additional_links: [{name: Code, url: 'https://github.com/mainaksingha01/GOPro'}, {
    name: Paper, url: 'https://arxiv.org/abs/2308.11605'}]
tags: ["Distance Metric Learning", "Evaluation", "Scalability", "Self-Supervised", "Supervised"]
short_authors: Mainak Singha, Ankit Jha, Biplab Banerjee
---
Large-scale foundation models, such as CLIP, have demonstrated remarkable
success in visual recognition tasks by embedding images in a semantically rich
space. Self-supervised learning (SSL) has also shown promise in improving
visual recognition by learning invariant features. However, the combination of
CLIP with SSL is found to face challenges due to the multi-task framework that
blends CLIP's contrastive loss and SSL's loss, including difficulties with loss
weighting and inconsistency among different views of images in CLIP's output
space. To overcome these challenges, we propose a prompt learning-based model
called GOPro, which is a unified framework that ensures similarity between
various augmented views of input images in a shared image-text embedding space,
using a pair of learnable image and text projectors atop CLIP, to promote
invariance and generalizability. To automatically learn such prompts, we
leverage the visual content and style primitives extracted from pre-trained
CLIP and adapt them to the target task. In addition to CLIP's cross-domain
contrastive loss, we introduce a visual contrastive loss and a novel prompt
consistency loss, considering the different views of the images. GOPro is
trained end-to-end on all three loss objectives, combining the strengths of
CLIP and SSL in a principled manner. Empirical evaluations demonstrate that
GOPro outperforms the state-of-the-art prompting techniques on three
challenging domain generalization tasks across multiple benchmarks by a
significant margin. Our code is available at
https://github.com/mainaksingha01/GOPro.