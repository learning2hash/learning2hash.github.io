---
layout: publication
title: Fine-grained Apparel Classification And Retrieval Without Rich Annotations
authors: Bhatnagar Aniket, Aggarwal Sanchit
conference: Arxiv
year: 2018
bibkey: bhatnagar2018fine
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.02385'}]
tags: ["Tools-&-Libraries", "Distance-Metric-Learning", "Datasets"]
short_authors: Bhatnagar Aniket, Aggarwal Sanchit
---
The ability to correctly classify and retrieve apparel images has a variety
of applications important to e-commerce, online advertising and internet
search. In this work, we propose a robust framework for fine-grained apparel
classification, in-shop and cross-domain retrieval which eliminates the
requirement of rich annotations like bounding boxes and human-joints or
clothing landmarks, and training of bounding box/ key-landmark detector for the
same. Factors such as subtle appearance differences, variations in human poses,
different shooting angles, apparel deformations, and self-occlusion add to the
challenges in classification and retrieval of apparel items. Cross-domain
retrieval is even harder due to the presence of large variation between online
shopping images, usually taken in ideal lighting, pose, positive angle and
clean background as compared with street photos captured by users in
complicated conditions with poor lighting and cluttered scenes. Our framework
uses compact bilinear CNN with tensor sketch algorithm to generate embeddings
that capture local pairwise feature interactions in a translationally invariant
manner. For apparel classification, we pass the feature embeddings through a
softmax classifier, while, the in-shop and cross-domain retrieval pipelines use
a triplet-loss based optimization approach, such that squared Euclidean
distance between embeddings measures the dissimilarity between the images.
Unlike previous works that relied on bounding box, key clothing landmarks or
human joint detectors to assist the final deep classifier, proposed framework
can be trained directly on the provided category labels or generated triplets
for triplet loss optimization. Lastly, Experimental results on the DeepFashion
fine-grained categorization, and in-shop and consumer-to-shop retrieval
datasets provide a comparative analysis with previous work performed in the
domain.