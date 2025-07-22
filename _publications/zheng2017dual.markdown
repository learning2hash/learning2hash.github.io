---
layout: publication
title: Dual-path Convolutional Image-text Embeddings With Instance Loss
authors: Zheng Zhedong, Zheng Liang, Garrett Michael, Yang Yi, Xu Mingliang, Shen
  Yi-dong
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2020
bibkey: zheng2017dual
citations: 127
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.05535'}]
tags: ["Unsupervised", "Datasets"]
short_authors: Zheng et al.
---
Matching images and sentences demands a fine understanding of both
modalities. In this paper, we propose a new system to discriminatively embed
the image and text to a shared visual-textual space. In this field, most
existing works apply the ranking loss to pull the positive image / text pairs
close and push the negative pairs apart from each other. However, directly
deploying the ranking loss is hard for network learning, since it starts from
the two heterogeneous features to build inter-modal relationship. To address
this problem, we propose the instance loss which explicitly considers the
intra-modal data distribution. It is based on an unsupervised assumption that
each image / text group can be viewed as a class. So the network can learn the
fine granularity from every image/text group. The experiment shows that the
instance loss offers better weight initialization for the ranking loss, so that
more discriminative embeddings can be learned. Besides, existing works usually
apply the off-the-shelf features, i.e., word2vec and fixed visual feature. So
in a minor contribution, this paper constructs an end-to-end dual-path
convolutional network to learn the image and text representations. End-to-end
learning allows the system to directly learn from the data and fully utilize
the supervision. On two generic retrieval datasets (Flickr30k and MSCOCO),
experiments demonstrate that our method yields competitive accuracy compared to
state-of-the-art methods. Moreover, in language based person retrieval, we
improve the state of the art by a large margin. The code has been made publicly
available.