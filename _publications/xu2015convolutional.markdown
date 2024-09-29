---
layout: publication
title: "Convolutional Neural Networks for Text Hashing"
authors:  Jiaming Xu, PengWang, Guanhua Tian, Bo Xu, Jun Zhao, Fangyuan Wang, Hongwei Hao
conference: IJCAI
year: 2015
bibkey: xu2015convolutional
additional_links:
   - {name: "PDF", url: "http://ijcai.org/papers15/Papers/IJCAI15-197.pdf"}
---
Hashing, as a popular approximate nearest neighbor
search, has been widely used for large-scale similarity search. Recently, a spectrum of machine learning
methods are utilized to learn similarity-preserving
binary codes. However, most of them directly encode the explicit features, keywords, which fail to
preserve the accurate semantic similarities in binary code beyond keyword matching, especially on
short texts. Here we propose a novel text hashing
framework with convolutional neural networks. In
particular, we first embed the keyword features into
compact binary code with a locality preserving constraint. Meanwhile word features and position features are together fed into a convolutional network to
learn the implicit features which are further incorporated with the explicit features to fit the pre-trained
binary code. Such base method can be successfully
accomplished without any external tags/labels, and
other three model variations are designed to integrate tags/labels. Experimental results show the
superiority of our proposed approach over several
state-of-the-art hashing methods when tested on one
short text dataset as well as one normal text dataset.
