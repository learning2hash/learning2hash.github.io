---
layout: publication
title: Natural Scene Recognition Based On Superpixels And Deep Boltzmann Machines
authors: Jinfu Yang, Jingyu Gao, Guanghui Wang, Shanshan Zhang
conference: Arxiv
year: 2015
bibkey: yang2015natural
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.07271'}]
tags: ["Unsupervised"]
short_authors: Yang et al.
---
The Deep Boltzmann Machines (DBM) is a state-of-the-art unsupervised learning
model, which has been successfully applied to handwritten digit recognition
and, as well as object recognition. However, the DBM is limited in scene
recognition due to the fact that natural scene images are usually very large.
In this paper, an efficient scene recognition approach is proposed based on
superpixels and the DBMs. First, a simple linear iterative clustering (SLIC)
algorithm is employed to generate superpixels of input images, where each
superpixel is regarded as an input of a learning model. Then, a two-layer DBM
model is constructed by stacking two restricted Boltzmann machines (RBMs), and
a greedy layer-wise algorithm is applied to train the DBM model. Finally, a
softmax regression is utilized to categorize scene images. The proposed
technique can effectively reduce the computational complexity and enhance the
performance for large natural image recognition. The approach is verified and
evaluated by extensive experiments, including the fifteen-scene categories
dataset the UIUC eight-sports dataset, and the SIFT flow dataset, are used to
evaluate the proposed method. The experimental results show that the proposed
approach outperforms other state-of-the-art methods in terms of recognition
rate.