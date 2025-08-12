---
layout: publication
title: File Fragment Classification Using Light-weight Convolutional Neural Networks
authors: Mustafa Ghaleb, Kunwar Saaim, Muhamad Felemban, Saleh Al-Saleh, Ahmad Al-Mulhem
conference: IEEE Access.12. (2024) 157179-157191
year: 2023
bibkey: ghaleb2023file
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.00656'}]
tags: []
short_authors: Ghaleb et al.
---
In digital forensics, file fragment classification is an important step
toward completing file carving process. There exist several techniques to
identify the type of file fragments without relying on meta-data, such as using
features like header/footer and N-gram to identify the fragment type. Recently,
convolutional neural network (CNN) models have been used to build
classification models to achieve this task. However, the number of parameters
in CNNs tends to grow exponentially as the number of layers increases. This
results in a dramatic increase in training and inference time. In this paper,
we propose light-weight file fragment classification models based on depthwise
separable CNNs. The evaluation results show that our proposed models provide
faster inference time with comparable accuracy as compared to the state-of-art
CNN based models. In particular, our models were able to achieve an accuracy of
79% on the FFT-75 dataset with nearly 100K parameters and 164M FLOPs, which is
4x smaller and 6x faster than the state-of-the-art classifier in the
literature.