---
layout: publication
title: Locality-aware Hybrid Coded Mapreduce For Server-rack Architecture
authors: Sneh Gupta, V. Lalitha
conference: 2017 IEEE Information Theory Workshop (ITW)
year: 2017
bibkey: gupta2017locality
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.01440'}]
tags: []
short_authors: Sneh Gupta, V. Lalitha
---
MapReduce is a widely used framework for distributed computing. Data
shuffling between the Map phase and Reduce phase of a job involves a large
amount of data transfer across servers, which in turn accounts for increase in
job completion time. Recently, Coded MapReduce has been proposed to offer
savings with respect to the communication cost incurred in data shuffling. This
is achieved by creating coded multicast opportunities for shuffling through
repeating Map tasks at multiple servers. We consider a server-rack architecture
for MapReduce and in this architecture, propose to divide the total
communication cost into two: intra-rack communication cost and cross-rack
communication cost. Having noted that cross-rack data transfer operates at
lower speed as compared to intra-rack data transfer, we present a scheme termed
as Hybrid Coded MapReduce which results in lower cross-rack communication than
Coded MapReduce at the cost of increase in intra-rack communication. In
addition, we pose the problem of assigning Map tasks to servers to maximize
data locality in the framework of Hybrid Coded MapReduce as a constrained
integer optimization problem. We show through simulations that data locality
can be improved considerably by using the solution of optimization to assign
Map tasks to servers.