---
layout: publication
title: Cross-view Transformers For Real-time Map-view Semantic Segmentation
authors: "Brady Zhou, Philipp Kr\xE4henb\xFChl"
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: zhou2022cross
citations: 173
additional_links: [{name: Code, url: 'https://github.com/bradyz/cross_view_transformers'},
  {name: Paper, url: 'https://arxiv.org/abs/2205.02833'}]
tags: ["CVPR"]
short_authors: "Brady Zhou, Philipp Kr\xE4henb\xFChl"
---
We present cross-view transformers, an efficient attention-based model for
map-view semantic segmentation from multiple cameras. Our architecture
implicitly learns a mapping from individual camera views into a canonical
map-view representation using a camera-aware cross-view attention mechanism.
Each camera uses positional embeddings that depend on its intrinsic and
extrinsic calibration. These embeddings allow a transformer to learn the
mapping across different views without ever explicitly modeling it
geometrically. The architecture consists of a convolutional image encoder for
each view and cross-view transformer layers to infer a map-view semantic
segmentation. Our model is simple, easily parallelizable, and runs in
real-time. The presented architecture performs at state-of-the-art on the
nuScenes dataset, with 4x faster inference speeds. Code is available at
https://github.com/bradyz/cross_view_transformers.