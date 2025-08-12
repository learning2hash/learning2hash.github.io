---
layout: publication
title: Image Segmentation For Fruit Detection And Yield Estimation In Apple Orchards
authors: Suchet Bargoti, James Underwood
conference: Journal of Field Robotics
year: 2017
bibkey: bargoti2016image
citations: 439
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.08120'}]
tags: ["Datasets", "Evaluation"]
short_authors: Suchet Bargoti, James Underwood
---
Ground vehicles equipped with monocular vision systems are a valuable source
of high resolution image data for precision agriculture applications in
orchards. This paper presents an image processing framework for fruit detection
and counting using orchard image data. A general purpose image segmentation
approach is used, including two feature learning algorithms; multi-scale
Multi-Layered Perceptrons (MLP) and Convolutional Neural Networks (CNN). These
networks were extended by including contextual information about how the image
data was captured (metadata), which correlates with some of the appearance
variations and/or class distributions observed in the data. The pixel-wise
fruit segmentation output is processed using the Watershed Segmentation (WS)
and Circular Hough Transform (CHT) algorithms to detect and count individual
fruits. Experiments were conducted in a commercial apple orchard near
Melbourne, Australia. The results show an improvement in fruit segmentation
performance with the inclusion of metadata on the previously benchmarked MLP
network. We extend this work with CNNs, bringing agrovision closer to the
state-of-the-art in computer vision, where although metadata had negligible
influence, the best pixel-wise F1-score of \\(0.791\\) was achieved. The WS
algorithm produced the best apple detection and counting results, with a
detection F1-score of \\(0.858\\). As a final step, image fruit counts were
accumulated over multiple rows at the orchard and compared against the
post-harvest fruit counts that were obtained from a grading and counting
machine. The count estimates using CNN and WS resulted in the best performance
for this dataset, with a squared correlation coefficient of \\(r^2=0.826\\).