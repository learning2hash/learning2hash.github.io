---
layout: publication
title: Sequential Dual Deep Learning With Shape And Texture Features For Sketch Recognition
authors: Qi Jia, Meiyu Yu, Xin Fan, Haojie Li
conference: Arxiv
year: 2017
bibkey: jia2017sequential
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.02716'}]
tags: []
short_authors: Jia et al.
---
Recognizing freehand sketches with high arbitrariness is greatly challenging.
Most existing methods either ignore the geometric characteristics or treat
sketches as handwritten characters with fixed structural ordering.
Consequently, they can hardly yield high recognition performance even though
sophisticated learning techniques are employed. In this paper, we propose a
sequential deep learning strategy that combines both shape and texture
features. A coded shape descriptor is exploited to characterize the geometry of
sketch strokes with high flexibility, while the outputs of constitutional
neural networks (CNN) are taken as the abstract texture feature. We develop
dual deep networks with memorable gated recurrent units (GRUs), and
sequentially feed these two types of features into the dual networks,
respectively. These dual networks enable the feature fusion by another gated
recurrent unit (GRU), and thus accurately recognize sketches invariant to
stroke ordering. The experiments on the TU-Berlin data set show that our method
outperforms the average of human and state-of-the-art algorithms even when
significant shape and appearance variations occur.