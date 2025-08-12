---
layout: publication
title: A New Dataset And Comparative Study For Aphid Cluster Detection
authors: Tianxiao Zhang, Kaidong Li, Xiangyu Chen, Cuncong Zhong, Bo Luo, Ivan Grijalva
  Teran, Brian McCornack, Daniel Flippo, Ajay Sharda, Guanghui Wang
conference: Arxiv
year: 2023
bibkey: zhang2023new
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.05929'}]
tags: ["Datasets", "Evaluation"]
short_authors: Zhang et al.
---
Aphids are one of the main threats to crops, rural families, and global food
security. Chemical pest control is a necessary component of crop production for
maximizing yields, however, it is unnecessary to apply the chemical approaches
to the entire fields in consideration of the environmental pollution and the
cost. Thus, accurately localizing the aphid and estimating the infestation
level is crucial to the precise local application of pesticides. Aphid
detection is very challenging as each individual aphid is really small and all
aphids are crowded together as clusters. In this paper, we propose to estimate
the infection level by detecting aphid clusters. We have taken millions of
images in the sorghum fields, manually selected 5,447 images that contain
aphids, and annotated each aphid cluster in the image. To use these images for
machine learning models, we crop the images into patches and created a labeled
dataset with over 151,000 image patches. Then, we implement and compare the
performance of four state-of-the-art object detection models.