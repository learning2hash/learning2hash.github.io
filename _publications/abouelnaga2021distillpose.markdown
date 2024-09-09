---
layout: publication
title: "DistillPose: Lightweight Camera Localization Using Auxiliary Learning"
authors: Abouelnaga Yehya, Bui Mai, Ilic Slobodan
conference: Arxiv
year: 2021
bibkey: abouelnaga2021distillpose
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2108.03819"}
tags: ['ARXIV', 'CNN']
---
We propose a lightweight retrieval-based pipeline to predict 6DOF camera poses from RGB images. Our pipeline uses a convolutional neural network (CNN) to encode a query image as a feature vector. A nearest neighbor lookup finds the pose-wise nearest database image. A siamese convolutional neural network regresses the relative pose from the nearest neighboring database image to the query image. The relative pose is then applied to the nearest neighboring absolute pose to obtain the query image's final absolute pose prediction. Our model is a distilled version of NN-Net that reduces its parameters by 98.87%, information retrieval feature vector size by 87.5%, and inference time by 89.18% without a significant decrease in localization accuracy.