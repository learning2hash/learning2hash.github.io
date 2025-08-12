---
layout: publication
title: Advancing Referring Expression Segmentation Beyond Single Image
authors: Yixuan Wu, Zhao Zhang, Xie Chi, Feng Zhu, Rui Zhao
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: wu2023advancing
citations: 15
additional_links: [{name: Code, url: 'https://github.com/yixuan730/group-res'}, {
    name: Paper, url: 'https://arxiv.org/abs/2305.12452'}]
tags: ["ICCV"]
short_authors: Wu et al.
---
Referring Expression Segmentation (RES) is a widely explored multi-modal
task, which endeavors to segment the pre-existing object within a single image
with a given linguistic expression. However, in broader real-world scenarios,
it is not always possible to determine if the described object exists in a
specific image. Typically, we have a collection of images, some of which may
contain the described objects. The current RES setting curbs its practicality
in such situations. To overcome this limitation, we propose a more realistic
and general setting, named Group-wise Referring Expression Segmentation (GRES),
which expands RES to a collection of related images, allowing the described
objects to be present in a subset of input images. To support this new setting,
we introduce an elaborately compiled dataset named Grouped Referring Dataset
(GRD), containing complete group-wise annotations of target objects described
by given expressions. We also present a baseline method named Grouped Referring
Segmenter (GRSer), which explicitly captures the language-vision and
intra-group vision-vision interactions to achieve state-of-the-art results on
the proposed GRES and related tasks, such as Co-Salient Object Detection and
RES. Our dataset and codes will be publicly released in
https://github.com/yixuan730/group-res.