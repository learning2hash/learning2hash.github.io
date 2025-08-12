---
layout: publication
title: An End-to-end Solution For Effectively Demoting Watermarked Images In Image
  Search
authors: Ning Ma, Xin Zhao, Mark Bolin
conference: Arxiv
year: 2019
bibkey: ma2019end
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.09473'}]
tags: ["Image Retrieval"]
short_authors: Ning Ma, Xin Zhao, Mark Bolin
---
We propose an end-to-end solution, from watermark feature generation to
metric design, for effectively demoting watermarked images surfed by a real
world image search engine. We use a few fundamental techniques to obtain
effective watermark features of images in the image search index, and utilize
the signals in a commercial search engine to improve the image search quality.
We collect a diverse and large set (about 1M) of images with human labels
indicating whether the image contains visible watermark. We train a few deep
convolutional neural networks to extract watermark information from the raw
images. The deep CNN classifiers we trained can achieve high accuracy on the
watermark test data set. We also analyze the images based on their domains to
get watermark information from a domain-based watermark classifier. We design a
new novel hybrid metric which includes the relevance, image attractiveness and
watermark information all together. We demonstrate that using these watermark
signals together with the new metric in image search ranker can significantly
demote the watermarked images during the online image ranking.