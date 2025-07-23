---
layout: publication
title: Evaluating The Performance-deviation Of Itemknn In Recbole And Lenskit
authors: Schmidt Michael, Nitschke Jannik, Prinz Tim
conference: Arxiv
year: 2024
bibkey: schmidt2024evaluating
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.13531'}]
tags: ["Efficiency", "Evaluation", "Recommender Systems", "Scalability", "Tools & Libraries"]
short_authors: Schmidt Michael, Nitschke Jannik, Prinz Tim
---
This study examines the performance of item-based k-Nearest Neighbors
(ItemKNN) algorithms in the RecBole and LensKit recommender system libraries.
Using four data sets (Anime, Modcloth, ML-100K, and ML-1M), we assess each
library's efficiency, accuracy, and scalability, focusing primarily on
normalized discounted cumulative gain (nDCG). Our results show that RecBole
outperforms LensKit on two of three metrics on the ML-100K data set: it
achieved an 18% higher nDCG, 14% higher precision, and 35% lower recall. To
ensure a fair comparison, we adjusted LensKit's nDCG calculation to match
RecBole's method. This alignment made the performance more comparable, with
LensKit achieving an nDCG of 0.2540 and RecBole 0.2674. Differences in
similarity matrix calculations were identified as the main cause of performance
deviations. After modifying LensKit to retain only the top K similar items,
both libraries showed nearly identical nDCG values across all data sets. For
instance, both achieved an nDCG of 0.2586 on the ML-1M data set with the same
random seed. Initially, LensKit's original implementation only surpassed
RecBole in the ModCloth dataset.