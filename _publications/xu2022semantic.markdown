---
layout: publication
title: Semantic Distillation Guided Salient Object Detection
authors: Bo Xu, Guanze Liu, Han Huang, Cheng Lu, Yandong Guo
conference: Arxiv
year: 2022
bibkey: xu2022semantic
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.04076'}]
tags: []
short_authors: Xu et al.
---
Most existing CNN-based salient object detection methods can identify local
segmentation details like hair and animal fur, but often misinterpret the real
saliency due to the lack of global contextual information caused by the
subjectiveness of the SOD task and the locality of convolution layers.
Moreover, due to the unrealistically expensive labeling costs, the current
existing SOD datasets are insufficient to cover the real data distribution. The
limitation and bias of the training data add additional difficulty to fully
exploring the semantic association between object-to-object and
object-to-environment in a given image. In this paper, we propose a semantic
distillation guided SOD (SDG-SOD) method that produces accurate results by
fusing semantically distilled knowledge from generated image captioning into
the Vision-Transformer-based SOD framework. SDG-SOD can better uncover
inter-objects and object-to-environment saliency and cover the gap between the
subjective nature of SOD and its expensive labeling. Comprehensive experiments
on five benchmark datasets demonstrate that the SDG-SOD outperforms the
state-of-the-art approaches on four evaluation metrics, and largely improves
the model performance on DUTS, ECSSD, DUT, HKU-IS, and PASCAL-S datasets.