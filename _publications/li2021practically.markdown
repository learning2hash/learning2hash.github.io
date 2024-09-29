---
layout: publication
title: C45;minhash Practically Reducing Two Permutations To Just One
authors: Li Xiaoyun, Li Ping
conference: "Arxiv"
year: 2021
bibkey: li2021practically
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2109.04595"}
tags: ['ARXIV', 'Independent']
---
Traditional minwise hashing (MinHash) requires applying K independent permutations to estimate the Jaccard similarity in massive binary (0/1) data where K can be (e.g.) 1024 or even larger depending on applications. The recent work on C45;MinHash (Li and Li 2021) has shown with rigorous proofs that only two permutations are needed. An initial permutation is applied to break whatever structures which might exist in the data and a second permutation is re45;used K times to produce K hashes via a circulant shifting fashion. (Li and Li 2021) has proved that perhaps surprisingly even though the K hashes are correlated the estimation variance is strictly smaller than the variance of the traditional MinHash. It has been demonstrated in (Li and Li 2021) that the initial permutation in C45;MinHash is indeed necessary. For the ease of theoretical analysis they have used two independent permutations. In this paper we show that one can actually simply use one permutation. That is one single permutation is used for both the initial pre45;processing step to break the structures in the data and the circulant hashing step to generate K hashes. Although the theoretical analysis becomes very complicated we are able to explicitly write down the expression for the expectation of the estimator. The new estimator is no longer unbiased but the bias is extremely small and has essentially no impact on the estimation accuracy (mean square errors). An extensive set of experiments are provided to verify our claim for using just one permutation.
