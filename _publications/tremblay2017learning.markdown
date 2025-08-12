---
layout: publication
title: 'Learning To Segment On Tiny Datasets: A New Shape Model'
authors: "Maxime Tremblay, Andr\xE9 Zaccarin"
conference: Arxiv
year: 2017
bibkey: tremblay2017learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.02165'}]
tags: ["Datasets"]
short_authors: "Maxime Tremblay, Andr\xE9 Zaccarin"
---
Current object segmentation algorithms are based on the hypothesis that one
has access to a very large amount of data. In this paper, we aim to segment
objects using only tiny datasets. To this extent, we propose a new automatic
part-based object segmentation algorithm for non-deformable and semi-deformable
objects in natural backgrounds. We have developed a novel shape descriptor
which models the local boundaries of an object's part. This shape descriptor is
used in a bag-of-words approach for object detection. Once the detection
process is performed, we use the background and foreground likelihood given by
our trained shape model, and the information from the image content, to define
a dense CRF model. We use a mean field approximation to solve it and thus
segment the object of interest. Performance evaluated on different datasets
shows that our approach can sometimes achieve results near state-of-the-art
techniques based on big data while requiring only a tiny training set.