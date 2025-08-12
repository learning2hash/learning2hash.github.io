---
layout: publication
title: Weakly Supervised Dataset Collection For Robust Person Detection
authors: Munetaka Minoguchi, Ken Okayama, Yutaka Satoh, Hirokatsu Kataoka
conference: Arxiv
year: 2020
bibkey: minoguchi2020weakly
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.12263'}]
tags: ["Datasets"]
short_authors: Minoguchi et al.
---
To construct an algorithm that can provide robust person detection, we
present a dataset with over 8 million images that was produced in a weakly
supervised manner. Through labor-intensive human annotation, the person
detection research community has produced relatively small datasets containing
on the order of 100,000 images, such as the EuroCity Persons dataset, which
includes 240,000 bounding boxes. Therefore, we have collected 8.7 million
images of persons based on a two-step collection process, namely person
detection with an existing detector and data refinement for false positive
suppression. According to the experimental results, the Weakly Supervised
Person Dataset (WSPD) is simple yet effective for person detection
pre-training. In the context of pre-trained person detection algorithms, our
WSPD pre-trained model has 13.38 and 6.38% better accuracy than the same model
trained on the fully supervised ImageNet and EuroCity Persons datasets,
respectively, when verified with the Caltech Pedestrian.