---
layout: publication
title: Can Image-level Labels Replace Pixel-level Labels For Image Parsing
authors: Zhiwu Lu, Zhenyong Fu, Tao Xiang, Liwei Wang, Ji-Rong Wen
conference: IEEE Trans. Pattern Anal. Mach. Intell. 39(3) 486-500 (2017)
year: 2014
bibkey: lu2014can
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1403.1626'}]
tags: ["Supervised"]
short_authors: Lu et al.
---
This paper presents a weakly supervised sparse learning approach to the
problem of noisily tagged image parsing, or segmenting all the objects within a
noisily tagged image and identifying their categories (i.e. tags). Different
from the traditional image parsing that takes pixel-level labels as strong
supervisory information, our noisily tagged image parsing is provided with
noisy tags of all the images (i.e. image-level labels), which is a natural
setting for social image collections (e.g. Flickr). By oversegmenting all the
images into regions, we formulate noisily tagged image parsing as a weakly
supervised sparse learning problem over all the regions, where the initial
labels of each region are inferred from image-level labels. Furthermore, we
develop an efficient algorithm to solve such weakly supervised sparse learning
problem. The experimental results on two benchmark datasets show the
effectiveness of our approach. More notably, the reported surprising results
shed some light on answering the question: can image-level labels replace
pixel-level labels (hard to access) as supervisory information for image
parsing.