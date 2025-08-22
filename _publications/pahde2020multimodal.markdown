---
layout: publication
title: Multimodal Prototypical Networks For Few-shot Learning
authors: Frederik Pahde, Mihai Puscas, Tassilo Klein, Moin Nabi
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: pahde2020multimodal
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.08899'}]
tags: ["Datasets", "Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: Pahde et al.
---
Although providing exceptional results for many computer vision tasks,
state-of-the-art deep learning algorithms catastrophically struggle in low data
scenarios. However, if data in additional modalities exist (e.g. text) this can
compensate for the lack of data and improve the classification results. To
overcome this data scarcity, we design a cross-modal feature generation
framework capable of enriching the low populated embedding space in few-shot
scenarios, leveraging data from the auxiliary modality. Specifically, we train
a generative model that maps text data into the visual feature space to obtain
more reliable prototypes. This allows to exploit data from additional
modalities (e.g. text) during training while the ultimate task at test time
remains classification with exclusively visual data. We show that in such cases
nearest neighbor classification is a viable approach and outperform
state-of-the-art single-modal and multimodal few-shot learning methods on the
CUB-200 and Oxford-102 datasets.