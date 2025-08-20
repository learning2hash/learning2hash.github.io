---
layout: publication
title: Adapting Pre-trained Vision Models For Novel Instance Detection And Segmentation
authors: Yangxiao Lu, Jishnu Jaykumar P, Yunhui Guo, Nicholas Ruozzi, Yu Xiang
conference: Arxiv
year: 2024
bibkey: lu2024adapting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.17859'}]
tags: [Few-shot & Zero-shot, Tools & Libraries, Datasets, Evaluation]
short_authors: Lu et al.
---
Novel Instance Detection and Segmentation (NIDS) aims at detecting and
segmenting novel object instances given a few examples of each instance. We
propose a unified, simple, yet effective framework (NIDS-Net) comprising object
proposal generation, embedding creation for both instance templates and
proposal regions, and embedding matching for instance label assignment.
Leveraging recent advancements in large vision methods, we utilize Grounding
DINO and Segment Anything Model (SAM) to obtain object proposals with accurate
bounding boxes and masks. Central to our approach is the generation of
high-quality instance embeddings. We utilized foreground feature averages of
patch embeddings from the DINOv2 ViT backbone, followed by refinement through a
weight adapter mechanism that we introduce.
  We show experimentally that our weight adapter can adjust the embeddings
locally within their feature space and effectively limit overfitting in the
few-shot setting. Furthermore, the weight adapter optimizes weights to enhance
the distinctiveness of instance embeddings during similarity computation. This
methodology enables a straightforward matching strategy that results in
significant performance gains. Our framework surpasses current state-of-the-art
methods, demonstrating notable improvements in four detection datasets. In the
segmentation tasks on seven core datasets of the BOP challenge, our method
outperforms the leading published RGB methods and remains competitive with the
best RGB-D method. We have also verified our method using real-world images
from a Fetch robot and a RealSense camera. Project Page:
https://irvlutd.github.io/NIDSNet/