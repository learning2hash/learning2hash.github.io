---
layout: publication
title: 'Commercemm: Large-scale Commerce Multimodal Representation Learning With Omni
  Retrieval'
authors: Licheng Yu, Jun Chen, Animesh Sinha, Mengjiao Mj Wang, Hugo Chen, Tamara
  L. Berg, Ning Zhang
conference: Arxiv
year: 2022
bibkey: yu2022commercemm
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.07247'}]
tags: ["Efficiency", "Multimodal Retrieval", "Scalability"]
short_authors: Yu et al.
---
We introduce CommerceMM - a multimodal model capable of providing a diverse
and granular understanding of commerce topics associated to the given piece of
content (image, text, image+text), and having the capability to generalize to a
wide range of tasks, including Multimodal Categorization, Image-Text Retrieval,
Query-to-Product Retrieval, Image-to-Product Retrieval, etc. We follow the
pre-training + fine-tuning training regime and present 5 effective pre-training
tasks on image-text pairs. To embrace more common and diverse commerce data
with text-to-multimodal, image-to-multimodal, and multimodal-to-multimodal
mapping, we propose another 9 novel cross-modal and cross-pair retrieval tasks,
called Omni-Retrieval pre-training. The pre-training is conducted in an
efficient manner with only two forward/backward updates for the combined 14
tasks. Extensive experiments and analysis show the effectiveness of each task.
When combining all pre-training tasks, our model achieves state-of-the-art
performance on 7 commerce-related downstream tasks after fine-tuning.
Additionally, we propose a novel approach of modality randomization to
dynamically adjust our model under different efficiency constraints.