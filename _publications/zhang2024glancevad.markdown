---
layout: publication
title: 'Glancevad: Exploring Glance Supervision For Label-efficient Video Anomaly
  Detection'
authors: Huaxin Zhang, Xiang Wang, Xiaohao Xu, Xiaonan Huang, Chuchu Han, Yuehuan
  Wang, Changxin Gao, Shanjun Zhang, Nong Sang
conference: Arxiv
year: 2024
bibkey: zhang2024glancevad
citations: 0
additional_links: [{name: Code, url: 'https://github.com/pipixin321/GlanceVAD'}, {
    name: Paper, url: 'https://arxiv.org/abs/2403.06154'}]
tags: []
short_authors: Zhang et al.
---
In recent years, video anomaly detection has been extensively investigated in
both unsupervised and weakly supervised settings to alleviate costly temporal
labeling. Despite significant progress, these methods still suffer from
unsatisfactory results such as numerous false alarms, primarily due to the
absence of precise temporal anomaly annotation. In this paper, we present a
novel labeling paradigm, termed "glance annotation", to achieve a better
balance between anomaly detection accuracy and annotation cost. Specifically,
glance annotation is a random frame within each abnormal event, which can be
easily accessed and is cost-effective. To assess its effectiveness, we manually
annotate the glance annotations for two standard video anomaly detection
datasets: UCF-Crime and XD-Violence. Additionally, we propose a customized
GlanceVAD method, that leverages gaussian kernels as the basic unit to compose
the temporal anomaly distribution, enabling the learning of diverse and robust
anomaly representations from the glance annotations. Through comprehensive
analysis and experiments, we verify that the proposed labeling paradigm can
achieve an excellent trade-off between annotation cost and model performance.
Extensive experimental results also demonstrate the effectiveness of our
GlanceVAD approach, which significantly outperforms existing advanced
unsupervised and weakly supervised methods. Code and annotations will be
publicly available at https://github.com/pipixin321/GlanceVAD.