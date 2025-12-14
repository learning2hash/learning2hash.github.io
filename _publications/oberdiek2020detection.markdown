---
layout: publication
title: Detection And Retrieval Of Out-of-distribution Objects In Semantic Segmentation
authors: Philipp Oberdiek, Matthias Rottmann, Gernot A. Fink
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: oberdiek2020detection
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.06831'}]
tags: [Evaluation, Image Retrieval, Neural Hashing, Datasets, CVPR]
short_authors: Philipp Oberdiek, Matthias Rottmann, Gernot A. Fink
---
When deploying deep learning technology in self-driving cars, deep neural
networks are constantly exposed to domain shifts. These include, e.g., changes
in weather conditions, time of day, and long-term temporal shift. In this work
we utilize a deep neural network trained on the Cityscapes dataset containing
urban street scenes and infer images from a different dataset, the A2D2
dataset, containing also countryside and highway images. We present a novel
pipeline for semantic segmenation that detects out-of-distribution (OOD)
segments by means of the deep neural network's prediction and performs image
retrieval after feature extraction and dimensionality reduction on image
patches. In our experiments we demonstrate that the deployed OOD approach is
suitable for detecting out-of-distribution concepts. Furthermore, we evaluate
the image patch retrieval qualitatively as well as quantitatively by means of
the semi-compatible A2D2 ground truth and obtain mAP values of up to 52.2%.