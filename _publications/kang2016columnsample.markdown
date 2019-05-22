---
layout: publication
title: "Column Sampling Based Discrete Supervised Hashing"
authors: Wang-Cheng Kang, Wu-Jun Li, Zhi-Hua Zhou
conference: AAAI
year: 2016
bibkey: kang2016columnsample
additional_links:
   - {name: "PDF", url: "http://cs.nju.edu.cn/lwj/paper/AAAI16_COSDISH.pdf"}
   - {name: "Code", url: "http://cs.nju.edu.cn/lwj/code/COSDISH.zip"}
---
By leveraging semantic (label) information, supervised hashing has demonstrated better accuracy than unsupervised hashing in many real applications. Because the hashing-code learning problem is essentially a discrete optimization problem which is hard to solve, most existing supervised hashing methods try to solve a relaxed continuous optimization problem by dropping the discrete constraints.
However, these methods typically suffer from poor performance due to the errors caused by the relaxation. Some other methods try to directly solve the discrete optimization problem. However, they are typically time-consuming and unscalable. In this paper, we propose a novel method, called column sampling based discrete supervised hashing (COSDISH), to directly learn the discrete hashing code from semantic information.
COSDISH is an iterative method, in each iteration of which several columns are sampled from the semantic similarity matrix and then the hashing code is decomposed into two parts which can be alternately optimized in a discrete way. Theoretical analysis shows that the learning (optimization) algorithm of COSDISH has a constant-approximation bound in each step of the alternating optimization procedure. Empirical results on datasets with semantic labels illustrate that COSDISH can outperform the state-of-the-art methods in real applications like image retrieval.
