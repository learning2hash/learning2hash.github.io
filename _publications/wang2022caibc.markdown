---
layout: publication
title: 'CAIBC: Capturing All-round Information Beyond Color For Text-based Person
  Retrieval'
authors: Zijie Wang, Aichun Zhu, Jingyi Xue, Xili Wan, Chao Liu, Tian Wang, Yifeng
  Li
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: wang2022caibc
citations: 69
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.05773'}]
tags: ["Datasets", "Evaluation", "Scalability", "Supervised"]
short_authors: Wang et al.
---
Given a natural language description, text-based person retrieval aims to
identify images of a target person from a large-scale person image database.
Existing methods generally face a \textbf\{color over-reliance problem\}, which
means that the models rely heavily on color information when matching
cross-modal data. Indeed, color information is an important decision-making
accordance for retrieval, but the over-reliance on color would distract the
model from other key clues (e.g. texture information, structural information,
etc.), and thereby lead to a sub-optimal retrieval performance. To solve this
problem, in this paper, we propose to \textbf\{C\}apture \textbf\{A\}ll-round
\textbf\{I\}nformation \textbf\{B\}eyond \textbf\{C\}olor (\textbf\{CAIBC\}) via a
jointly optimized multi-branch architecture for text-based person retrieval.
CAIBC contains three branches including an RGB branch, a grayscale (GRS) branch
and a color (CLR) branch. Besides, with the aim of making full use of all-round
information in a balanced and effective way, a mutual learning mechanism is
employed to enable the three branches which attend to varied aspects of
information to communicate with and learn from each other. Extensive
experimental analysis is carried out to evaluate our proposed CAIBC method on
the CUHK-PEDES and RSTPReid datasets in both \textbf\{supervised\} and
\textbf\{weakly supervised\} text-based person retrieval settings, which
demonstrates that CAIBC significantly outperforms existing methods and achieves
the state-of-the-art performance on all the three tasks.