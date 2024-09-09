---
layout: publication
title: Voronoi-based compact image descriptors Efficient Region-of-Interest retrieval with VLAD and deep-learning-based descriptors
authors: Chadha Aaron, Andreopoulos Yiannis
conference: "Arxiv"
year: 2016
bibkey: chadha2016voronoi
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.08906"}
tags: ['ARXIV', 'CNN', 'Deep Learning', 'Image Retrieval', 'TOM']
---
We investigate the problem of image retrieval based on visual queries when the latter comprise arbitrary regions-of-interest (ROI) rather than entire images. Our proposal is a compact image descriptor that combines the state-of-the-art in content-based descriptor extraction with a multi-level Voronoi-based spatial partitioning of each dataset image. The proposed multi-level Voronoi-based encoding uses a spatial hierarchical K-means over interest-point locations and computes a content-based descriptor over each cell. In order to reduce the matching complexity with minimal or no sacrifice in retrieval performance (i) we utilize the tree structure of the spatial hierarchical K-means to perform a top-to-bottom pruning for local similarity maxima; (ii) we propose a new image similarity score that combines relevant information from all partition levels into a single measure for similarity; (iii) we combine our proposal with a novel and efficient approach for optimal bit allocation within quantized descriptor representations. By deriving both a Voronoi-based VLAD descriptor (termed as Fast-VVLAD) and a Voronoi-based deep convolutional neural network (CNN) descriptor (termed as Fast-VDCNN) we demonstrate that our Voronoi-based framework is agnostic to the descriptor basis and can easily be slotted into existing frameworks. Via a range of ROI queries in two standard datasets it is shown that the Voronoi-based descriptors achieve comparable or higher mean Average Precision against conventional grid-based spatial search while offering more than two-fold reduction in complexity. Finally beyond ROI queries we show that Voronoi partitioning improves the geometric invariance of compact CNN descriptors thereby resulting in competitive performance to the current state-of-the-art on whole image retrieval.
