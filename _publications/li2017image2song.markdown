---
layout: publication
title: 'Image2song: Song Retrieval Via Bridging Image Content And Lyric Words'
authors: Xuelong Li, di Hu, Xiaoqiang Lu
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: li2017image2song
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.05851'}]
tags: ["Datasets", "ICCV", "Tools & Libraries"]
short_authors: Xuelong Li, di Hu, Xiaoqiang Lu
---
Image is usually taken for expressing some kinds of emotions or purposes,
such as love, celebrating Christmas. There is another better way that combines
the image and relevant song to amplify the expression, which has drawn much
attention in the social network recently. Hence, the automatic selection of
songs should be expected. In this paper, we propose to retrieve semantic
relevant songs just by an image query, which is named as the image2song
problem. Motivated by the requirements of establishing correlation in
semantic/content, we build a semantic-based song retrieval framework, which
learns the correlation between image content and lyric words. This model uses a
convolutional neural network to generate rich tags from image regions, a
recurrent neural network to model lyric, and then establishes correlation via a
multi-layer perceptron. To reduce the content gap between image and lyric, we
propose to make the lyric modeling focus on the main image content via a tag
attention. We collect a dataset from the social-sharing multimodal data to
study the proposed problem, which consists of (image, music clip, lyric)
triplets. We demonstrate that our proposed model shows noticeable results in
the image2song retrieval task and provides suitable songs. Besides, the
song2image task is also performed.