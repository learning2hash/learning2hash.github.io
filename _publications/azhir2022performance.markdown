---
layout: publication
title: Performance Evaluation Of Query Plan Recommendation With Apache Hadoop And
  Apache Spark
authors: Elham Azhir, Mehdi Hosseinzadeh, Faheem Khan, Amir Mosavi
conference: Mathematics
year: 2022
bibkey: azhir2022performance
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.07143'}]
tags: ["Efficiency", "Evaluation", "Recommender Systems", "Scalability"]
short_authors: Azhir et al.
---
Access plan recommendation is a query optimization approach that executes new
queries using prior created query execution plans (QEPs). The query optimizer
divides the query space into clusters in the mentioned method. However,
traditional clustering algorithms take a significant amount of execution time
for clustering such large datasets. The MapReduce distributed computing model
provides efficient solutions for storing and processing vast quantities of
data. Apache Spark and Apache Hadoop frameworks are used in the present
investigation to cluster different sizes of query datasets in the
MapReduce-based access plan recommendation method. The performance evaluation
is performed based on execution time. The results of the experiments
demonstrated the effectiveness of parallel query clustering in achieving high
scalability. Furthermore, Apache Spark achieved better performance than Apache
Hadoop, reaching an average speedup of 2x.