---
layout: publication
title: 'PDH : Probabilistic Deep Hashing Based On MAP Estimation Of Hamming Distance'
authors: Yosuke Kaga, Masakazu Fujio, Kenta Takahashi, Tetsushi Ohki, Masakatsu Nishigaki
conference: 2019 26th IEEE International Conference on Image Processing (ICIP)
year: 2019
bibkey: kaga2019pdh
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.08501'}]
tags: ["Hashing Methods", "Image Retrieval", "Neural Hashing"]
short_authors: Kaga et al.
---
With the growth of image on the web, research on hashing which enables
high-speed image retrieval has been actively studied. In recent years, various
hashing methods based on deep neural networks have been proposed and achieved
higher precision than the other hashing methods. In these methods, multiple
losses for hash codes and the parameters of neural networks are defined. They
generate hash codes that minimize the weighted sum of the losses. Therefore, an
expert has to tune the weights for the losses heuristically, and the
probabilistic optimality of the loss function cannot be explained. In order to
generate explainable hash codes without weight tuning, we theoretically derive
a single loss function with no hyperparameters for the hash code from the
probability distribution of the images. By generating hash codes that minimize
this loss function, highly accurate image retrieval with probabilistic
optimality is performed. We evaluate the performance of hashing using MNIST,
CIFAR-10, SVHN and show that the proposed method outperforms the
state-of-the-art hashing methods.