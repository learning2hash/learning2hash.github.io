---
layout: publication
title: 'Seeing Without Looking: Analysis Pipeline For Child Sexual Abuse Datasets'
authors: "Camila Laranjeira, Jo\xE3o MacEdo, Sandra Avila, Jefersson A. Dos Santos"
conference: 2022 ACM Conference on Fairness Accountability and Transparency
year: 2022
bibkey: laranjeira2022seeing
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.14110'}]
tags: ["Datasets", "Evaluation"]
short_authors: Laranjeira et al.
---
The online sharing and viewing of Child Sexual Abuse Material (CSAM) are
growing fast, such that human experts can no longer handle the manual
inspection. However, the automatic classification of CSAM is a challenging
field of research, largely due to the inaccessibility of target data that is -
and should forever be - private and in sole possession of law enforcement
agencies. To aid researchers in drawing insights from unseen data and safely
providing further understanding of CSAM images, we propose an analysis template
that goes beyond the statistics of the dataset and respective labels. It
focuses on the extraction of automatic signals, provided both by pre-trained
machine learning models, e.g., object categories and pornography detection, as
well as image metrics such as luminance and sharpness. Only aggregated
statistics of sparse signals are provided to guarantee the anonymity of
children and adolescents victimized. The pipeline allows filtering the data by
applying thresholds to each specified signal and provides the distribution of
such signals within the subset, correlations between signals, as well as a bias
evaluation. We demonstrated our proposal on the Region-based annotated Child
Pornography Dataset (RCPD), one of the few CSAM benchmarks in the literature,
composed of over 2000 samples among regular and CSAM images, produced in
partnership with Brazil's Federal Police. Although noisy and limited in several
senses, we argue that automatic signals can highlight important aspects of the
overall distribution of data, which is valuable for databases that can not be
disclosed. Our goal is to safely publicize the characteristics of CSAM
datasets, encouraging researchers to join the field and perhaps other
institutions to provide similar reports on their benchmarks.