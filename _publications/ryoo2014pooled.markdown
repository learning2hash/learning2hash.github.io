---
layout: publication
title: Pooled Motion Features For First-person Videos
authors: M. S. Ryoo, Brandon Rothrock, Larry Matthies
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2015
bibkey: ryoo2014pooled
citations: 164
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.6505'}]
tags: ["CVPR"]
short_authors: M. S. Ryoo, Brandon Rothrock, Larry Matthies
---
In this paper, we present a new feature representation for first-person
videos. In first-person video understanding (e.g., activity recognition), it is
very important to capture both entire scene dynamics (i.e., egomotion) and
salient local motion observed in videos. We describe a representation framework
based on time series pooling, which is designed to abstract
short-term/long-term changes in feature descriptor elements. The idea is to
keep track of how descriptor values are changing over time and summarize them
to represent motion in the activity video. The framework is general, handling
any types of per-frame feature descriptors including conventional motion
descriptors like histogram of optical flows (HOF) as well as appearance
descriptors from more recent convolutional neural networks (CNN). We
experimentally confirm that our approach clearly outperforms previous feature
representations including bag-of-visual-words and improved Fisher vector (IFV)
when using identical underlying feature descriptors. We also confirm that our
feature representation has superior performance to existing state-of-the-art
features like local spatio-temporal features and Improved Trajectory Features
(originally developed for 3rd-person videos) when handling first-person videos.
Multiple first-person activity datasets were tested under various settings to
confirm these findings.