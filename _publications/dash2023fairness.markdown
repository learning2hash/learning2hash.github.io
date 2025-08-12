---
layout: publication
title: 'Fairness In Image Search: A Study Of Occupational Stereotyping In Image Retrieval
  And Its Debiasing'
authors: Swagatika Dash
conference: Arxiv
year: 2023
bibkey: dash2023fairness
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.03881'}]
tags: ["Image Retrieval"]
short_authors: Swagatika Dash
---
Multi-modal search engines have experienced significant growth and widespread
use in recent years, making them the second most common internet use. While
search engine systems offer a range of services, the image search field has
recently become a focal point in the information retrieval community, as the
adage goes, "a picture is worth a thousand words". Although popular search
engines like Google excel at image search accuracy and agility, there is an
ongoing debate over whether their search results can be biased in terms of
gender, language, demographics, socio-cultural aspects, and stereotypes. This
potential for bias can have a significant impact on individuals' perceptions
and influence their perspectives.
  In this paper, we present our study on bias and fairness in web search, with
a focus on keyword-based image search. We first discuss several kinds of biases
that exist in search systems and why it is important to mitigate them. We
narrow down our study to assessing and mitigating occupational stereotypes in
image search, which is a prevalent fairness issue in image retrieval. For the
assessment of stereotypes, we take gender as an indicator. We explore various
open-source and proprietary APIs for gender identification from images. With
these, we examine the extent of gender bias in top-tanked image search results
obtained for several occupational keywords. To mitigate the bias, we then
propose a fairness-aware re-ranking algorithm that optimizes (a) relevance of
the search result with the keyword and (b) fairness w.r.t genders identified.
We experiment on 100 top-ranked images obtained for 10 occupational keywords
and consider random re-ranking and re-ranking based on relevance as baselines.
Our experimental results show that the fairness-aware re-ranking algorithm
produces rankings with better fairness scores and competitive relevance scores
than the baselines.