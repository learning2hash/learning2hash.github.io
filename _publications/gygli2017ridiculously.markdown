---
layout: publication
title: Ridiculously Fast Shot Boundary Detection With Fully Convolutional Neural Networks
authors: Michael Gygli
conference: 2018 International Conference on Content-Based Multimedia Indexing (CBMI)
year: 2018
bibkey: gygli2017ridiculously
citations: 79
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.08214'}]
tags: ["Efficiency"]
short_authors: Michael Gygli
---
Shot boundary detection (SBD) is an important component of many video
analysis tasks, such as action recognition, video indexing, summarization and
editing. Previous work typically used a combination of low-level features like
color histograms, in conjunction with simple models such as SVMs. Instead, we
propose to learn shot detection end-to-end, from pixels to final shot
boundaries. For training such a model, we rely on our insight that all shot
boundaries are generated. Thus, we create a dataset with one million frames and
automatically generated transitions such as cuts, dissolves and fades. In order
to efficiently analyze hours of videos, we propose a Convolutional Neural
Network (CNN) which is fully convolutional in time, thus allowing to use a
large temporal context without the need to repeatedly processing frames. With
this architecture our method obtains state-of-the-art results while running at
an unprecedented speed of more than 120x real-time.