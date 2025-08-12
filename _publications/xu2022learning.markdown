---
layout: publication
title: Learning To Generate Image Embeddings With User-level Differential Privacy
authors: Zheng Xu, Maxwell Collins, Yuxiao Wang, Liviu Panait, Sewoong Oh, Sean Augenstein,
  Ting Liu, Florian Schroff, H. Brendan Mcmahan
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: xu2022learning
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.10844'}]
tags: ["CVPR", "Privacy & Security"]
short_authors: Xu et al.
---
Small on-device models have been successfully trained with user-level
differential privacy (DP) for next word prediction and image classification
tasks in the past. However, existing methods can fail when directly applied to
learn embedding models using supervised training data with a large class space.
To achieve user-level DP for large image-to-embedding feature extractors, we
propose DP-FedEmb, a variant of federated learning algorithms with per-user
sensitivity control and noise addition, to train from user-partitioned data
centralized in the datacenter. DP-FedEmb combines virtual clients, partial
aggregation, private local fine-tuning, and public pretraining to achieve
strong privacy utility trade-offs. We apply DP-FedEmb to train image embedding
models for faces, landmarks and natural species, and demonstrate its superior
utility under same privacy budget on benchmark datasets DigiFace, EMNIST, GLD
and iNaturalist. We further illustrate it is possible to achieve strong
user-level DP guarantees of \\(\epsilon<4\\) while controlling the utility drop
within 5%, when millions of users can participate in training.