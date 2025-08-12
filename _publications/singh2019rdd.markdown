---
layout: publication
title: 'Rdd-eclat: Approaches To Parallelize Eclat Algorithm On Spark RDD Framework'
authors: Pankaj Singh, Sudhakar Singh, P. K. Mishra, Rakhi Garg
conference: Lecture Notes on Data Engineering and Communications Technologies
year: 2020
bibkey: singh2019rdd
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.06415'}]
tags: ["Scalability", "Tools & Libraries"]
short_authors: Singh et al.
---
Initially, a number of frequent itemset mining (FIM) algorithms have been
designed on the Hadoop MapReduce, a distributed big data processing framework.
But, due to heavy disk I/O, MapReduce is found to be inefficient for such
highly iterative algorithms. Therefore, Spark, a more efficient distributed
data processing framework, has been developed with in-memory computation and
resilient distributed dataset (RDD) features to support the iterative
algorithms. On the Spark RDD framework, Apriori and FP-Growth based FIM
algorithms have been designed, but Eclat-based algorithm has not been explored
yet. In this paper, RDD-Eclat, a parallel Eclat algorithm on the Spark RDD
framework is proposed with its five variants. The proposed algorithms are
evaluated on the various benchmark datasets, which shows that RDD-Eclat
outperforms the Spark-based Apriori by many times. Also, the experimental
results show the scalability of the proposed algorithms on increasing the
number of cores and size of the dataset.