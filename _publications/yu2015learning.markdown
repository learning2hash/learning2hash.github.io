---
layout: publication
title: Learning cross space mapping via DNN using large scale click-through logs
authors: Yu et al.
conference: IEEE Transactions on Multimedia
year: 2015
bibkey: yu2015learning
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.13275'}]
tags: ["Evaluation"]
---
The gap between low-level visual signals and high-level semantics has been
progressively bridged by continuous development of deep neural network (DNN).
With recent progress of DNN, almost all image classification tasks have
achieved new records of accuracy. To extend the ability of DNN to image
retrieval tasks, we proposed a unified DNN model for image-query similarity
calculation by simultaneously modeling image and query in one network. The
unified DNN is named the cross space mapping (CSM) model, which contains two
parts, a convolutional part and a query-embedding part. The image and query are
mapped to a common vector space via these two parts respectively, and
image-query similarity is naturally defined as an inner product of their
mappings in the space. To ensure good generalization ability of the DNN, we
learn weights of the DNN from a large number of click-through logs which
consists of 23 million clicked image-query pairs between 1 million images and
11.7 million queries. Both the qualitative results and quantitative results on
an image retrieval evaluation task with 1000 queries demonstrate the
superiority of the proposed method.