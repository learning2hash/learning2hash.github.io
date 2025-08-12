---
layout: publication
title: 'S\(^3\)AD: Semi-supervised Small Apple Detection In Orchard Environments'
authors: Robert Johanson, Christian Wilms, Ole Johannsen, Simone Frintrop
conference: Arxiv
year: 2023
bibkey: johanson2023s
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.05029'}]
tags: []
short_authors: Johanson et al.
---
Crop detection is integral for precision agriculture applications such as
automated yield estimation or fruit picking. However, crop detection, e.g.,
apple detection in orchard environments remains challenging due to a lack of
large-scale datasets and the small relative size of the crops in the image. In
this work, we address these challenges by reformulating the apple detection
task in a semi-supervised manner. To this end, we provide the large,
high-resolution dataset MAD comprising 105 labeled images with 14,667 annotated
apple instances and 4,440 unlabeled images. Utilizing this dataset, we also
propose a novel Semi-Supervised Small Apple Detection system S\(^3\)AD based on
contextual attention and selective tiling to improve the challenging detection
of small apples, while limiting the computational overhead. We conduct an
extensive evaluation on MAD and the MSU dataset, showing that S\(^3\)AD
substantially outperforms strong fully-supervised baselines, including several
small object detection systems, by up to \(14.9%\). Additionally, we exploit the
detailed annotations of our dataset w.r.t. apple properties to analyze the
influence of relative size or level of occlusion on the results of various
systems, quantifying current challenges.