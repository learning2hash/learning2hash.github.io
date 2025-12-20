---
layout: publication
title: Adaptive Similarity Bootstrapping For Self-distillation Based Representation
  Learning
authors: "Tim Lebailly, Thomas Stegm\xFCller, Behzad Bozorgtabar, Jean-Philippe Thiran,\
  \ Tinne Tuytelaars"
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: lebailly2023adaptive
citations: 3
additional_links: [{name: Code, url: 'https://github.com/tileb1/AdaSim'}, {name: Paper,
    url: 'https://arxiv.org/abs/2303.13606'}]
tags: ["Evaluation", "ICCV", "Self-Supervised", "Supervised"]
short_authors: Lebailly et al.
---
Most self-supervised methods for representation learning leverage a
cross-view consistency objective i.e., they maximize the representation
similarity of a given image's augmented views. Recent work NNCLR goes beyond
the cross-view paradigm and uses positive pairs from different images obtained
via nearest neighbor bootstrapping in a contrastive setting. We empirically
show that as opposed to the contrastive learning setting which relies on
negative samples, incorporating nearest neighbor bootstrapping in a
self-distillation scheme can lead to a performance drop or even collapse. We
scrutinize the reason for this unexpected behavior and provide a solution. We
propose to adaptively bootstrap neighbors based on the estimated quality of the
latent space. We report consistent improvements compared to the naive
bootstrapping approach and the original baselines. Our approach leads to
performance improvements for various self-distillation method/backbone
combinations and standard downstream tasks. Our code is publicly available at
https://github.com/tileb1/AdaSim.