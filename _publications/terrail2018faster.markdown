---
layout: publication
title: 'Faster RER-CNN: Application To The Detection Of Vehicles In Aerial Images'
authors: "Jean Ogier Du Terrail, Fr\xE9d\xE9ric Jurie"
conference: Arxiv
year: 2018
bibkey: terrail2018faster
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.07628'}]
tags: []
short_authors: "Jean Ogier Du Terrail, Fr\xE9d\xE9ric Jurie"
---
Detecting small vehicles in aerial images is a difficult job that can be
challenging even for humans. Rotating objects, low resolution, small
inter-class variability and very large images comprising complicated
backgrounds render the work of photo-interpreters tedious and wearisome.
Unfortunately even the best classical detection pipelines like Faster R-CNN
cannot be used off-the-shelf with good results because they were built to
process object centric images from day-to-day life with multi-scale vertical
objects. In this work we build on the Faster R-CNN approach to turn it into a
detection framework that deals appropriately with the rotation equivariance
inherent to any aerial image task. This new pipeline (Faster Rotation
Equivariant Regions CNN) gives, without any bells and whistles,
state-of-the-art results on one of the most challenging aerial imagery
datasets: VeDAI and give good results w.r.t. the baseline Faster R-CNN on two
others: Munich and GoogleEarth .