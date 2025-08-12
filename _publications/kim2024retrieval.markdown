---
layout: publication
title: Retrieval-augmented Open-vocabulary Object Detection
authors: Jooyeon Kim, Eulrang Cho, Sehyung Kim, Hyunwoo J. Kim
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: kim2024retrieval
citations: 2
additional_links: [{name: Code, url: 'https://github.com/mlvlab/RALF'}, {name: Paper,
    url: 'https://arxiv.org/abs/2404.05687'}]
tags: ["CVPR"]
short_authors: Kim et al.
---
Open-vocabulary object detection (OVD) has been studied with Vision-Language
Models (VLMs) to detect novel objects beyond the pre-trained categories.
Previous approaches improve the generalization ability to expand the knowledge
of the detector, using 'positive' pseudo-labels with additional 'class' names,
e.g., sock, iPod, and alligator. To extend the previous methods in two aspects,
we propose Retrieval-Augmented Losses and visual Features (RALF). Our method
retrieves related 'negative' classes and augments loss functions. Also, visual
features are augmented with 'verbalized concepts' of classes, e.g., worn on the
feet, handheld music player, and sharp teeth. Specifically, RALF consists of
two modules: Retrieval Augmented Losses (RAL) and Retrieval-Augmented visual
Features (RAF). RAL constitutes two losses reflecting the semantic similarity
with negative vocabularies. In addition, RAF augments visual features with the
verbalized concepts from a large language model (LLM). Our experiments
demonstrate the effectiveness of RALF on COCO and LVIS benchmark datasets. We
achieve improvement up to 3.4 box AP\(_\{50\}^\{\text\{N\}\}\) on novel categories of
the COCO dataset and 3.6 mask AP\(_\{\text\{r\}\}\) gains on the LVIS dataset. Code
is available at https://github.com/mlvlab/RALF .