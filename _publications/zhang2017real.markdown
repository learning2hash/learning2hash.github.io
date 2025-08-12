---
layout: publication
title: Real-time User-guided Image Colorization With Learned Deep Priors
authors: Richard Zhang, Jun-Yan Zhu, Phillip Isola, Xinyang Geng, Angela S. Lin, Tianhe
  Yu, Alexei A. Efros
conference: ACM Transactions on Graphics
year: 2017
bibkey: zhang2017real
citations: 518
additional_links: [{name: Code, url: 'https://richzhang.github.io/ideepcolor'}, {
    name: Paper, url: 'https://arxiv.org/abs/1705.02999'}]
tags: []
short_authors: Zhang et al.
---
We propose a deep learning approach for user-guided image colorization. The
system directly maps a grayscale image, along with sparse, local user "hints"
to an output colorization with a Convolutional Neural Network (CNN). Rather
than using hand-defined rules, the network propagates user edits by fusing
low-level cues along with high-level semantic information, learned from
large-scale data. We train on a million images, with simulated user inputs. To
guide the user towards efficient input selection, the system recommends likely
colors based on the input image and current user inputs. The colorization is
performed in a single feed-forward pass, enabling real-time use. Even with
randomly simulated user inputs, we show that the proposed system helps novice
users quickly create realistic colorizations, and offers large improvements in
colorization quality with just a minute of use. In addition, we demonstrate
that the framework can incorporate other user "hints" to the desired
colorization, showing an application to color histogram transfer. Our code and
models are available at https://richzhang.github.io/ideepcolor.