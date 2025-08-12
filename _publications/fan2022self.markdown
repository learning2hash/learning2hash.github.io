---
layout: publication
title: Self-support Few-shot Semantic Segmentation
authors: Qi Fan, Wenjie Pei, Yu-Wing Tai, Chi-Keung Tang
conference: Lecture Notes in Computer Science
year: 2022
bibkey: fan2022self
citations: 109
additional_links: [{name: Code, url: 'https://github.com/fanq15/SSP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2207.11549'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Fan et al.
---
Existing few-shot segmentation methods have achieved great progress based on
the support-query matching framework. But they still heavily suffer from the
limited coverage of intra-class variations from the few-shot supports provided.
Motivated by the simple Gestalt principle that pixels belonging to the same
object are more similar than those to different objects of same class, we
propose a novel self-support matching strategy to alleviate this problem, which
uses query prototypes to match query features, where the query prototypes are
collected from high-confidence query predictions. This strategy can effectively
capture the consistent underlying characteristics of the query objects, and
thus fittingly match query features. We also propose an adaptive self-support
background prototype generation module and self-support loss to further
facilitate the self-support matching procedure. Our self-support network
substantially improves the prototype quality, benefits more improvement from
stronger backbones and more supports, and achieves SOTA on multiple datasets.
Codes are at https://github.com/fanq15/SSP.