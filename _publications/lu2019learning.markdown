---
layout: publication
title: Learning Effective Visual Relationship Detector On 1 GPU
authors: Yichao Lu, Cheng Chang, Himanshu Rai, Guangwei Yu, Maksims Volkovs
conference: Arxiv
year: 2019
bibkey: lu2019learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.06185'}]
tags: []
short_authors: Lu et al.
---
We present our winning solution to the Open Images 2019 Visual Relationship
challenge. This is the largest challenge of its kind to date with nearly 9
million training images. Challenge task consists of detecting objects and
identifying relationships between them in complex scenes. Our solution has
three stages, first object detection model is fine-tuned for the challenge
classes using a novel weight transfer approach. Then, spatio-semantic and
visual relationship models are trained on candidate object pairs. Finally,
features and model predictions are combined to generate the final relationship
prediction. Throughout the challenge we focused on minimizing the hardware
requirements of our architecture. Specifically, our weight transfer approach
enables much faster optimization, allowing the entire architecture to be
trained on a single GPU in under two days. In addition to efficient
optimization, our approach also achieves superior accuracy winning first place
out of over 200 teams, and outperforming the second place team by over \(5%\) on
the held-out private leaderboard.