---
layout: publication
title: Attention-based Dynamic Subspace Learners For Medical Image Analysis
authors: Sukesh Adiga, Jose Dolz, Herve Lombaert
conference: IEEE Journal of Biomedical and Health Informatics
year: 2022
bibkey: adiga2022attention
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.09068'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Recommender Systems", "Supervised"]
short_authors: Sukesh Adiga, Jose Dolz, Herve Lombaert
---
Learning similarity is a key aspect in medical image analysis, particularly
in recommendation systems or in uncovering the interpretation of anatomical
data in images. Most existing methods learn such similarities in the embedding
space over image sets using a single metric learner. Images, however, have a
variety of object attributes such as color, shape, or artifacts. Encoding such
attributes using a single metric learner is inadequate and may fail to
generalize. Instead, multiple learners could focus on separate aspects of these
attributes in subspaces of an overarching embedding. This, however, implies the
number of learners to be found empirically for each new dataset. This work,
Dynamic Subspace Learners, proposes to dynamically exploit multiple learners by
removing the need of knowing apriori the number of learners and aggregating new
subspace learners during training. Furthermore, the visual interpretability of
such subspace learning is enforced by integrating an attention module into our
method. This integrated attention mechanism provides a visual insight of
discriminative image features that contribute to the clustering of image sets
and a visual explanation of the embedding features. The benefits of our
attention-based dynamic subspace learners are evaluated in the application of
image clustering, image retrieval, and weakly supervised segmentation. Our
method achieves competitive results with the performances of multiple learners
baselines and significantly outperforms the classification network in terms of
clustering and retrieval scores on three different public benchmark datasets.
Moreover, our attention maps offer a proxy-labels, which improves the
segmentation accuracy up to 15% in Dice scores when compared to
state-of-the-art interpretation techniques.