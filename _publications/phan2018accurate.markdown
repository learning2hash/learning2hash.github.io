---
layout: publication
title: Accurate And Scalable Image Clustering Based On Sparse Representation Of Camera
  Fingerprint
authors: Quoc-Tin Phan, Giulia Boato, Francesco G. B. de Natale
conference: IEEE Transactions on Information Forensics and Security
year: 2018
bibkey: phan2018accurate
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.07945'}]
tags: ["Scalability"]
short_authors: Quoc-Tin Phan, Giulia Boato, Francesco G. B. de Natale
---
Clustering images according to their acquisition devices is a well-known
problem in multimedia forensics, which is typically faced by means of camera
Sensor Pattern Noise (SPN). Such an issue is challenging since SPN is a
noise-like signal, hard to be estimated and easy to be attenuated or destroyed
by many factors. Moreover, the high dimensionality of SPN hinders large-scale
applications. Existing approaches are typically based on the correlation among
SPNs in the pixel domain, which might not be able to capture intrinsic data
structure in union of vector subspaces. In this paper, we propose an accurate
clustering framework, which exploits linear dependencies among SPNs in their
intrinsic vector subspaces. Such dependencies are encoded under sparse
representations which are obtained by solving a LASSO problem with
non-negativity constraint. The proposed framework is highly accurate in number
of clusters estimation and image association. Moreover, our framework is
scalable to the number of images and robust against double JPEG compression as
well as the presence of outliers, owning big potential for real-world
applications. Experimental results on Dresden and Vision database show that our
proposed framework can adapt well to both medium-scale and large-scale
contexts, and outperforms state-of-the-art methods.