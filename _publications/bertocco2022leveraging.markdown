---
layout: publication
title: Leveraging Ensembles And Self-supervised Learning For Fully-unsupervised Person
  Re-identification And Text Authorship Attribution
authors: "Gabriel Bertocco, Ant\xF4nio Theophilo, Fernanda Andal\xF3, Anderson Rocha"
conference: IEEE Transactions on Information Forensics and Security
year: 2023
bibkey: bertocco2022leveraging
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.03126'}]
tags: ["Self-Supervised", "Unsupervised"]
short_authors: Bertocco et al.
---
Learning from fully-unlabeled data is challenging in Multimedia Forensics
problems, such as Person Re-Identification and Text Authorship Attribution.
Recent self-supervised learning methods have shown to be effective when dealing
with fully-unlabeled data in cases where the underlying classes have
significant semantic differences, as intra-class distances are substantially
lower than inter-class distances. However, this is not the case for forensic
applications in which classes have similar semantics and the training and test
sets have disjoint identities. General self-supervised learning methods might
fail to learn discriminative features in this scenario, thus requiring more
robust strategies. We propose a strategy to tackle Person Re-Identification and
Text Authorship Attribution by enabling learning from unlabeled data even when
samples from different classes are not prominently diverse. We propose a novel
ensemble-based clustering strategy whereby clusters derived from different
configurations are combined to generate a better grouping for the data samples
in a fully-unsupervised way. This strategy allows clusters with different
densities and higher variability to emerge, reducing intra-class discrepancies
without requiring the burden of finding an optimal configuration per dataset.
We also consider different Convolutional Neural Networks for feature extraction
and subsequent distance computations between samples. We refine these distances
by incorporating context and grouping them to capture complementary
information. Our method is robust across both tasks, with different data
modalities, and outperforms state-of-the-art methods with a fully-unsupervised
solution without any labeling or human intervention.