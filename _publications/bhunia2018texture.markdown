---
layout: publication
title: Texture Synthesis Guided Deep Hashing for Texture Image Retrieval
authors: Bhunia Ayan Kumar, Kishore Perla Sai Raj, Mukherjee Pranay, Das Abhirup,
  Roy Partha Pratim
conference: 2019 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2019
bibkey: bhunia2018texture
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.01401'}]
tags: ["Similarity-Search", "Image-Retrieval", "Hashing-Methods", "Datasets", "Neural-Hashing", "Scalability"]
short_authors: Bhunia et al.
---
With the large-scale explosion of images and videos over the internet,
efficient hashing methods have been developed to facilitate memory and time
efficient retrieval of similar images. However, none of the existing works uses
hashing to address texture image retrieval mostly because of the lack of
sufficiently large texture image databases. Our work addresses this problem by
developing a novel deep learning architecture that generates binary hash codes
for input texture images. For this, we first pre-train a Texture Synthesis
Network (TSN) which takes a texture patch as input and outputs an enlarged view
of the texture by injecting newer texture content. Thus it signifies that the
TSN encodes the learnt texture specific information in its intermediate layers.
In the next stage, a second network gathers the multi-scale feature
representations from the TSN's intermediate layers using channel-wise
attention, combines them in a progressive manner to a dense continuous
representation which is finally converted into a binary hash code with the help
of individual and pairwise label information. The new enlarged texture patches
also help in data augmentation to alleviate the problem of insufficient texture
data and are used to train the second stage of the network. Experiments on
three public texture image retrieval datasets indicate the superiority of our
texture synthesis guided hashing approach over current state-of-the-art
methods.