---
layout: publication
title: Open-set Image Tagging With Multi-grained Text Supervision
authors: Xinyu Huang, Yi-Jie Huang, Youcai Zhang, Weiwei Tian, Rui Feng, Yuejie Zhang,
  Yanchun Xie, Yaqian Li, Lei Zhang
conference: Arxiv
year: 2023
bibkey: huang2023open
citations: 2
additional_links: [{name: Code, url: 'https://github.com/xinyu1205/recognize-anything'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.15200'}]
tags: []
short_authors: Huang et al.
---
In this paper, we introduce the Recognize Anything Plus Model (RAM++), an
open-set image tagging model effectively leveraging multi-grained text
supervision. Previous approaches (e.g., CLIP) primarily utilize global text
supervision paired with images, leading to sub-optimal performance in
recognizing multiple individual semantic tags. In contrast, RAM++ seamlessly
integrates individual tag supervision with global text supervision, all within
a unified alignment framework. This integration not only ensures efficient
recognition of predefined tag categories, but also enhances generalization
capabilities for diverse open-set categories. Furthermore, RAM++ employs large
language models (LLMs) to convert semantically constrained tag supervision into
more expansive tag description supervision, thereby enriching the scope of
open-set visual description concepts. Comprehensive evaluations on various
image recognition benchmarks demonstrate RAM++ exceeds existing
state-of-the-art (SOTA) open-set image tagging models on most aspects.
Specifically, for predefined commonly used tag categories, RAM++ showcases 10.2
mAP and 15.4 mAP enhancements over CLIP on OpenImages and ImageNet. For
open-set categories beyond predefined, RAM++ records improvements of 5.0 mAP
and 6.4 mAP over CLIP and RAM respectively on OpenImages. For diverse
human-object interaction phrases, RAM++ achieves 7.8 mAP and 4.7 mAP
improvements on the HICO benchmark. Code, datasets and pre-trained models are
available at https://github.com/xinyu1205/recognize-anything.