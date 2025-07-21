---
layout: publication
title: Multimorbidity Content-Based Medical Image Retrieval Using Proxies
authors: Xing et al.
conference: IEEE Access
year: 2023
bibkey: xing2023multimorbidity
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.12185'}]
tags: ["Image Retrieval"]
---
Content-based medical image retrieval is an important diagnostic tool that
improves the explainability of computer-aided diagnosis systems and provides
decision making support to healthcare professionals. Medical imaging data, such
as radiology images, are often multimorbidity; a single sample may have more
than one pathology present. As such, image retrieval systems for the medical
domain must be designed for the multi-label scenario. In this paper, we propose
a novel multi-label metric learning method that can be used for both
classification and content-based image retrieval. In this way, our model is
able to support diagnosis by predicting the presence of diseases and provide
evidence for these predictions by returning samples with similar pathological
content to the user. In practice, the retrieved images may also be accompanied
by pathology reports, further assisting in the diagnostic process. Our method
leverages proxy feature vectors, enabling the efficient learning of a robust
feature space in which the distance between feature vectors can be used as a
measure of the similarity of those samples. Unlike existing proxy-based
methods, training samples are able to assign to multiple proxies that span
multiple class labels. This multi-label proxy assignment results in a feature
space that encodes the complex relationships between diseases present in
medical imaging data. Our method outperforms state-of-the-art image retrieval
systems and a set of baseline approaches. We demonstrate the efficacy of our
approach to both classification and content-based image retrieval on two
multimorbidity radiology datasets.