---
layout: publication
title: 'Anomalydino: Boosting Patch-based Few-shot Anomaly Detection With Dinov2'
authors: Simon Damm, Mike Laszkiewicz, Johannes Lederer, Asja Fischer
conference: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2025
bibkey: damm2024anomalydino
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.14529'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Damm et al.
---
Recent advances in multimodal foundation models have set new standards in
few-shot anomaly detection. This paper explores whether high-quality visual
features alone are sufficient to rival existing state-of-the-art
vision-language models. We affirm this by adapting DINOv2 for one-shot and
few-shot anomaly detection, with a focus on industrial applications. We show
that this approach does not only rival existing techniques but can even
outmatch them in many settings. Our proposed vision-only approach, AnomalyDINO,
follows the well-established patch-level deep nearest neighbor paradigm, and
enables both image-level anomaly prediction and pixel-level anomaly
segmentation. The approach is methodologically simple and training-free and,
thus, does not require any additional data for fine-tuning or meta-learning.
The approach is methodologically simple and training-free and, thus, does not
require any additional data for fine-tuning or meta-learning. Despite its
simplicity, AnomalyDINO achieves state-of-the-art results in one- and few-shot
anomaly detection (e.g., pushing the one-shot performance on MVTec-AD from an
AUROC of 93.1% to 96.6%). The reduced overhead, coupled with its outstanding
few-shot performance, makes AnomalyDINO a strong candidate for fast deployment,
e.g., in industrial contexts.