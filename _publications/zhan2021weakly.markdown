---
layout: publication
title: Weakly-Supervised Online Hashing
authors: Zhan et al.
conference: 2021 IEEE International Conference on Multimedia and Expo (ICME)
year: 2021
bibkey: zhan2021weakly
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.07436'}]
tags: ["Hashing Methods", "Supervised"]
---
With the rapid development of social websites, recent years have witnessed an
explosive growth of social images with user-provided tags which continuously
arrive in a streaming fashion. Due to the fast query speed and low storage
cost, hashing-based methods for image search have attracted increasing
attention. However, existing hashing methods for social image retrieval are
based on batch mode which violates the nature of social images, i.e., social
images are usually generated periodically or collected in a stream fashion.
Although there exist many online image hashing methods, they either adopt
unsupervised learning which ignore the relevant tags, or are designed in the
supervised manner which needs high-quality labels. In this paper, to overcome
the above limitations, we propose a new method named Weakly-supervised Online
Hashing (WOH). In order to learn high-quality hash codes, WOH exploits the weak
supervision by considering the semantics of tags and removing the noise.
Besides, We develop a discrete online optimization algorithm for WOH, which is
efficient and scalable. Extensive experiments conducted on two real-world
datasets demonstrate the superiority of WOH compared with several
state-of-the-art hashing baselines.