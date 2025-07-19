---
layout: publication
title: Deep Learning Of Binary Hash Codes For Fast Image Retrieval
authors: Lin et al.
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2015
bibkey: lin2015deep
citations: 626
additional_links: [{name: Paper, url: 'http://www.iis.sinica.edu.tw/~kevinlin311.tw/cvprw15.pdf'}]
tags: [Hashing Methods, Image Retrieval, CVPR]
---
Approximate nearest neighbor search is an efficient strategy for large-scale image retrieval. Encouraged by the recent advances in convolutional neural networks (CNNs), we propose an effective deep learning framework to generate binary hash codes for fast image retrieval. Our idea is that when the data labels are available, binary codes can be learned by employing a hidden layer for representing the latent concepts that dominate the class labels.
he utilization of the CNN also allows for learning image representations. Unlike other supervised methods that require pair-wised inputs for binary code learning, our method learns hash codes and image representations in a point-wised manner, making it suitable for large-scale datasets. Experimental results show that our method outperforms several state-of-the-art hashing algorithms on the CIFAR-10 and MNIST datasets. We further demonstrate its scalability and efficacy on a large-scale dataset of 1 million clothing images.