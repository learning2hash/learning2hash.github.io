---
layout: publication
title: Few-shot Fruit Segmentation Via Transfer Learning
authors: Jordan A. James, Heather K. Manching, Amanda M. Hulse-Kemp, William J. Beksi
conference: 2024 IEEE International Conference on Robotics and Automation (ICRA)
year: 2024
bibkey: james2024few
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.02556'}]
tags: ["Few Shot & Zero Shot", "ICRA"]
short_authors: James et al.
---
Advancements in machine learning, computer vision, and robotics have paved
the way for transformative solutions in various domains, particularly in
agriculture. For example, accurate identification and segmentation of fruits
from field images plays a crucial role in automating jobs such as harvesting,
disease detection, and yield estimation. However, achieving robust and precise
infield fruit segmentation remains a challenging task since large amounts of
labeled data are required to handle variations in fruit size, shape, color, and
occlusion. In this paper, we develop a few-shot semantic segmentation framework
for infield fruits using transfer learning. Concretely, our work is aimed at
addressing agricultural domains that lack publicly available labeled data.
Motivated by similar success in urban scene parsing, we propose specialized
pre-training using a public benchmark dataset for fruit transfer learning. By
leveraging pre-trained neural networks, accurate semantic segmentation of fruit
in the field is achieved with only a few labeled images. Furthermore, we show
that models with pre-training learn to distinguish between fruit still on the
trees and fruit that have fallen on the ground, and they can effectively
transfer the knowledge to the target fruit dataset.