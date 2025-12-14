---
layout: publication
title: Open-vocabulary Mobile Manipulation Based On Double Relaxed Contrastive Learning
  With Dense Labeling
authors: Daichi Yashima, Ryosuke Korekata, Komei Sugiura
conference: Arxiv
year: 2024
bibkey: yashima2024open
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.16576'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Self-Supervised, Datasets]
short_authors: Daichi Yashima, Ryosuke Korekata, Komei Sugiura
---
Growing labor shortages are increasing the demand for domestic service robots
(DSRs) to assist in various settings. In this study, we develop a DSR that
transports everyday objects to specified pieces of furniture based on
open-vocabulary instructions. Our approach focuses on retrieving images of
target objects and receptacles from pre-collected images of indoor
environments. For example, given an instruction "Please get the right red towel
hanging on the metal towel rack and put it in the white washing machine on the
left," the DSR is expected to carry the red towel to the washing machine based
on the retrieved images. This is challenging because the correct images should
be retrieved from thousands of collected images, which may include many images
of similar towels and appliances. To address this, we propose RelaX-Former,
which learns diverse and robust representations from among positive, unlabeled
positive, and negative samples. We evaluated RelaX-Former on a dataset
containing real-world indoor images and human annotated instructions including
complex referring expressions. The experimental results demonstrate that
RelaX-Former outperformed existing baseline models across standard image
retrieval metrics. Moreover, we performed physical experiments using a DSR to
evaluate the performance of our approach in a zero-shot transfer setting. The
experiments involved the DSR to carry objects to specific receptacles based on
open-vocabulary instructions, achieving an overall success rate of 75%.