---
layout: publication
title: Deep Asymmetric Hashing With Dual Semantic Regression And Class Structure Quantization
authors: Jianglin Lu, Hailing Wang, Jie Zhou, Mengfan Yan, Jiajun Wen
conference: Arxiv
year: 2021
citations: 2
bibkey: lu2021deep
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.12478'}]
tags: [Deep Hashing, Quantization, ANN Search, Hashing Methods, Applications, Loss
    Functions]
---
Recently, deep hashing methods have been widely used in image retrieval task.
Most existing deep hashing approaches adopt one-to-one quantization to reduce
information loss. However, such class-unrelated quantization cannot give
discriminative feedback for network training. In addition, these methods only
utilize single label to integrate supervision information of data for hashing
function learning, which may result in inferior network generalization
performance and relatively low-quality hash codes since the inter-class
information of data is totally ignored. In this paper, we propose a dual
semantic asymmetric hashing (DSAH) method, which generates discriminative hash
codes under three-fold constraints. Firstly, DSAH utilizes class prior to
conduct class structure quantization so as to transmit class information during
the quantization process. Secondly, a simple yet effective label mechanism is
designed to characterize both the intra-class compactness and inter-class
separability of data, thereby achieving semantic-sensitive binary code
learning. Finally, a meaningful pairwise similarity preserving loss is devised
to minimize the distances between class-related network outputs based on an
affinity graph. With these three main components, high-quality hash codes can
be generated through network. Extensive experiments conducted on various
datasets demonstrate the superiority of DSAH in comparison with
state-of-the-art deep hashing methods.