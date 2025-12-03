---
layout: publication
title: Compositional Image-text Matching And Retrieval By Grounding Entities
authors: "Madhukar Reddy Vongala, Saurabh Srivastava, Jana Ko\u0161eck\xE1"
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2025
bibkey: vongala2025compositional
citations: 0
additional_links: [{name: Code, url: 'https://github.com/madhukarreddyvongala/GroundingCLIP'},
  {name: Paper, url: 'https://arxiv.org/abs/2505.02278'}]
tags: ["CVPR", "Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: "Madhukar Reddy Vongala, Saurabh Srivastava, Jana Ko\u0161eck\xE1"
---
Vision-language pretraining on large datasets of images-text pairs is one of
the main building blocks of current Vision-Language Models. While with
additional training, these models excel in various downstream tasks, including
visual question answering, image captioning, and visual commonsense reasoning.
However, a notable weakness of pretrained models like CLIP, is their inability
to perform entity grounding and compositional image and text
matching~\cite\{Jiang2024ComCLIP, yang2023amc, Rajabi2023GroundedVSR,
learninglocalizeCVPR24\}. In this work we propose a novel learning-free
zero-shot augmentation of CLIP embeddings that has favorable compositional
properties. We compute separate embeddings of sub-images of object entities and
relations that are localized by the state of the art open vocabulary detectors
and dynamically adjust the baseline global image embedding. % The final
embedding is obtained by computing a weighted combination of the sub-image
embeddings. The resulting embedding is then utilized for similarity computation
with text embedding, resulting in a average 1.5% improvement in image-text
matching accuracy on the Visual Genome and SVO Probes
datasets~\cite\{krishna2017visualgenome, svo\}. Notably, the enhanced embeddings
demonstrate superior retrieval performance, thus achieving significant gains on
the Flickr30K and MS-COCO retrieval benchmarks~\cite\{flickr30ke, mscoco\},
improving the state-of-the-art Recall@1 by 12% and 0.4%, respectively. Our
code is available at https://github.com/madhukarreddyvongala/GroundingCLIP.