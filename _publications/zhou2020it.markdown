---
layout: publication
title: 'It''s The Best Only When It Fits You Most: Finding Related Models For Serving
  Based On Dynamic Locality Sensitive Hashing'
authors: Lixi Zhou, Zijie Wang, Amitabh Das, Jia Zou
conference: Arxiv
year: 2020
bibkey: zhou2020it
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.09474'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Locality Sensitive Hashing"]
short_authors: Zhou et al.
---
In recent, deep learning has become the most popular direction in machine
learning and artificial intelligence. However, preparation of training data is
often a bottleneck in the lifecycle of deploying a deep learning model for
production or research. Reusing models for inferencing a dataset can greatly
save the human costs required for training data creation. Although there exist
a number of model sharing platform such as TensorFlow Hub, PyTorch Hub, DLHub,
most of these systems require model uploaders to manually specify the details
of each model and model downloaders to screen keyword search results for
selecting a model. They are in lack of an automatic model searching tool. This
paper proposes an end-to-end process of searching related models for serving
based on the similarity of the target dataset and the training datasets of the
available models. While there exist many similarity measurements, we study how
to efficiently apply these metrics without pair-wise comparison and compare the
effectiveness of these metrics. We find that our proposed adaptivity
measurement which is based on Jensen-Shannon (JS) divergence, is an effective
measurement, and its computation can be significantly accelerated by using the
technique of locality sensitive hashing.