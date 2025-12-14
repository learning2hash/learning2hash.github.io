---
layout: publication
title: Learning Comprehensive Representations With Richer Self For Text-to-image Person
  Re-identification
authors: Shuanglin Yan, Neng Dong, Jun Liu, Liyan Zhang, Jinhui Tang
conference: Proceedings of the 31st ACM International Conference on Multimedia
year: 2023
bibkey: yan2023learning
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.11210'}]
tags: [Evaluation, Supervised, Image Retrieval, Datasets, Multimodal Retrieval, Tools
    & Libraries]
short_authors: Yan et al.
---
Text-to-image person re-identification (TIReID) retrieves pedestrian images
of the same identity based on a query text. However, existing methods for
TIReID typically treat it as a one-to-one image-text matching problem, only
focusing on the relationship between image-text pairs within a view. The
many-to-many matching between image-text pairs across views under the same
identity is not taken into account, which is one of the main reasons for the
poor performance of existing methods. To this end, we propose a simple yet
effective framework, called LCR\(^2\)S, for modeling many-to-many correspondences
of the same identity by learning comprehensive representations for both
modalities from a novel perspective. We construct a support set for each image
(text) by using other images (texts) under the same identity and design a
multi-head attentional fusion module to fuse the image (text) and its support
set. The resulting enriched image and text features fuse information from
multiple views, which are aligned to train a "richer" TIReID model with
many-to-many correspondences. Since the support set is unavailable during
inference, we propose to distill the knowledge learned by the "richer" model
into a lightweight model for inference with a single image/text as input. The
lightweight model focuses on semantic association and reasoning of multi-view
information, which can generate a comprehensive representation containing
multi-view information with only a single-view input to perform accurate
text-to-image retrieval during inference. In particular, we use the intra-modal
features and inter-modal semantic relations of the "richer" model to supervise
the lightweight model to inherit its powerful capability. Extensive experiments
demonstrate the effectiveness of LCR\(^2\)S, and it also achieves new
state-of-the-art performance on three popular TIReID datasets.