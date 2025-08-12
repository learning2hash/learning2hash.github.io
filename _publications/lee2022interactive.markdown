---
layout: publication
title: Interactive Multi-class Tiny-object Detection
authors: "Chunggi Lee, Seonwook Park, Heon Song, Jeongun Ryu, Sanghoon Kim, Haejoon\
  \ Kim, S\xE9rgio Pereira, Donggeun Yoo"
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: lee2022interactive
citations: 16
additional_links: [{name: Code, url: 'https://github.com/ChungYi347/Interactive-Multi-Class-Tiny-Object-Detection'},
  {name: Paper, url: 'https://arxiv.org/abs/2203.15266'}]
tags: ["CVPR"]
short_authors: Lee et al.
---
Annotating tens or hundreds of tiny objects in a given image is laborious yet
crucial for a multitude of Computer Vision tasks. Such imagery typically
contains objects from various categories, yet the multi-class interactive
annotation setting for the detection task has thus far been unexplored. To
address these needs, we propose a novel interactive annotation method for
multiple instances of tiny objects from multiple classes, based on a few
point-based user inputs. Our approach, C3Det, relates the full image context
with annotator inputs in a local and global manner via late-fusion and
feature-correlation, respectively. We perform experiments on the Tiny-DOTA and
LCell datasets using both two-stage and one-stage object detection
architectures to verify the efficacy of our approach. Our approach outperforms
existing approaches in interactive annotation, achieving higher mAP with fewer
clicks. Furthermore, we validate the annotation efficiency of our approach in a
user study where it is shown to be 2.85x faster and yield only 0.36x task load
(NASA-TLX, lower is better) compared to manual annotation. The code is
available at
https://github.com/ChungYi347/Interactive-Multi-Class-Tiny-Object-Detection.