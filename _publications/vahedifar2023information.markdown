---
layout: publication
title: Information Modified K-nearest Neighbor
authors: Mohammad Ali Vahedifar, Azim Akhtarshenas, Maryam Sabbaghian, Mohammad Mohammadi
  Rafatpanah, Ramin Toosi
conference: Arxiv
year: 2023
bibkey: vahedifar2023information
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.01991'}]
tags: []
short_authors: Vahedifar et al.
---
The fundamental concept underlying K-Nearest Neighbors (KNN) is the
classification of samples based on the majority through their nearest
neighbors. Although distance and neighbors' labels are critical in KNN,
traditional KNN treats all samples equally. However, some KNN variants weigh
neighbors differently based on a specific rule, considering each neighbor's
distance and label. Many KNN methodologies introduce complex algorithms that do
not significantly outperform the traditional KNN, often leading to less
satisfactory outcomes. The gap in reliably extracting information for
accurately predicting true weights remains an open research challenge. In our
proposed method, information-modified KNN (IMKNN), we bridge the gap by
presenting a straightforward algorithm that achieves effective results. To this
end, we introduce a classification method to improve the performance of the KNN
algorithm. By exploiting mutual information (MI) and incorporating ideas from
Shapley's values, we improve the traditional KNN performance in accuracy,
precision, and recall, offering a more refined and effective solution.
  To evaluate the effectiveness of our method, it is compared with eight
variants of KNN. We conduct experiments on 12 widely-used datasets, achieving
11.05%, 12.42%, and 12.07% in accuracy, precision, and recall performance,
respectively, compared to traditional KNN. Additionally, we compared IMKNN with
traditional KNN across four large-scale datasets to highlight the distinct
advantages of IMKNN in the impact of monotonicity, noise, density, subclusters,
and skewed distributions. Our research indicates that IMKNN consistently
surpasses other methods in diverse datasets.