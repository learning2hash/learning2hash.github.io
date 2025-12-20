---
layout: publication
title: Text-to-image Diffusion Models Are Great Sketch-photo Matchmakers
authors: Subhadeep Koley, Ayan Kumar Bhunia, Aneeshan Sain, Pinaki Nath Chowdhury,
  Tao Xiang, Yi-Zhe Song
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: koley2024text
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.07214'}]
tags: ["CVPR", "Datasets", "Evaluation", "Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Koley et al.
---
This paper, for the first time, explores text-to-image diffusion models for
Zero-Shot Sketch-based Image Retrieval (ZS-SBIR). We highlight a pivotal
discovery: the capacity of text-to-image diffusion models to seamlessly bridge
the gap between sketches and photos. This proficiency is underpinned by their
robust cross-modal capabilities and shape bias, findings that are substantiated
through our pilot studies. In order to harness pre-trained diffusion models
effectively, we introduce a straightforward yet powerful strategy focused on
two key aspects: selecting optimal feature layers and utilising visual and
textual prompts. For the former, we identify which layers are most enriched
with information and are best suited for the specific retrieval requirements
(category-level or fine-grained). Then we employ visual and textual prompts to
guide the model's feature extraction process, enabling it to generate more
discriminative and contextually relevant cross-modal representations. Extensive
experiments on several benchmark datasets validate significant performance
improvements.