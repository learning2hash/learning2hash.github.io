---
layout: publication
title: 'Image Textualization: An Automatic Framework For Creating Accurate And Detailed
  Image Descriptions'
authors: Renjie Pi, Jianshu Zhang, Jipeng Zhang, Rui Pan, Zhekai Chen, Tong Zhang
conference: Arxiv
year: 2024
bibkey: pi2024image
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.07502'}]
tags: ["Tools & Libraries"]
short_authors: Pi et al.
---
Image description datasets play a crucial role in the advancement of various
applications such as image understanding, text-to-image generation, and
text-image retrieval. Currently, image description datasets primarily originate
from two sources. One source is the scraping of image-text pairs from the web.
Despite their abundance, these descriptions are often of low quality and noisy.
Another is through human labeling. Datasets such as COCO are generally very
short and lack details. Although detailed image descriptions can be annotated
by humans, the high annotation cost limits the feasibility. These limitations
underscore the need for more efficient and scalable methods to generate
accurate and detailed image descriptions. In this paper, we propose an
innovative framework termed Image Textualization (IT), which automatically
produces high-quality image descriptions by leveraging existing multi-modal
large language models (MLLMs) and multiple vision expert models in a
collaborative manner, which maximally convert the visual information into text.
To address the current lack of benchmarks for detailed descriptions, we propose
several benchmarks for comprehensive evaluation, which verifies the quality of
image descriptions created by our framework. Furthermore, we show that
LLaVA-7B, benefiting from training on IT-curated descriptions, acquire improved
capability to generate richer image descriptions, substantially increasing the
length and detail of their output with less hallucination.