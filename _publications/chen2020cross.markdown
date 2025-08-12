---
layout: publication
title: Cross-supervised Object Detection
authors: Zitian Chen, Zhiqiang Shen, Jiahui Yu, Erik Learned-Miller
conference: Arxiv
year: 2020
bibkey: chen2020cross
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.15056'}]
tags: ["Supervised"]
short_authors: Chen et al.
---
After learning a new object category from image-level annotations (with no
object bounding boxes), humans are remarkably good at precisely localizing
those objects. However, building good object localizers (i.e., detectors)
currently requires expensive instance-level annotations. While some work has
been done on learning detectors from weakly labeled samples (with only class
labels), these detectors do poorly at localization. In this work, we show how
to build better object detectors from weakly labeled images of new categories
by leveraging knowledge learned from fully labeled base categories. We call
this novel learning paradigm cross-supervised object detection. We propose a
unified framework that combines a detection head trained from instance-level
annotations and a recognition head learned from image-level annotations,
together with a spatial correlation module that bridges the gap between
detection and recognition. These contributions enable us to better detect novel
objects with image-level annotations in complex multi-object scenes such as the
COCO dataset.