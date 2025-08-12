---
layout: publication
title: Detecting And Grouping Identical Objects For Region Proposal And Classification
authors: Wim Abbeloos, Sergio Caccamo, Esra Ataer-Cansizoglu, Yuichi Taguchi, Chen
  Feng, Teng-Yok Lee
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2017
bibkey: abbeloos2017detecting
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.07255'}]
tags: ["CVPR"]
short_authors: Abbeloos et al.
---
Often multiple instances of an object occur in the same scene, for example in
a warehouse. Unsupervised multi-instance object discovery algorithms are able
to detect and identify such objects. We use such an algorithm to provide object
proposals to a convolutional neural network (CNN) based classifier. This
results in fewer regions to evaluate, compared to traditional region proposal
algorithms. Additionally, it enables using the joint probability of multiple
instances of an object, resulting in improved classification accuracy. The
proposed technique can also split a single class into multiple sub-classes
corresponding to the different object types, enabling hierarchical
classification.