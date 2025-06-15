---
layout: publication
title: 'Radon Features And Barcodes For Medical Image Retrieval Via SVM'
authors: Shujin Zhu, H. R. Tizhoosh
conference: "Arxiv"
year: 2016
citations: 10
bibkey: zhu2016radon
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1604.04675'}
tags: ['Cross-Modal', 'Independent', 'Retrieval Models', 'Evaluation', 'Shallow', 'Applications']
---
For more than two decades, research has been performed on content-based image
retrieval (CBIR). By combining Radon projections and the support vector
machines (SVM), a content-based medical image retrieval method is presented in
this work. The proposed approach employs the normalized Radon projections with
corresponding image category labels to build an SVM classifier, and the Radon
barcode database which encodes every image in a binary format is also generated
simultaneously to tag all images. To retrieve similar images when a query image
is given, Radon projections and the barcode of the query image are generated.
Subsequently, the k-nearest neighbor search method is applied to find the
images with minimum Hamming distance of the Radon barcode within the same class
predicted by the trained SVM classifier that uses Radon features. The
performance of the proposed method is validated by using the IRMA 2009 dataset
with 14,410 x-ray images in 57 categories. The results demonstrate that our
method has the capacity to retrieve similar responses for the correctly
identified query image and even for those mistakenly classified by SVM. The
approach further is very fast and has low memory requirement.
