---
layout: publication
title: Scene Text Recognition With Image-text Matching-guided Dictionary
authors: Jiajun Wei, Hongjian Zhan, Xiao Tu, Yue Lu, Umapada Pal
conference: Arxiv
year: 2023
bibkey: wei2023scene
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.04524'}]
tags: [Evaluation, Datasets]
short_authors: Wei et al.
---
Employing a dictionary can efficiently rectify the deviation between the
visual prediction and the ground truth in scene text recognition methods.
However, the independence of the dictionary on the visual features may lead to
incorrect rectification of accurate visual predictions. In this paper, we
propose a new dictionary language model leveraging the Scene Image-Text
Matching(SITM) network, which avoids the drawbacks of the explicit dictionary
language model: 1) the independence of the visual features; 2) noisy choice in
candidates etc. The SITM network accomplishes this by using Image-Text
Contrastive (ITC) Learning to match an image with its corresponding text among
candidates in the inference stage. ITC is widely used in vision-language
learning to pull the positive image-text pair closer in feature space. Inspired
by ITC, the SITM network combines the visual features and the text features of
all candidates to identify the candidate with the minimum distance in the
feature space. Our lexicon method achieves better results(93.8% accuracy) than
the ordinary method results(92.1% accuracy) on six mainstream benchmarks.
Additionally, we integrate our method with ABINet and establish new
state-of-the-art results on several benchmarks.