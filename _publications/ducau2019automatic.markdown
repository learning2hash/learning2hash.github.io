---
layout: publication
title: Automatic Malware Description via Attribute Tagging and Similarity Embedding
authors: Ducau et al.
conference: Arxiv
year: 2019
bibkey: ducau2019automatic
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.06262'}]
tags: []
---
With the rapid proliferation and increased sophistication of malicious
software (malware), detection methods no longer rely only on manually generated
signatures but have also incorporated more general approaches like machine
learning detection. Although powerful for conviction of malicious artifacts,
these methods do not produce any further information about the type of threat
that has been detected neither allows for identifying relationships between
malware samples. In this work, we address the information gap between machine
learning and signature-based detection methods by learning a representation
space for malware samples in which files with similar malicious behaviors
appear close to each other. We do so by introducing a deep learning based
tagging model trained to generate human-interpretable semantic descriptions of
malicious software, which, at the same time provides potentially more useful
and flexible information than malware family names.
  We show that the malware descriptions generated with the proposed approach
correctly identify more than 95% of eleven possible tag descriptions for a
given sample, at a deployable false positive rate of 1% per tag. Furthermore,
we use the learned representation space to introduce a similarity index between
malware files, and empirically demonstrate using dynamic traces from files'
execution, that is not only more effective at identifying samples from the same
families, but also 32 times smaller than those based on raw feature vectors.