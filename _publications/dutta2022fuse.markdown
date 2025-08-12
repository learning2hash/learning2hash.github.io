---
layout: publication
title: 'Fuse And Attend: Generalized Embedding Learning For Art And Sketches'
authors: Ujjal Kr Dutta
conference: Lecture Notes in Computer Science
year: 2023
bibkey: dutta2022fuse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.09698'}]
tags: []
short_authors: Ujjal Kr Dutta
---
While deep Embedding Learning approaches have witnessed widespread success in
multiple computer vision tasks, the state-of-the-art methods for representing
natural images need not necessarily perform well on images from other domains,
such as paintings, cartoons, and sketch. This is because of the huge shift in
the distribution of data from across these domains, as compared to natural
images. Domains like sketch often contain sparse informative pixels. However,
recognizing objects in such domains is crucial, given multiple relevant
applications leveraging such data, for instance, sketch to image retrieval.
Thus, achieving an Embedding Learning model that could perform well across
multiple domains is not only challenging, but plays a pivotal role in computer
vision. To this end, in this paper, we propose a novel Embedding Learning
approach with the goal of generalizing across different domains. During
training, given a query image from a domain, we employ gated fusion and
attention to generate a positive example, which carries a broad notion of the
semantics of the query object category (from across multiple domains). By
virtue of Contrastive Learning, we pull the embeddings of the query and
positive, in order to learn a representation which is robust across domains. At
the same time, to teach the model to be discriminative against examples from
different semantic categories (across domains), we also maintain a pool of
negative embeddings (from different categories). We show the prowess of our
method using the DomainBed framework, on the popular PACS (Photo, Art painting,
Cartoon, and Sketch) dataset.