---
layout: publication
title: Deep Supervised Hashing With Anchor Graph
authors: Chen Yudong, Lai, Ding, Lin, Wong
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: chen2018deep
citations: 60
additional_links: [{name: Paper, url: 'http://openaccess.thecvf.com/content_ICCV_2019/papers/Chen_Deep_Supervised_Hashing_With_Anchor_Graph_ICCV_2019_paper.pdf'}]
tags: ["Hashing-Methods", "Neural-Hashing", "Compact-Codes", "CVPR", "Scalability", "Datasets", "Supervised", "Evaluation"]
short_authors: Chen et al.
---
Recently, a series of deep supervised hashing methods were proposed for binary code learning. However, due to the high computation cost and the limited hardware's memory, these methods will first select a subset from the training set, and then form a mini-batch data to update the network in each iteration. Therefore, the remaining labeled data cannot be fully utilized and the model cannot directly obtain the binary codes of the entire training set for retrieval. To address these problems, this paper proposes an interesting regularized deep model to seamlessly integrate the advantages of deep hashing and efficient binary code learning by using the anchor graph. As such, the deep features and label matrix can be jointly used to optimize the binary codes, and the network can obtain more discriminative feedback from the linear combinations of the learned bits. Moreover, we also reveal the algorithm mechanism and its computation essence. Experiments on three large-scale datasets indicate that the proposed method achieves better retrieval performance with less training time compared to previous deep hashing methods.