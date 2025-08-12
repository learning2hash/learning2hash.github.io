---
layout: publication
title: Class-agnostic Visio-temporal Scene Sketch Semantic Segmentation
authors: "Aleyna K\xFCt\xFCk, Tevfik Metin Sezgin"
conference: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2025
bibkey: "k\xFCt\xFCk2024class"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.00266'}]
tags: ["Datasets", "Evaluation"]
short_authors: "Aleyna K\xFCt\xFCk, Tevfik Metin Sezgin"
---
Scene sketch semantic segmentation is a crucial task for various applications
including sketch-to-image retrieval and scene understanding. Existing sketch
segmentation methods treat sketches as bitmap images, leading to the loss of
temporal order among strokes due to the shift from vector to image format.
Moreover, these methods struggle to segment objects from categories absent in
the training data. In this paper, we propose a Class-Agnostic Visio-Temporal
Network (CAVT) for scene sketch semantic segmentation. CAVT employs a
class-agnostic object detector to detect individual objects in a scene and
groups the strokes of instances through its post-processing module. This is the
first approach that performs segmentation at both the instance and stroke
levels within scene sketches. Furthermore, there is a lack of free-hand scene
sketch datasets with both instance and stroke-level class annotations. To fill
this gap, we collected the largest Free-hand Instance- and Stroke-level Scene
Sketch Dataset (FrISS) that contains 1K scene sketches and covers 403 object
classes with dense annotations. Extensive experiments on FrISS and other
datasets demonstrate the superior performance of our method over
state-of-the-art scene sketch segmentation models. The code and dataset will be
made public after acceptance.