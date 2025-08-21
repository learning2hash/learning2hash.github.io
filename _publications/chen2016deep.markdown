---
layout: publication
title: Deep Ranking For Person Re-identification Via Joint Representation Learning
authors: Shi-Zhe Chen, Chun-Chao Guo, Jian-Huang Lai
conference: IEEE Transactions on Image Processing
year: 2016
bibkey: chen2016deep
citations: 174
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.06821'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Shi-Zhe Chen, Chun-Chao Guo, Jian-Huang Lai
---
This paper proposes a novel approach to person re-identification, a
fundamental task in distributed multi-camera surveillance systems. Although a
variety of powerful algorithms have been presented in the past few years, most
of them usually focus on designing hand-crafted features and learning metrics
either individually or sequentially. Different from previous works, we
formulate a unified deep ranking framework that jointly tackles both of these
key components to maximize their strengths. We start from the principle that
the correct match of the probe image should be positioned in the top rank
within the whole gallery set. An effective learning-to-rank algorithm is
proposed to minimize the cost corresponding to the ranking disorders of the
gallery. The ranking model is solved with a deep convolutional neural network
(CNN) that builds the relation between input image pairs and their similarity
scores through joint representation learning directly from raw image pixels.
The proposed framework allows us to get rid of feature engineering and does not
rely on any assumption. An extensive comparative evaluation is given,
demonstrating that our approach significantly outperforms all state-of-the-art
approaches, including both traditional and CNN-based methods on the challenging
VIPeR, CUHK-01 and CAVIAR4REID datasets. Additionally, our approach has better
ability to generalize across datasets without fine-tuning.