---
layout: publication
title: Unsupervised Learning Of Object-centric Embeddings For Cell Instance Segmentation
  In Microscopy Images
authors: Steffen Wolf, Manan Lalit, Henry Westmacott, Katie McDole, Jan Funke
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: wolf2023unsupervised
citations: 6
additional_links: [{name: Code, url: 'https://github.com/funkelab/cellulus'}, {name: Paper,
    url: 'https://arxiv.org/abs/2310.08501'}]
tags: ["ICCV", "Unsupervised"]
short_authors: Wolf et al.
---
Segmentation of objects in microscopy images is required for many biomedical
applications. We introduce object-centric embeddings (OCEs), which embed image
patches such that the spatial offsets between patches cropped from the same
object are preserved. Those learnt embeddings can be used to delineate
individual objects and thus obtain instance segmentations. Here, we show
theoretically that, under assumptions commonly found in microscopy images, OCEs
can be learnt through a self-supervised task that predicts the spatial offset
between image patches. Together, this forms an unsupervised cell instance
segmentation method which we evaluate on nine diverse large-scale microscopy
datasets. Segmentations obtained with our method lead to substantially improved
results, compared to state-of-the-art baselines on six out of nine datasets,
and perform on par on the remaining three datasets. If ground-truth annotations
are available, our method serves as an excellent starting point for supervised
training, reducing the required amount of ground-truth needed by one order of
magnitude, thus substantially increasing the practical applicability of our
method. Source code is available at https://github.com/funkelab/cellulus.