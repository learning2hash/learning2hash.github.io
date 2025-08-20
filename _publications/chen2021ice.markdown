---
layout: publication
title: 'ICE: Inter-instance Contrastive Encoding For Unsupervised Person Re-identification'
authors: Hao Chen, Benoit Lagadec, Francois Bremond
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: chen2021ice
citations: 194
additional_links: [{name: Code, url: 'https://github.com/chenhao2345/ICE.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2103.16364'}]
tags: [Scalability, Datasets, ICCV, Supervised, Distance Metric Learning, Unsupervised,
  Self-Supervised]
short_authors: Hao Chen, Benoit Lagadec, Francois Bremond
---
Unsupervised person re-identification (ReID) aims at learning discriminative
identity features without annotations. Recently, self-supervised contrastive
learning has gained increasing attention for its effectiveness in unsupervised
representation learning. The main idea of instance contrastive learning is to
match a same instance in different augmented views. However, the relationship
between different instances has not been fully explored in previous contrastive
methods, especially for instance-level contrastive loss. To address this issue,
we propose Inter-instance Contrastive Encoding (ICE) that leverages
inter-instance pairwise similarity scores to boost previous class-level
contrastive ReID methods. We first use pairwise similarity ranking as one-hot
hard pseudo labels for hard instance contrast, which aims at reducing
intra-class variance. Then, we use similarity scores as soft pseudo labels to
enhance the consistency between augmented and original views, which makes our
model more robust to augmentation perturbations. Experiments on several
large-scale person ReID datasets validate the effectiveness of our proposed
unsupervised method ICE, which is competitive with even supervised methods.
Code is made available at https://github.com/chenhao2345/ICE.