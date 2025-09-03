---
layout: publication
title: Aligning Bag Of Regions For Open-vocabulary Object Detection
authors: Size Wu, Wenwei Zhang, Sheng Jin, Wentao Liu, Chen Change Loy
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: wu2023aligning
citations: 63
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2302.13996'}]
tags: ["CVPR", "Datasets", "Scalability"]
short_authors: Wu et al.
---
Pre-trained vision-language models (VLMs) learn to align vision and language
representations on large-scale datasets, where each image-text pair usually
contains a bag of semantic concepts. However, existing open-vocabulary object
detectors only align region embeddings individually with the corresponding
features extracted from the VLMs. Such a design leaves the compositional
structure of semantic concepts in a scene under-exploited, although the
structure may be implicitly learned by the VLMs. In this work, we propose to
align the embedding of bag of regions beyond individual regions. The proposed
method groups contextually interrelated regions as a bag. The embeddings of
regions in a bag are treated as embeddings of words in a sentence, and they are
sent to the text encoder of a VLM to obtain the bag-of-regions embedding, which
is learned to be aligned to the corresponding features extracted by a frozen
VLM. Applied to the commonly used Faster R-CNN, our approach surpasses the
previous best results by 4.6 box AP50 and 2.8 mask AP on novel categories of
open-vocabulary COCO and LVIS benchmarks, respectively. Code and models are
available at https://github.com/wusize/ovdet.