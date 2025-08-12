---
layout: publication
title: 'Syn2real: Forgery Classification Via Unsupervised Domain Adaptation'
authors: Akash Kumar, Arnav Bhavasar
conference: 2020 IEEE Winter Applications of Computer Vision Workshops (WACVW)
year: 2020
bibkey: kumar2020syn2real
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.00807'}]
tags: ["Unsupervised"]
short_authors: Akash Kumar, Arnav Bhavasar
---
In recent years, image manipulation is becoming increasingly more accessible,
yielding more natural-looking images, owing to the modern tools in image
processing and computer vision techniques. The task of the identification of
forged images has become very challenging. Amongst different types of
forgeries, the cases of Copy-Move forgery are increasing manifold, due to the
difficulties involved to detect this tampering. To tackle such problems,
publicly available datasets are insufficient. In this paper, we propose to
create a synthetic forged dataset using deep semantic image inpainting and
copy-move forgery algorithm. However, models trained on these datasets have a
significant drop in performance when tested on more realistic data. To
alleviate this problem, we use unsupervised domain adaptation networks to
detect copy-move forgery in new domains by mapping the feature space from our
synthetically generated dataset. Furthermore, we improvised the F1 score on
CASIA and CoMoFoD dataset to 80.3% and 78.8%, respectively. Our approach can be
helpful in those cases where the classification of data is unavailable.