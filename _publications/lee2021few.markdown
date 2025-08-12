---
layout: publication
title: Few-shot Object Detection By Attending To Per-sample-prototype
authors: Hojun Lee, Myunggi Lee, Nojun Kwak
conference: 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2022
bibkey: lee2021few
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.07734'}]
tags: []
short_authors: Hojun Lee, Myunggi Lee, Nojun Kwak
---
Few-shot object detection aims to detect instances of specific categories in
a query image with only a handful of support samples. Although this takes less
effort than obtaining enough annotated images for supervised object detection,
it results in a far inferior performance compared to the conventional object
detection methods. In this paper, we propose a meta-learning-based approach
that considers the unique characteristics of each support sample. Rather than
simply averaging the information of the support samples to generate a single
prototype per category, our method can better utilize the information of each
support sample by treating each support sample as an individual prototype.
Specifically, we introduce two types of attention mechanisms for aggregating
the query and support feature maps. The first is to refine the information of
few-shot samples by extracting shared information between the support samples
through attention. Second, each support sample is used as a class code to
leverage the information by comparing similarities between each support feature
and query features. Our proposed method is complementary to the previous
methods, making it easy to plug and play for further improvement. We have
evaluated our method on PASCAL VOC and COCO benchmarks, and the results verify
the effectiveness of our method. In particular, the advantages of our method
are maximized when there is more diversity among support data.