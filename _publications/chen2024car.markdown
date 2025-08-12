---
layout: publication
title: Car Damage Detection And Patch-to-patch Self-supervised Image Alignment
authors: Hanxiao Chen
conference: Arxiv
year: 2024
bibkey: chen2024car
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.06674'}]
tags: ["Self-Supervised"]
short_authors: Hanxiao Chen
---
Most computer vision applications aim to identify pixels in a scene and use
them for diverse purposes. One intriguing application is car damage detection
for insurance carriers which tends to detect all car damages by comparing both
pre-trip and post-trip images, even requiring two components: (i) car damage
detection; (ii) image alignment. Firstly, we implemented a Mask R-CNN model to
detect car damages on custom images. Whereas for the image alignment section,
we especially propose a novel self-supervised Patch-to-Patch SimCLR inspired
alignment approach to find perspective transformations between custom pre/post
car rental images except for traditional computer vision methods.