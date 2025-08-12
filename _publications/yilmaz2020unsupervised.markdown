---
layout: publication
title: Unsupervised Anomaly Detection Via Deep Metric Learning With End-to-end Optimization
authors: Selim F. Yilmaz, Suleyman S. Kozat
conference: Arxiv
year: 2020
bibkey: yilmaz2020unsupervised
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.05865'}]
tags: ["Distance Metric Learning", "Unsupervised"]
short_authors: Selim F. Yilmaz, Suleyman S. Kozat
---
We investigate unsupervised anomaly detection for high-dimensional data and
introduce a deep metric learning (DML) based framework. In particular, we learn
a distance metric through a deep neural network. Through this metric, we
project the data into the metric space that better separates the anomalies from
the normal data and reduces the effect of the curse of dimensionality for
high-dimensional data. We present a novel data distillation method through
self-supervision to remedy the conventional practice of assuming all data as
normal. We also employ the hard mining technique from the DML literature. We
show these components improve the performance of our model and significantly
reduce the running time. Through an extensive set of experiments on the 14
real-world datasets, our method demonstrates significant performance gains
compared to the state-of-the-art unsupervised anomaly detection methods, e.g.,
an absolute improvement between 4.44% and 11.74% on the average over the 14
datasets. Furthermore, we share the source code of our method on Github to
facilitate further research.