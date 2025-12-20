---
layout: publication
title: 'Metricbert: Text Representation Learning Via Self-supervised Triplet Training'
authors: Itzik Malkiel, Dvir Ginzburg, Oren Barkan, Avi Caciularu, Yoni Weill, Noam
  Koenigstein
conference: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: malkiel2022metricbert
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.06610'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Self-Supervised", "Supervised"]
short_authors: Malkiel et al.
---
We present MetricBERT, a BERT-based model that learns to embed text under a
well-defined similarity metric while simultaneously adhering to the
``traditional'' masked-language task. We focus on downstream tasks of learning
similarities for recommendations where we show that MetricBERT outperforms
state-of-the-art alternatives, sometimes by a substantial margin. We conduct
extensive evaluations of our method and its different variants, showing that
our training objective is highly beneficial over a traditional contrastive
loss, a standard cosine similarity objective, and six other baselines. As an
additional contribution, we publish a dataset of video games descriptions along
with a test set of similarity annotations crafted by a domain expert.