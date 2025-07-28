---
layout: publication
title: Personalized Classifier For Food Image Recognition
authors: Shota Horiguchi, Sosuke Amano, Makoto Ogawa, Kiyoharu Aizawa
conference: IEEE Transactions on Multimedia
year: 2018
bibkey: horiguchi2018personalized
citations: 88
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.04600'}]
tags: []
short_authors: Horiguchi et al.
---
Currently, food image recognition tasks are evaluated against fixed datasets.
However, in real-world conditions, there are cases in which the number of
samples in each class continues to increase and samples from novel classes
appear. In particular, dynamic datasets in which each individual user creates
samples and continues the updating process often have content that varies
considerably between different users, and the number of samples per person is
very limited. A single classifier common to all users cannot handle such
dynamic data. Bridging the gap between the laboratory environment and the real
world has not yet been accomplished on a large scale. Personalizing a
classifier incrementally for each user is a promising way to do this. In this
paper, we address the personalization problem, which involves adapting to the
user's domain incrementally using a very limited number of samples. We propose
a simple yet effective personalization framework which is a combination of the
nearest class mean classifier and the 1-nearest neighbor classifier based on
deep features. To conduct realistic experiments, we made use of a new dataset
of daily food images collected by a food-logging application. Experimental
results show that our proposed method significantly outperforms existing
methods.