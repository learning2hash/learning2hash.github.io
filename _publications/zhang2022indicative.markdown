---
layout: publication
title: 'Indicative Image Retrieval: Turning Blackbox Learning Into Grey'
authors: Xulu Zhang, Zhenqun Yang, Hao Tian, Qing Li, Xiaoyong Wei
conference: Arxiv
year: 2022
bibkey: zhang2022indicative
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.11898'}]
tags: ["Image Retrieval"]
short_authors: Zhang et al.
---
Deep learning became the game changer for image retrieval soon after it was
introduced. It promotes the feature extraction (by representation learning) as
the core of image retrieval, with the relevance/matching evaluation being
degenerated into simple similarity metrics. In many applications, we need the
matching evidence to be indicated rather than just have the ranked list (e.g.,
the locations of the target proteins/cells/lesions in medical images). It is
like the matched words need to be highlighted in search engines. However, this
is not easy to implement without explicit relevance/matching modeling. The deep
representation learning models are not feasible because of their blackbox
nature. In this paper, we revisit the importance of relevance/matching modeling
in deep learning era with an indicative retrieval setting. The study shows that
it is possible to skip the representation learning and model the matching
evidence directly. By removing the dependency on the pre-trained models, it has
avoided a lot of related issues (e.g., the domain gap between classification
and retrieval, the detail-diffusion caused by convolution, and so on). More
importantly, the study demonstrates that the matching can be explicitly modeled
and backtracked later for generating the matching evidence indications. It can
improve the explainability of deep inference. Our method obtains a best
performance in literature on both Oxford-5k and Paris-6k, and sets a new record
of 97.77% on Oxford-5k (97.81% on Paris-6k) without extracting any deep
features.