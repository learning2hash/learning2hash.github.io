---
layout: publication
title: A Fine-grained Vehicle Detection (FGVD) Dataset For Unconstrained Roads
authors: Prafful Kumar Khoba, Chirag Parikh, Rohit Saluja, Ravi Kiran Sarvadevabhatla,
  C. V. Jawahar
conference: Proceedings of the Thirteenth Indian Conference on Computer Vision, Graphics
  and Image Processing
year: 2022
bibkey: khoba2022fine
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.14569'}]
tags: ["Datasets"]
short_authors: Khoba et al.
---
The previous fine-grained datasets mainly focus on classification and are
often captured in a controlled setup, with the camera focusing on the objects.
We introduce the first Fine-Grained Vehicle Detection (FGVD) dataset in the
wild, captured from a moving camera mounted on a car. It contains 5502 scene
images with 210 unique fine-grained labels of multiple vehicle types organized
in a three-level hierarchy. While previous classification datasets also include
makes for different kinds of cars, the FGVD dataset introduces new class labels
for categorizing two-wheelers, autorickshaws, and trucks. The FGVD dataset is
challenging as it has vehicles in complex traffic scenarios with intra-class
and inter-class variations in types, scale, pose, occlusion, and lighting
conditions. The current object detectors like yolov5 and faster RCNN perform
poorly on our dataset due to a lack of hierarchical modeling. Along with
providing baseline results for existing object detectors on FGVD Dataset, we
also present the results of a combination of an existing detector and the
recent Hierarchical Residual Network (HRN) classifier for the FGVD task.
Finally, we show that FGVD vehicle images are the most challenging to classify
among the fine-grained datasets.