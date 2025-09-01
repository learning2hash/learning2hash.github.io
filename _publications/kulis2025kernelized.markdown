---
layout: publication
title: Kernelized Locality-sensitive Hashing For Scalable Image Search
authors: B. Kulis, Grauman
conference: 2009 IEEE 12th International Conference on Computer Vision
year: 2009
bibkey: kulis2025kernelized
citations: 910
additional_links: [{name: Paper, url: 'https://www.robots.ox.ac.uk/~vgg/rg/papers/klsh.pdf'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Hashing Methods", "ICCV", "Image Retrieval", "Scalability"]
short_authors: B. Kulis, Grauman
---
Fast retrieval methods are critical for large-scale and
data-driven vision applications. Recent work has explored
ways to embed high-dimensional features or complex distance
functions into a low-dimensional Hamming space
where items can be efficiently searched. However, existing
methods do not apply for high-dimensional kernelized
data when the underlying feature embedding for the kernel
is unknown. We show how to generalize locality-sensitive
hashing to accommodate arbitrary kernel functions, making
it possible to preserve the algorithm’s sub-linear time similarity
search guarantees for a wide class of useful similarity
functions. Since a number of successful image-based kernels
have unknown or incomputable embeddings, this is especially
valuable for image retrieval tasks. We validate our
technique on several large-scale datasets, and show that it
enables accurate and fast performance for example-based
object classification, feature matching, and content-based
retrieval.