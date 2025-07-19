---
layout: publication
title: Accurate and Efficient Similarity Search for Large Scale Face Recognition
authors: Qi Ce, Liu Zhizhong, Su Fei
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2018
bibkey: qi2018accurate
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.00365'}]
tags: [CVPR, Similarity Search]
---
Face verification is a relatively easy task with the help of discriminative
features from deep neural networks. However, it is still a challenge to
recognize faces on millions of identities while keeping high performance and
efficiency. The challenge 2 of MS-Celeb-1M is a classification task. However,
the number of identities is too large and it is not that elegant to treat the
task as an image classification task. We treat the classification task as
similarity search and do experiments on different similarity search strategies.
Similarity search strategy accelerates the speed of searching and boosts the
accuracy of final results. The model used for extracting features is a single
deep neural network pretrained on CASIA-Webface, which is not trained on the
base set or novel set offered by official. Finally, we rank \textbf\{3rd\}, while
the speed of searching is 1ms/image.