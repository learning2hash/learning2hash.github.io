---
layout: publication
title: Benchmarking Hashing Algorithms for Load Balancing in a Distributed Database Environment
authors: Slesarev Alexander, Mikhailov Mikhail, Chernishev George
conference: "Arxiv"
year: 2022
bibkey: slesarev2022benchmarking
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2211.00741"}
tags: ['ARXIV', 'TIP']
---
Modern high load applications store data using multiple database instances. Such an architecture requires data consistency and it is important to ensure even distribution of data among nodes. Load balancing is used to achieve these goals. Hashing is the backbone of virtually all load balancing systems. Since the introduction of classic Consistent Hashing many algorithms have been devised for this purpose. One of the purposes of the load balancer is to ensure storage cluster scalability. It is crucial for the performance of the whole system to transfer as few data records as possible during node addition or removal. The load balancer hashing algorithm has the greatest impact on this process. In this paper we experimentally evaluate several hashing algorithms used for load balancing conducting both simulated and real system experiments. To evaluate algorithm performance we have developed a benchmark suite based on Unidata MDM~ -- a scalable toolkit for various Master Data Management (MDM) applications. For assessment we have employed three criteria~ -- uniformity of the produced distribution the number of moved records and computation speed. Following the results of our experiments we have created a table in which each algorithm is given an assessment according to the abovementioned criteria.
