---
layout: publication
title: 'Fast-at: Fast Automatic Thumbnail Generation Using Deep Neural Networks'
authors: Seyed A. Esmaeili, Bharat Singh, Larry S. Davis
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: esmaeili2016fast
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.04811'}]
tags: ["CVPR"]
short_authors: Seyed A. Esmaeili, Bharat Singh, Larry S. Davis
---
Fast-AT is an automatic thumbnail generation system based on deep neural
networks. It is a fully-convolutional deep neural network, which learns
specific filters for thumbnails of different sizes and aspect ratios. During
inference, the appropriate filter is selected depending on the dimensions of
the target thumbnail. Unlike most previous work, Fast-AT does not utilize
saliency but addresses the problem directly. In addition, it eliminates the
need to conduct region search on the saliency map. The model generalizes to
thumbnails of different sizes including those with extreme aspect ratios and
can generate thumbnails in real time. A data set of more than 70,000 thumbnail
annotations was collected to train Fast-AT. We show competitive results in
comparison to existing techniques.