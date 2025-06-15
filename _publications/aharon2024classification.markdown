---
layout: publication
title: 'A Classification-by-retrieval Framework For Few-shot Anomaly Detection To Detect API Injection Attacks'
authors: Udi Aharon, Ran Dubin, Amit Dvir, Chen Hajaj
conference: "Computers Security Volume 140 December 2024 Article 104249"
year: 2024
citations: 0
bibkey: aharon2024classification
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2405.11247'}
tags: ['Retrieval Models', 'Unimodal', 'Shallow', 'Datasets', 'Vector Indexing', 'Supervised', 'Training Strategy']
---
Application Programming Interface (API) Injection attacks refer to the unauthorized or malicious use of APIs, which are often exploited to gain access to sensitive data or manipulate online systems for illicit purposes. Identifying actors that deceitfully utilize an API poses a demanding problem. Although there have been notable advancements and contributions in the field of API security, there remains a significant challenge when dealing with attackers who use novel approaches that don't match the well-known payloads commonly seen in attacks. Also, attackers may exploit standard functionalities unconventionally and with objectives surpassing their intended boundaries. Thus, API security needs to be more sophisticated and dynamic than ever, with advanced computational intelligence methods, such as machine learning models that can quickly identify and respond to abnormal behavior. In response to these challenges, we propose a novel unsupervised few-shot anomaly detection framework composed of two main parts: First, we train a dedicated generic language model for API based on FastText embedding. Next, we use Approximate Nearest Neighbor search in a classification-by-retrieval approach. Our framework allows for training a fast, lightweight classification model using only a few examples of normal API requests. We evaluated the performance of our framework using the CSIC 2010 and ATRDF 2023 datasets. The results demonstrate that our framework improves API attack detection accuracy compared to the state-of-the-art (SOTA) unsupervised anomaly detection baselines.
