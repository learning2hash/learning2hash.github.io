---
layout: publication
title: Source-free Domain Adaptation Of Weakly-supervised Object Localization Models
  For Histology
authors: Alexis Guichemerre, Soufiane Belharbi, Tsiry Mayet, Shakeeb Murtaza, Pourya
  Shamsolmoali, Luke McCaffrey, Eric Granger
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2024
bibkey: guichemerre2024source
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.19113'}]
tags: ["CVPR", "Supervised", "Unsupervised"]
short_authors: Guichemerre et al.
---
Given the emergence of deep learning, digital pathology has gained popularity
for cancer diagnosis based on histology images. Deep weakly supervised object
localization (WSOL) models can be trained to classify histology images
according to cancer grade and identify regions of interest (ROIs) for
interpretation, using inexpensive global image-class annotations. A WSOL model
initially trained on some labeled source image data can be adapted using
unlabeled target data in cases of significant domain shifts caused by
variations in staining, scanners, and cancer type. In this paper, we focus on
source-free (unsupervised) domain adaptation (SFDA), a challenging problem
where a pre-trained source model is adapted to a new target domain without
using any source domain data for privacy and efficiency reasons. SFDA of WSOL
models raises several challenges in histology, most notably because they are
not intended to adapt for both classification and localization tasks. In this
paper, 4 state-of-the-art SFDA methods, each one representative of a main SFDA
family, are compared for WSOL in terms of classification and localization
accuracy. They are the SFDA-Distribution Estimation, Source HypOthesis
Transfer, Cross-Domain Contrastive Learning, and Adaptively Domain Statistics
Alignment. Experimental results on the challenging Glas (smaller, breast
cancer) and Camelyon16 (larger, colon cancer) histology datasets indicate that
these SFDA methods typically perform poorly for localization after adaptation
when optimized for classification.