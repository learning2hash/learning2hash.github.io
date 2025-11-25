---
layout: publication
title: Fast Wireless Sensor Anomaly Detection Based On Data Stream In Edge Computing
  Enabled Smart Greenhouse
authors: Yihong Yang, Sheng Ding, Yuwen Liu, Shunmei Meng, Xiaoxiao Chi, Rui Ma, Chao
  Yan
conference: Arxiv
year: 2021
bibkey: yang2021fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.13353'}]
tags: ["Efficiency", "Locality-Sensitive-Hashing"]
short_authors: Yang et al.
---
Edge computing enabled smart greenhouse is a representative application of
Internet of Things technology, which can monitor the environmental information
in real time and employ the information to contribute to intelligent
decision-making. In the process, anomaly detection for wireless sensor data
plays an important role. However, traditional anomaly detection algorithms
originally designed for anomaly detection in static data have not properly
considered the inherent characteristics of data stream produced by wireless
sensor such as infiniteness, correlations and concept drift, which may pose a
considerable challenge on anomaly detection based on data stream, and lead to
low detection accuracy and efficiency. First, data stream usually generates
quickly which means that it is infinite and enormous, so any traditional
off-line anomaly detection algorithm that attempts to store the whole dataset
or to scan the dataset multiple times for anomaly detection will run out of
memory space. Second, there exist correlations among different data streams,
which traditional algorithms hardly consider. Third, the underlying data
generation process or data distribution may change over time. Thus, traditional
anomaly detection algorithms with no model update will lose their effects.
Considering these issues, a novel method (called DLSHiForest) on basis of
Locality-Sensitive Hashing and time window technique in this paper is proposed
to solve these problems while achieving accurate and efficient detection.
Comprehensive experiments are executed using real-world agricultural greenhouse
dataset to demonstrate the feasibility of our approach. Experimental results
show that our proposal is practicable in addressing challenges of traditional
anomaly detection while ensuring accuracy and efficiency.