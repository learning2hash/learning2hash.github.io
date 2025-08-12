---
layout: publication
title: 'Histonet: Predicting Size Histograms Of Object Instances'
authors: "Kishan Sharma, Moritz Gold, Christian Zurbruegg, Laura Leal-taix\xE9, Jan\
  \ Dirk Wegner"
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: sharma2019histonet
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.05227'}]
tags: []
short_authors: Sharma et al.
---
We propose to predict histograms of object sizes in crowded scenes directly
without any explicit object instance segmentation. What makes this task
challenging is the high density of objects (of the same category), which makes
instance identification hard. Instead of explicitly segmenting object
instances, we show that directly learning histograms of object sizes improves
accuracy while using drastically less parameters. This is very useful for
application scenarios where explicit, pixel-accurate instance segmentation is
not needed, but there lies interest in the overall distribution of instance
sizes. Our core applications are in biology, where we estimate the size
distribution of soldier fly larvae, and medicine, where we estimate the size
distribution of cancer cells as an intermediate step to calculate the tumor
cellularity score. Given an image with hundreds of small object instances, we
output the total count and the size histogram. We also provide a new data set
for this task, the FlyLarvae data set, which consists of 11,000 larvae
instances labeled pixel-wise. Our method results in an overall improvement in
the count and size distribution prediction as compared to state-of-the-art
instance segmentation method Mask R-CNN.