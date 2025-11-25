---
layout: publication
title: Tevis:translating Text Synopses To Video Storyboards
authors: Xu Gu, Yuchong Sun, Feiyue Ni, Shizhe Chen, Xihua Wang, Ruihua Song, Boyuan
  Li, Xiang Cao
conference: Arxiv
year: 2022
bibkey: gu2022tevis
citations: 1
additional_links: [{name: Code, url: 'https://ruc-aimind.github.io/projects/TeViS/'},
  {name: Paper, url: 'https://arxiv.org/abs/2301.00135'}]
tags: ["Datasets", "Evaluation", "Quantization"]
short_authors: Gu et al.
---
A video storyboard is a roadmap for video creation which consists of
shot-by-shot images to visualize key plots in a text synopsis. Creating video
storyboards, however, remains challenging which not only requires cross-modal
association between high-level texts and images but also demands long-term
reasoning to make transitions smooth across shots. In this paper, we propose a
new task called Text synopsis to Video Storyboard (TeViS) which aims to
retrieve an ordered sequence of images as the video storyboard to visualize the
text synopsis. We construct a MovieNet-TeViS dataset based on the public
MovieNet dataset. It contains 10K text synopses each paired with keyframes
manually selected from corresponding movies by considering both relevance and
cinematic coherence. To benchmark the task, we present strong CLIP-based
baselines and a novel VQ-Trans. VQ-Trans first encodes text synopsis and images
into a joint embedding space and uses vector quantization (VQ) to improve the
visual representation. Then, it auto-regressively generates a sequence of
visual features for retrieval and ordering. Experimental results demonstrate
that VQ-Trans significantly outperforms prior methods and the CLIP-based
baselines. Nevertheless, there is still a large gap compared to human
performance suggesting room for promising future work. The code and data are
available at: https://ruc-aimind.github.io/projects/TeViS/