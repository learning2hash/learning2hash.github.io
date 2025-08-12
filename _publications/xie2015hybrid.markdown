---
layout: publication
title: Hybrid CNN And Dictionary-based Models For Scene Recognition And Domain Adaptation
authors: Guo-Sen Xie, Xu-Yao Zhang, Shuicheng Yan, Cheng-Lin Liu
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2015
bibkey: xie2015hybrid
citations: 169
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.07977'}]
tags: []
short_authors: Xie et al.
---
Convolutional neural network (CNN) has achieved state-of-the-art performance
in many different visual tasks. Learned from a large-scale training dataset,
CNN features are much more discriminative and accurate than the hand-crafted
features. Moreover, CNN features are also transferable among different domains.
On the other hand, traditional dictionarybased features (such as BoW and SPM)
contain much more local discriminative and structural information, which is
implicitly embedded in the images. To further improve the performance, in this
paper, we propose to combine CNN with dictionarybased models for scene
recognition and visual domain adaptation. Specifically, based on the well-tuned
CNN models (e.g., AlexNet and VGG Net), two dictionary-based representations
are further constructed, namely mid-level local representation (MLR) and
convolutional Fisher vector representation (CFV). In MLR, an efficient
two-stage clustering method, i.e., weighted spatial and feature space spectral
clustering on the parts of a single image followed by clustering all
representative parts of all images, is used to generate a class-mixture or a
classspecific part dictionary. After that, the part dictionary is used to
operate with the multi-scale image inputs for generating midlevel
representation. In CFV, a multi-scale and scale-proportional GMM training
strategy is utilized to generate Fisher vectors based on the last convolutional
layer of CNN. By integrating the complementary information of MLR, CFV and the
CNN features of the fully connected layer, the state-of-the-art performance can
be achieved on scene recognition and domain adaptation problems. An interested
finding is that our proposed hybrid representation (from VGG net trained on
ImageNet) is also complementary with GoogLeNet and/or VGG-11 (trained on
Place205) greatly.