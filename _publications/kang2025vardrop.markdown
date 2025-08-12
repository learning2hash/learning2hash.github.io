---
layout: publication
title: 'Vardrop: Enhancing Training Efficiency By Reducing Variate Redundancy In Periodic
  Time Series Forecasting'
authors: Junhyeok Kang, Yooju Shin, Jae-Gil Lee
conference: Arxiv
year: 2025
bibkey: kang2025vardrop
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.14183'}]
tags: ["Efficiency"]
short_authors: Junhyeok Kang, Yooju Shin, Jae-Gil Lee
---
Variate tokenization, which independently embeds each variate as separate
tokens, has achieved remarkable improvements in multivariate time series
forecasting. However, employing self-attention with variate tokens incurs a
quadratic computational cost with respect to the number of variates, thus
limiting its training efficiency for large-scale applications. To address this
issue, we propose VarDrop, a simple yet efficient strategy that reduces the
token usage by omitting redundant variate tokens during training. VarDrop
adaptively excludes redundant tokens within a given batch, thereby reducing the
number of tokens used for dot-product attention while preserving essential
information. Specifically, we introduce k-dominant frequency hashing (k-DFH),
which utilizes the ranked dominant frequencies in the frequency domain as a
hash value to efficiently group variate tokens exhibiting similar periodic
behaviors. Then, only representative tokens in each group are sampled through
stratified sampling. By performing sparse attention with these selected tokens,
the computational cost of scaled dot-product attention is significantly
alleviated. Experiments conducted on public benchmark datasets demonstrate that
VarDrop outperforms existing efficient baselines.