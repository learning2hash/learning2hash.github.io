---
layout: publication
title: 'Nocplace: Nocturnal Visual Place Recognition Via Generative And Inherited
  Knowledge Transfer'
authors: Bingxi Liu, Yiqun Wang, Huaqi Tao, Tingjun Huang, Fulin Tang, Yihong Wu,
  Jinqiang Cui, Hong Zhang
conference: Arxiv
year: 2024
bibkey: liu2024nocplace
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.17159'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Scalability"]
short_authors: Liu et al.
---
Visual Place Recognition (VPR) is crucial in computer vision, aiming to
retrieve database images similar to a query image from an extensive collection
of known images. However, like many vision tasks, VPR always degrades at night
due to the scarcity of nighttime images. Moreover, VPR needs to address the
cross-domain problem of night-to-day rather than just the issue of a single
nighttime domain. In response to these issues, we present NocPlace, which
leverages generative and inherited knowledge transfer to embed resilience
against dazzling lights and extreme darkness in the global descriptor. First,
we establish a day-night urban scene dataset called NightCities, capturing
diverse lighting variations and dark scenarios across 60 cities globally. Then,
an image generation network is trained on this dataset and processes a
large-scale VPR dataset, obtaining its nighttime version. Finally, VPR models
are fine-tuned using descriptors inherited from themselves and night-style
images, which builds explicit cross-domain contrastive relationships.
Comprehensive experiments on various datasets demonstrate our contributions and
the superiority of NocPlace. Without adding any real-time computing resources,
NocPlace improves the performance of Eigenplaces by 7.6% on Tokyo 24/7 Night
and 16.8% on SVOX Night.