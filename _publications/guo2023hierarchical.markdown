---
layout: publication
title: Hierarchical Fine-grained Image Forgery Detection And Localization
authors: Xiao Guo, Xiaohong Liu, Zhiyuan Ren, Steven Grosz, Iacopo Masi, Xiaoming
  Liu
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: guo2023hierarchical
citations: 71
additional_links: [{name: Code, url: 'https://github.com/CHELSEA234/HiFi_IFDL\}\{github.com/CHELSEA234/HiFi-IFDL\'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.17111'}]
tags: ["CVPR"]
short_authors: Guo et al.
---
Differences in forgery attributes of images generated in CNN-synthesized and
image-editing domains are large, and such differences make a unified image
forgery detection and localization (IFDL) challenging. To this end, we present
a hierarchical fine-grained formulation for IFDL representation learning.
Specifically, we first represent forgery attributes of a manipulated image with
multiple labels at different levels. Then we perform fine-grained
classification at these levels using the hierarchical dependency between them.
As a result, the algorithm is encouraged to learn both comprehensive features
and inherent hierarchical nature of different forgery attributes, thereby
improving the IFDL representation. Our proposed IFDL framework contains three
components: multi-branch feature extractor, localization and classification
modules. Each branch of the feature extractor learns to classify forgery
attributes at one level, while localization and classification modules segment
the pixel-level forgery region and detect image-level forgery, respectively.
Lastly, we construct a hierarchical fine-grained dataset to facilitate our
study. We demonstrate the effectiveness of our method on \(7\) different
benchmarks, for both tasks of IFDL and forgery attribute classification. Our
source code and dataset can be found:
\href\{https://github.com/CHELSEA234/HiFi_IFDL\}\{github.com/CHELSEA234/HiFi-IFDL\}.