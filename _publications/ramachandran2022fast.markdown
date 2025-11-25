---
layout: publication
title: Fast And Efficient Scene Categorization For Autonomous Driving Using Vaes
authors: Saravanabalagi Ramachandran, Jonathan Horgan, Ganesh Sistu, John McDonald
conference: 24th Irish Machine Vision and Image Processing Conference
year: 2022
bibkey: ramachandran2022fast
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.14981'}]
tags: ["Efficiency", "Evaluation", "Unsupervised"]
short_authors: Ramachandran et al.
---
Scene categorization is a useful precursor task that provides prior knowledge
for many advanced computer vision tasks with a broad range of applications in
content-based image indexing and retrieval systems. Despite the success of data
driven approaches in the field of computer vision such as object detection,
semantic segmentation, etc., their application in learning high-level features
for scene recognition has not achieved the same level of success. We propose to
generate a fast and efficient intermediate interpretable generalized global
descriptor that captures coarse features from the image and use a
classification head to map the descriptors to 3 scene categories: Rural, Urban
and Suburban. We train a Variational Autoencoder in an unsupervised manner and
map images to a constrained multi-dimensional latent space and use the latent
vectors as compact embeddings that serve as global descriptors for images. The
experimental results evidence that the VAE latent vectors capture coarse
information from the image, supporting their usage as global descriptors. The
proposed global descriptor is very compact with an embedding length of 128,
significantly faster to compute, and is robust to seasonal and illuminational
changes, while capturing sufficient scene information required for scene
categorization.