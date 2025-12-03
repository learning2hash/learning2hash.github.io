---
layout: publication
title: Modality-aware Triplet Hard Mining For Zero-shot Sketch-based Image Retrieval
authors: Zongheng Huang, Yifan Sun, Chuchu Han, Changxin Gao, Nong Sang
conference: Arxiv
year: 2021
bibkey: huang2021modality
citations: 3
additional_links: [{name: Code, url: 'https://github.com/huangzongheng/MATHM'}, {
    name: Paper, url: 'https://arxiv.org/abs/2112.07966'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Huang et al.
---
This paper tackles the Zero-Shot Sketch-Based Image Retrieval (ZS-SBIR)
problem from the viewpoint of cross-modality metric learning. This task has two
characteristics: 1) the zero-shot setting requires a metric space with good
within-class compactness and the between-class discrepancy for recognizing the
novel classes and 2) the sketch query and the photo gallery are in different
modalities. The metric learning viewpoint benefits ZS-SBIR from two aspects.
First, it facilitates improvement through recent good practices in deep metric
learning (DML). By combining two fundamental learning approaches in DML, e.g.,
classification training and pairwise training, we set up a strong baseline for
ZS-SBIR. Without bells and whistles, this baseline achieves competitive
retrieval accuracy. Second, it provides an insight that properly suppressing
the modality gap is critical. To this end, we design a novel method named
Modality-Aware Triplet Hard Mining (MATHM). MATHM enhances the baseline with
three types of pairwise learning, e.g., a cross-modality sample pair, a
within-modality sample pair, and their combination.\We also design an adaptive
weighting method to balance these three components during training dynamically.
Experimental results confirm that MATHM brings another round of significant
improvement based on the strong baseline and sets up new state-of-the-art
performance. For example, on the TU-Berlin dataset, we achieve 47.88+2.94%
mAP@all and 58.28+2.34% Prec@100. Code will be publicly available at:
https://github.com/huangzongheng/MATHM.