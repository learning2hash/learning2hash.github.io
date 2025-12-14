---
layout: publication
title: Evaluating The Fairness Of Discriminative Foundation Models In Computer Vision
authors: Junaid Ali, Matthaeus Kleindessner, Florian Wenzel, Kailash Budhathoki, Volkan
  Cevher, Chris Russell
conference: Proceedings of the 2023 AAAI/ACM Conference on AI, Ethics, and Society
year: 2023
bibkey: ali2023evaluating
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.11867'}]
tags: [Evaluation, Image Retrieval, Re-ranking, Few-shot & Zero-shot, Datasets, AAAI]
short_authors: Ali et al.
---
We propose a novel taxonomy for bias evaluation of discriminative foundation
models, such as Contrastive Language-Pretraining (CLIP), that are used for
labeling tasks. We then systematically evaluate existing methods for mitigating
bias in these models with respect to our taxonomy. Specifically, we evaluate
OpenAI's CLIP and OpenCLIP models for key applications, such as zero-shot
classification, image retrieval and image captioning. We categorize desired
behaviors based around three axes: (i) if the task concerns humans; (ii) how
subjective the task is (i.e., how likely it is that people from a diverse range
of backgrounds would agree on a labeling); and (iii) the intended purpose of
the task and if fairness is better served by impartiality (i.e., making
decisions independent of the protected attributes) or representation (i.e.,
making decisions to maximize diversity). Finally, we provide quantitative
fairness evaluations for both binary-valued and multi-valued protected
attributes over ten diverse datasets. We find that fair PCA, a post-processing
method for fair representations, works very well for debiasing in most of the
aforementioned tasks while incurring only minor loss of performance. However,
different debiasing approaches vary in their effectiveness depending on the
task. Hence, one should choose the debiasing approach depending on the specific
use case.