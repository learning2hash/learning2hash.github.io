---
layout: publication
title: Voronoi45;based Compact Image Descriptors Efficient Region45;of45;interest Retrieval With VLAD And Deep45;learning45;based Descriptors
authors: Chadha Aaron, Andreopoulos Yiannis
conference: "Arxiv"
year: 2016
bibkey: chadha2016compact
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1611.08906"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Supervised']
---
We investigate the problem of image retrieval based on visual queries when the latter comprise arbitrary regions45;of45;interest (ROI) rather than entire images. Our proposal is a compact image descriptor that combines the state45;of45;the45;art in content45;based descriptor extraction with a multi45;level Voronoi45;based spatial partitioning of each dataset image. The proposed multi45;level Voronoi45;based encoding uses a spatial hierarchical K45;means over interest45;point locations and computes a content45;based descriptor over each cell. In order to reduce the matching complexity with minimal or no sacrifice in retrieval performance (i) we utilize the tree structure of the spatial hierarchical K45;means to perform a top45;to45;bottom pruning for local similarity maxima; (ii) we propose a new image similarity score that combines relevant information from all partition levels into a single measure for similarity; (iii) we combine our proposal with a novel and efficient approach for optimal bit allocation within quantized descriptor representations. By deriving both a Voronoi45;based VLAD descriptor (termed as Fast45;VVLAD) and a Voronoi45;based deep convolutional neural network (CNN) descriptor (termed as Fast45;VDCNN) we demonstrate that our Voronoi45;based framework is agnostic to the descriptor basis and can easily be slotted into existing frameworks. Via a range of ROI queries in two standard datasets it is shown that the Voronoi45;based descriptors achieve comparable or higher mean Average Precision against conventional grid45;based spatial search while offering more than two45;fold reduction in complexity. Finally beyond ROI queries we show that Voronoi partitioning improves the geometric invariance of compact CNN descriptors thereby resulting in competitive performance to the current state45;of45;the45;art on whole image retrieval.
