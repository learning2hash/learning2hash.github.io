---
layout: publication
title: Dynamic Spatial Verification For Large-scale Object-level Image Retrieval
authors: Joel Brogan, Aparna Bharati, Daniel Moreira, Kevin Bowyer, Patrick Flynn,
  Anderson Rocha, Walter Scheirer
conference: Arxiv
year: 2019
bibkey: brogan2019dynamic
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.10019'}]
tags: ["Image Retrieval", "Scalability"]
short_authors: Brogan et al.
---
Images from social media can reflect diverse viewpoints, heated arguments,
and expressions of creativity, adding new complexity to retrieval tasks.
Researchers working onContent-Based Image Retrieval (CBIR) have traditionally
tuned their algorithms to match filtered results with user search intent.
However, we are now bombarded with composite images of unknown origin,
authenticity, and even meaning. With such uncertainty, users may not have an
initial idea of what the results of a search query should look like. For
instance, hidden people, spliced objects, and subtly altered scenes can be
difficult for a user to detect initially in a meme image, but may contribute
significantly to its composition. We propose a new approach for spatial
verification that aims at modeling object-level regions dynamically clustering
keypoints in a 2D Hough space, which are then used to accurately weight small
contributing objects within the results, without the need for costly object
detection steps. We call this method Objects in Scene to Objects in Scene
(OS2OS) score, and it is optimized for fast matrix operations on CPUs. OS2OS
performs comparably to state-of-the-art methods in classic CBIR problems, on
the Oxford5K, Paris 6K, and Google-Landmarks datasets, without the need for
bounding boxes. It also succeeds in emerging retrieval tasks such as image
composite matching in the NIST MFC2018 dataset and meme-style composite imagery
fromReddit.