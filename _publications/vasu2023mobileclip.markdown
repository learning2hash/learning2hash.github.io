---
layout: publication
title: 'Mobileclip: Fast Image-text Models Through Multi-modal Reinforced Training'
authors: Pavan Kumar Anasosalu Vasu, Hadi Pouransari, Fartash Faghri, Raviteja Vemulapalli,
  Oncel Tuzel
conference: Arxiv
year: 2023
bibkey: vasu2023mobileclip
citations: 5
additional_links: [{name: Code, url: 'https://github.com/apple/ml-mobileclip'}, {
    name: Paper, url: 'https://arxiv.org/abs/2311.17049'}]
tags: [Evaluation, Few-shot & Zero-shot, Efficiency, Datasets, Robustness]
short_authors: Vasu et al.
---
Contrastive pretraining of image-text foundation models, such as CLIP,
demonstrated excellent zero-shot performance and improved robustness on a wide
range of downstream tasks. However, these models utilize large
transformer-based encoders with significant memory and latency overhead which
pose challenges for deployment on mobile devices. In this work, we introduce
MobileCLIP -- a new family of efficient image-text models optimized for runtime
performance along with a novel and efficient training approach, namely
multi-modal reinforced training. The proposed training approach leverages
knowledge transfer from an image captioning model and an ensemble of strong
CLIP encoders to improve the accuracy of efficient models. Our approach avoids
train-time compute overhead by storing the additional knowledge in a reinforced
dataset. MobileCLIP sets a new state-of-the-art latency-accuracy tradeoff for
zero-shot classification and retrieval tasks on several datasets. Our
MobileCLIP-S2 variant is 2.3\(\times\) faster while more accurate compared to
previous best CLIP model based on ViT-B/16. We further demonstrate the
effectiveness of our multi-modal reinforced training by training a CLIP model
based on ViT-B/16 image backbone and achieving +2.9% average performance
improvement on 38 evaluation benchmarks compared to the previous best.
Moreover, we show that the proposed approach achieves 10\(\times\)-1000\(\times\)
improved learning efficiency when compared with non-reinforced CLIP training.
Code and models are available at https://github.com/apple/ml-mobileclip .