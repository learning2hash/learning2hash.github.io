---
layout: publication
title: 'Metric Learning With HORDE: High-order Regularizer For Deep Embeddings'
authors: Pierre Jacob, David Picard, Aymeric Histace, Edouard Klein
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: jacob2019metric
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.02735'}]
tags: [ICCV, Image Retrieval, Few-shot & Zero-shot, Distance Metric Learning, Datasets]
short_authors: Jacob et al.
---
Learning an effective similarity measure between image representations is key
to the success of recent advances in visual search tasks (e.g. verification or
zero-shot learning). Although the metric learning part is well addressed, this
metric is usually computed over the average of the extracted deep features.
This representation is then trained to be discriminative. However, these deep
features tend to be scattered across the feature space. Consequently, the
representations are not robust to outliers, object occlusions, background
variations, etc. In this paper, we tackle this scattering problem with a
distribution-aware regularization named HORDE. This regularizer enforces
visually-close images to have deep features with the same distribution which
are well localized in the feature space. We provide a theoretical analysis
supporting this regularization effect. We also show the effectiveness of our
approach by obtaining state-of-the-art results on 4 well-known datasets
(Cub-200-2011, Cars-196, Stanford Online Products and Inshop Clothes
Retrieval).