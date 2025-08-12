---
layout: publication
title: 'MEET: A Million-scale Dataset For Fine-grained Geospatial Scene Classification
  With Zoom-free Remote Sensing Imagery'
authors: Yansheng Li, Yuning Wu, Gong Cheng, Chao Tao, Bo Dang, Yu Wang, Jiahao Zhang,
  Chuge Zhang, Yiting Liu, Xu Tang, Jiayi Ma, Yongjun Zhang
conference: IEEE/CAA Journal of Automatica Sinica
year: 2025
bibkey: li2025meet
citations: 0
additional_links: [{name: Code, url: 'https://jerrywyn.github.io/project/MEET.html'},
  {name: Paper, url: 'https://arxiv.org/abs/2503.11219'}]
tags: ["Datasets", "Evaluation"]
short_authors: Li et al.
---
Accurate fine-grained geospatial scene classification using remote sensing
imagery is essential for a wide range of applications. However, existing
approaches often rely on manually zooming remote sensing images at different
scales to create typical scene samples. This approach fails to adequately
support the fixed-resolution image interpretation requirements in real-world
scenarios. To address this limitation, we introduce the Million-scale
finE-grained geospatial scEne classification dataseT (MEET), which contains
over 1.03 million zoom-free remote sensing scene samples, manually annotated
into 80 fine-grained categories. In MEET, each scene sample follows a
scene-inscene layout, where the central scene serves as the reference, and
auxiliary scenes provide crucial spatial context for finegrained
classification. Moreover, to tackle the emerging challenge of scene-in-scene
classification, we present the Context-Aware Transformer (CAT), a model
specifically designed for this task, which adaptively fuses spatial context to
accurately classify the scene samples. CAT adaptively fuses spatial context to
accurately classify the scene samples by learning attentional features that
capture the relationships between the center and auxiliary scenes. Based on
MEET, we establish a comprehensive benchmark for fine-grained geospatial scene
classification, evaluating CAT against 11 competitive baselines. The results
demonstrate that CAT significantly outperforms these baselines, achieving a
1.88% higher balanced accuracy (BA) with the Swin-Large backbone, and a notable
7.87% improvement with the Swin-Huge backbone. Further experiments validate the
effectiveness of each module in CAT and show the practical applicability of CAT
in the urban functional zone mapping. The source code and dataset will be
publicly available at https://jerrywyn.github.io/project/MEET.html.