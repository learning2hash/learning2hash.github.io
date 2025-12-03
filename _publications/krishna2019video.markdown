---
layout: publication
title: Video Segment Copy Detection Using Memory Constrained Hierarchical Batch-normalized
  LSTM Autoencoder
authors: Arjun Krishna, A S Akil Arif Ibrahim
conference: Arxiv
year: 2019
bibkey: krishna2019video
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.09518'}]
tags: ["Datasets", "Hashing Methods", "Image Retrieval", "Neural Hashing"]
short_authors: Arjun Krishna, A S Akil Arif Ibrahim
---
In this report, we introduce a video hashing method for scalable video
segment copy detection. The objective of video segment copy detection is to
find the video (s) present in a large database, one of whose segments (cropped
in time) is a (transformed) copy of the given query video. This transformation
may be temporal (for example frame dropping, change in frame rate) or spatial
(brightness and contrast change, addition of noise etc.) in nature although the
primary focus of this report is detecting temporal attacks. The video hashing
method proposed by us uses a deep learning neural network to learn variable
length binary hash codes for the entire video considering both temporal and
spatial features into account. This is in contrast to most existing video
hashing methods, as they use conventional image hashing techniques to obtain
hash codes for a video after extracting features for every frame or certain key
frames, in which case the temporal information present in the video is not
exploited. Our hashing method is specifically resilient to time cropping making
it extremely useful in video segment copy detection. Experimental results
obtained on the large augmented dataset consisting of around 25,000 videos with
segment copies demonstrate the efficacy of our proposed video hashing method.