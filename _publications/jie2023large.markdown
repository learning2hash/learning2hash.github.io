---
layout: publication
title: A Large-scale Car Parts (LSCP) Dataset For Lightweight Fine-grained Detection
authors: Wang Jie, Zhong Yilin, Cao Qianqian
conference: Arxiv
year: 2023
bibkey: jie2023large
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.11754'}]
tags: ["Datasets"]
short_authors: Wang Jie, Zhong Yilin, Cao Qianqian
---
Automotive related datasets have previously been used for training autonomous
driving systems or vehicle classification tasks. However, there is a lack of
datasets in the field of automotive AI for car parts detection, and most
available datasets are limited in size and scope, struggling to cover diverse
scenarios. To address this gap, this paper presents a large-scale and
fine-grained automotive dataset consisting of 84,162 images for detecting 12
different types of car parts. This dataset was collected from natural cameras
and online websites which covers various car brands, scenarios, and shooting
angles. To alleviate the burden of manual annotation, we propose a novel
semi-supervised auto-labeling method that leverages state-of-the-art
pre-trained detectors. Moreover, we study the limitations of the Grounding DINO
approach for zero-shot labeling. Finally, we evaluate the effectiveness of our
proposed dataset through fine-grained car parts detection by training several
lightweight YOLO-series detectors.