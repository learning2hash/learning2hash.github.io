---
layout: publication
title: A Content-driven Micro-video Recommendation Dataset At Scale
authors: Yongxin Ni, Yu Cheng, Xiangyan Liu, Junchen Fu, Youhua Li, Xiangnan He, Yongfeng
  Zhang, Fajie Yuan
conference: Arxiv
year: 2023
bibkey: ni2023content
citations: 3
additional_links: [{name: Code, url: 'https://github.com/westlake-repl/MicroLens'},
  {name: Paper, url: 'https://arxiv.org/abs/2309.15379'}]
tags: ["Datasets", "Recommender Systems", "Scalability"]
short_authors: Ni et al.
---
Micro-videos have recently gained immense popularity, sparking critical
research in micro-video recommendation with significant implications for the
entertainment, advertising, and e-commerce industries. However, the lack of
large-scale public micro-video datasets poses a major challenge for developing
effective recommender systems. To address this challenge, we introduce a very
large micro-video recommendation dataset, named "MicroLens", consisting of one
billion user-item interaction behaviors, 34 million users, and one million
micro-videos. This dataset also contains various raw modality information about
videos, including titles, cover images, audio, and full-length videos.
MicroLens serves as a benchmark for content-driven micro-video recommendation,
enabling researchers to utilize various modalities of video information for
recommendation, rather than relying solely on item IDs or off-the-shelf video
features extracted from a pre-trained network. Our benchmarking of multiple
recommender models and video encoders on MicroLens has yielded valuable
insights into the performance of micro-video recommendation. We believe that
this dataset will not only benefit the recommender system community but also
promote the development of the video understanding field. Our datasets and code
are available at https://github.com/westlake-repl/MicroLens.