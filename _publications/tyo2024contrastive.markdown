---
layout: publication
title: Contrastive Multiple Instance Learning For Weakly Supervised Person Reid
authors: Jacob Tyo, Zachary C. Lipton
conference: Arxiv
year: 2024
bibkey: tyo2024contrastive
citations: 0
additional_links: [{name: Code, url: 'https://drive.google.com/file/d/1rjMbWB6m-apHF3Wg_cfqc8QqKgQ21AsT/view?usp=drive_link'},
  {name: Paper, url: 'https://arxiv.org/abs/2402.07685'}]
tags: ["Distance Metric Learning"]
short_authors: Jacob Tyo, Zachary C. Lipton
---
The acquisition of large-scale, precisely labeled datasets for person
re-identification (ReID) poses a significant challenge. Weakly supervised ReID
has begun to address this issue, although its performance lags behind fully
supervised methods. In response, we introduce Contrastive Multiple Instance
Learning (CMIL), a novel framework tailored for more effective weakly
supervised ReID. CMIL distinguishes itself by requiring only a single model and
no pseudo labels while leveraging contrastive losses -- a technique that has
significantly enhanced traditional ReID performance yet is absent in all prior
MIL-based approaches. Through extensive experiments and analysis across three
datasets, CMIL not only matches state-of-the-art performance on the large-scale
SYSU-30k dataset with fewer assumptions but also consistently outperforms all
baselines on the WL-market1501 and Weakly Labeled MUddy racer re-iDentification
dataset (WL-MUDD) datasets. We introduce and release the WL-MUDD dataset, an
extension of the MUDD dataset featuring naturally occurring weak labels from
the real-world application at PerformancePhoto.co. All our code and data are
accessible at
https://drive.google.com/file/d/1rjMbWB6m-apHF3Wg_cfqc8QqKgQ21AsT/view?usp=drive_link.