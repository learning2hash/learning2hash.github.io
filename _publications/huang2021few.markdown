---
layout: publication
title: Few-shot Unsupervised Domain Adaptation With Image-to-class Sparse Similarity
  Encoding
authors: Shengqi Huang, Wanqi Yang, Lei Wang, Luping Zhou, Ming Yang
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: huang2021few
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.02953'}]
tags: ["Few Shot & Zero Shot", "Unsupervised"]
short_authors: Huang et al.
---
This paper investigates a valuable setting called few-shot unsupervised
domain adaptation (FS-UDA), which has not been sufficiently studied in the
literature. In this setting, the source domain data are labelled, but with
few-shot per category, while the target domain data are unlabelled. To address
the FS-UDA setting, we develop a general UDA model to solve the following two
key issues: the few-shot labeled data per category and the domain adaptation
between support and query sets. Our model is general in that once trained it
will be able to be applied to various FS-UDA tasks from the same source and
target domains. Inspired by the recent local descriptor based few-shot learning
(FSL), our general UDA model is fully built upon local descriptors (LDs) for
image classification and domain adaptation. By proposing a novel concept called
similarity patterns (SPs), our model not only effectively considers the spatial
relationship of LDs that was ignored in previous FSL methods, but also makes
the learned image similarity better serve the required domain alignment.
Specifically, we propose a novel IMage-to-class sparse Similarity Encoding
(IMSE) method. It learns SPs to extract the local discriminative information
for classification and meanwhile aligns the covariance matrix of the SPs for
domain adaptation. Also, domain adversarial training and multi-scale local
feature matching are performed upon LDs. Extensive experiments conducted on a
multi-domain benchmark dataset DomainNet demonstrates the state-of-the-art
performance of our IMSE for the novel setting of FS-UDA. In addition, for FSL,
our IMSE can also show better performance than most of recent FSL methods on
miniImageNet.