---
layout: publication
title: Exploring Nearest Neighbor Approaches For Image Captioning
authors: Jacob Devlin, Saurabh Gupta, Ross Girshick, Margaret Mitchell, C. Lawrence
  Zitnick
conference: Arxiv
year: 2015
bibkey: devlin2015exploring
citations: 158
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.04467'}]
tags: [Evaluation]
short_authors: Devlin et al.
---
We explore a variety of nearest neighbor baseline approaches for image
captioning. These approaches find a set of nearest neighbor images in the
training set from which a caption may be borrowed for the query image. We
select a caption for the query image by finding the caption that best
represents the "consensus" of the set of candidate captions gathered from the
nearest neighbor images. When measured by automatic evaluation metrics on the
MS COCO caption evaluation server, these approaches perform as well as many
recent approaches that generate novel captions. However, human studies show
that a method that generates novel captions is still preferred over the nearest
neighbor approach.