---
layout: publication
title: Object-centric Cross-modal Feature Distillation For Event-based Object Detection
authors: Lei Li, Alexander Liniger, Mario Millhaeusler, Vagia Tsiminaki, Yuanyou Li,
  Dengxin Dai
conference: 2024 IEEE International Conference on Robotics and Automation (ICRA)
year: 2024
bibkey: li2023object
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.05494'}]
tags: ["ICRA"]
short_authors: Li et al.
---
Event cameras are gaining popularity due to their unique properties, such as
their low latency and high dynamic range. One task where these benefits can be
crucial is real-time object detection. However, RGB detectors still outperform
event-based detectors due to the sparsity of the event data and missing visual
details. In this paper, we develop a novel knowledge distillation approach to
shrink the performance gap between these two modalities. To this end, we
propose a cross-modality object detection distillation method that by design
can focus on regions where the knowledge distillation works best. We achieve
this by using an object-centric slot attention mechanism that can iteratively
decouple features maps into object-centric features and corresponding
pixel-features used for distillation. We evaluate our novel distillation
approach on a synthetic and a real event dataset with aligned grayscale images
as a teacher modality. We show that object-centric distillation allows to
significantly improve the performance of the event-based student object
detector, nearly halving the performance gap with respect to the teacher.