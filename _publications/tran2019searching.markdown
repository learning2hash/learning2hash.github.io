---
layout: publication
title: Searching For Apparel Products From Images In The Wild
authors: Tran Son, Du Ming, Chanda Sampath, Manmatha R., Taylor Cj
conference: Arxiv
year: 2019
bibkey: tran2019searching
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.02244'}]
tags: ["Evaluation", "Datasets"]
short_authors: Tran et al.
---
In this age of social media, people often look at what others are wearing. In
particular, Instagram and Twitter influencers often provide images of
themselves wearing different outfits and their followers are often inspired to
buy similar clothes.We propose a system to automatically find the closest
visually similar clothes in the online Catalog (street-to-shop searching). The
problem is challenging since the original images are taken under different pose
and lighting conditions. The system initially localizes high-level descriptive
regions (top, bottom, wristwear. . . ) using multiple CNN detectors such as
YOLO and SSD that are trained specifically for apparel domain. It then
classifies these regions into more specific regions such as t-shirts, tunic or
dresses. Finally, a feature embedding learned using a multi-task function is
recovered for every item and then compared with corresponding items in the
online Catalog database and ranked according to distance. We validate our
approach component-wise using benchmark datasets and end-to-end using human
evaluation.