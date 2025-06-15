---
layout: publication
title: 'Locality Sensitive Hashing With Extended Differential Privacy'
authors: Natasha Fernandes, Yusuke Kawamoto, Takao Murakami
conference: "Proceedings of the 26th European Symposium on Research in Computer Security (ESORICS 2021) Part II Lecture Notes in Computer Science Vol. 12973 pp.563-583 2021"
year: 2020
citations: 4
bibkey: fernandes2020locality
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2010.09393'}
tags: ['Hashing Methods', 'Applications', 'Privacy and Security', 'Tools and Libraries', 'Hashing Fundamentals']
---
Extended differential privacy, a generalization of standard differential
privacy (DP) using a general metric, has been widely studied to provide
rigorous privacy guarantees while keeping high utility. However, existing works
on extended DP are limited to few metrics, such as the Euclidean metric.
Consequently, they have only a small number of applications, such as
location-based services and document processing. In this paper, we propose a
couple of mechanisms providing extended DP with a different metric: angular
distance (or cosine distance). Our mechanisms are based on locality sensitive
hashing (LSH), which can be applied to the angular distance and work well for
personal data in a high-dimensional space. We theoretically analyze the privacy
properties of our mechanisms, and prove extended DP for input data by taking
into account that LSH preserves the original metric only approximately. We
apply our mechanisms to friend matching based on high-dimensional personal data
with angular distance in the local model, and evaluate our mechanisms using two
real datasets. We show that LDP requires a very large privacy budget and that
RAPPOR does not work in this application. Then we show that our mechanisms
enable friend matching with high utility and rigorous privacy guarantees based
on extended DP.
