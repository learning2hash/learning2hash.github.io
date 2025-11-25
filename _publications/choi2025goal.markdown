---
layout: publication
title: 'GOAL: Global-local Object Alignment Learning'
authors: Hyungyu Choi, Young Kyun Jang, Chanho Eom
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: choi2025goal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.17782'}]
tags: ["CVPR", "Image Retrieval", "Text Retrieval"]
short_authors: Hyungyu Choi, Young Kyun Jang, Chanho Eom
---
Vision-language models like CLIP have shown impressive capabilities in
aligning images and text, but they often struggle with lengthy and detailed
text descriptions because of their training focus on short and concise
captions. We present GOAL (Global-local Object Alignment Learning), a novel
fine-tuning method that enhances CLIP's ability to handle lengthy text by
leveraging both global and local semantic alignments between image and lengthy
text. Our approach consists of two key components: Local Image-Sentence
Matching (LISM), which identifies corresponding pairs between image segments
and descriptive sentences, and Token Similarity-based Learning (TSL), which
efficiently propagates local element attention through these matched pairs.
Evaluating GOAL on three new benchmarks for image-lengthy text retrieval, we
demonstrate significant improvements over baseline CLIP fine-tuning,
establishing a simple yet effective approach for adapting CLIP to detailed
textual descriptions. Through extensive experiments, we show that our method's
focus on local semantic alignment alongside global context leads to more
nuanced and representative embeddings, particularly beneficial for tasks
requiring fine-grained understanding of lengthy text descriptions.