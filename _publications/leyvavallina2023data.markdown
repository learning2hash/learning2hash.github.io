---
layout: publication
title: Data-efficient Large Scale Place Recognition With Graded Similarity Supervision
authors: Maria Leyva-Vallina, Nicola Strisciuglio, Nicolai Petkov
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: leyvavallina2023data
citations: 24
additional_links: [{name: Code, url: 'https://github.com/marialeyvallina/generalized_contrastive_loss'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.11739'}]
tags: ["CVPR", "Datasets", "Hybrid ANN Methods", "Re-Ranking"]
short_authors: Maria Leyva-Vallina, Nicola Strisciuglio, Nicolai Petkov
---
Visual place recognition (VPR) is a fundamental task of computer vision for
visual localization. Existing methods are trained using image pairs that either
depict the same place or not. Such a binary indication does not consider
continuous relations of similarity between images of the same place taken from
different positions, determined by the continuous nature of camera pose. The
binary similarity induces a noisy supervision signal into the training of VPR
methods, which stall in local minima and require expensive hard mining
algorithms to guarantee convergence. Motivated by the fact that two images of
the same place only partially share visual cues due to camera pose differences,
we deploy an automatic re-annotation strategy to re-label VPR datasets. We
compute graded similarity labels for image pairs based on available
localization metadata. Furthermore, we propose a new Generalized Contrastive
Loss (GCL) that uses graded similarity labels for training contrastive
networks. We demonstrate that the use of the new labels and GCL allow to
dispense from hard-pair mining, and to train image descriptors that perform
better in VPR by nearest neighbor search, obtaining superior or comparable
results than methods that require expensive hard-pair mining and re-ranking
techniques. Code and models available at:
https://github.com/marialeyvallina/generalized_contrastive_loss