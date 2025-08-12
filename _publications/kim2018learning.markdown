---
layout: publication
title: Learning Image Representations By Completing Damaged Jigsaw Puzzles
authors: Dahun Kim, Donghyeon Cho, Donggeun Yoo, In So Kweon
conference: 2018 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2018
bibkey: kim2018learning
citations: 164
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.01880'}]
tags: ["Self-Supervised"]
short_authors: Kim et al.
---
In this paper, we explore methods of complicating self-supervised tasks for
representation learning. That is, we do severe damage to data and encourage a
network to recover them. First, we complicate each of three powerful
self-supervised task candidates: jigsaw puzzle, inpainting, and colorization.
In addition, we introduce a novel complicated self-supervised task called
"Completing damaged jigsaw puzzles" which is puzzles with one piece missing and
the other pieces without color. We train a convolutional neural network not
only to solve the puzzles, but also generate the missing content and colorize
the puzzles. The recovery of the aforementioned damage pushes the network to
obtain robust and general-purpose representations. We demonstrate that
complicating the self-supervised tasks improves their original versions and
that our final task learns more robust and transferable representations
compared to the previous methods, as well as the simple combination of our
candidate tasks. Our approach achieves state-of-the-art performance in transfer
learning on PASCAL classification and semantic segmentation.