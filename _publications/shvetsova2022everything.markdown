---
layout: publication
title: Everything at Once -- Multi-modal Fusion Transformer for Video Retrieval
authors: Shvetsova et al.
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: shvetsova2022everything
citations: 98
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.04446'}]
tags: ["CVPR", "Video Retrieval"]
---
Multi-modal learning from video data has seen increased attention recently as
it allows to train semantically meaningful embeddings without human annotation
enabling tasks like zero-shot retrieval and classification. In this work, we
present a multi-modal, modality agnostic fusion transformer approach that
learns to exchange information between multiple modalities, such as video,
audio, and text, and integrate them into a joined multi-modal representation to
obtain an embedding that aggregates multi-modal temporal information. We
propose to train the system with a combinatorial loss on everything at once,
single modalities as well as pairs of modalities, explicitly leaving out any
add-ons such as position or modality encoding. At test time, the resulting
model can process and fuse any number of input modalities. Moreover, the
implicit properties of the transformer allow to process inputs of different
lengths. To evaluate the proposed approach, we train the model on the large
scale HowTo100M dataset and evaluate the resulting embedding space on four
challenging benchmark datasets obtaining state-of-the-art results in zero-shot
video retrieval and zero-shot video action localization.