---
layout: publication
title: Asymmetric Scalable Cross45;modal Hashing
authors: Li Wenyun, Pun Chi-man
conference: "Arxiv"
year: 2022
bibkey: li2022asymmetric
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2207.12650"}
tags: ['ARXIV', 'Independent']
---
Cross45;modal hashing is a successful method to solve large45;scale multimedia retrieval issue. A lot of matrix factorization45;based hashing methods are proposed. However the existing methods still struggle with a few problems such as how to generate the binary codes efficiently rather than directly relax them to continuity. In addition most of the existing methods choose to use an n× n similarity matrix for optimization which makes the memory and computation unaffordable. In this paper we propose a novel Asymmetric Scalable Cross45;Modal Hashing (ASCMH) to address these issues. It firstly introduces a collective matrix factorization to learn a common latent space from the kernelized features of different modalities and then transforms the similarity matrix optimization to a distance45;distance difference problem minimization with the help of semantic labels and common latent space. Hence the computational complexity of the n× n asymmetric optimization is relieved. In the generation of hash codes we also employ an orthogonal constraint of label information which is indispensable for search accuracy. So the redundancy of computation can be much reduced. For efficient optimization and scalable to large45;scale datasets we adopt the two45;step approach rather than optimizing simultaneously. Extensive experiments on three benchmark datasets Wiki MIRFlickr45;25K and NUS45;WIDE demonstrate that our ASCMH outperforms the state45;of45;the45;art cross45;modal hashing methods in terms of accuracy and efficiency.
