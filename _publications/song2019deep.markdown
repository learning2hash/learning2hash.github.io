---
layout: publication
title: Deep Hashing Learning For Visual And Semantic Retrieval Of Remote Sensing Images
authors: Song Weiwei, Li Shutao, Benediktsson Jon Atli
conference: "Arxiv"
year: 2019
bibkey: song2019deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1909.04614"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Supervised']
---
Driven by the urgent demand for managing remote sensing big data, large-scale remote sensing image retrieval (RSIR) attracts increasing attention in the remote sensing field. In general, existing retrieval methods can be regarded as visual-based retrieval approaches which search and return a set of similar images from a database to a given query image. Although retrieval methods have achieved great success, there is still a question that needs to be responded to: Can we obtain the accurate semantic labels of the returned similar images to further help analyzing and processing imagery? Inspired by the above question, in this paper, we redefine the image retrieval problem as visual and semantic retrieval of images. Specifically, we propose a novel deep hashing convolutional neural network (DHCNN) to simultaneously retrieve the similar images and classify their semantic labels in a unified framework. In more detail, a convolutional neural network (CNN) is used to extract high-dimensional deep features. Then, a hash layer is perfectly inserted into the network to transfer the deep features into compact hash codes. In addition, a fully connected layer with a softmax function is performed on hash layer to generate class distribution. Finally, a loss function is elaborately designed to simultaneously consider the label loss of each image and similarity loss of pairs of images. Experimental results on two remote sensing datasets demonstrate that the proposed method achieves the state-of-art retrieval and classification performance.
