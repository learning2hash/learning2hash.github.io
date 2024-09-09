---
layout: publication
title: Hadamard Matrix Guided Online Hashing
authors: Lin Mingbao, Ji Rongrong, Liu Hong, Sun Xiaoshuai, Chen Shen, Tian Qi
conference: "Arxiv"
year: 2019
bibkey: lin2019hadamard
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1905.04454"}
tags: ['ARXIV', 'LSH', 'Supervised']
---
Online image hashing has attracted increasing research attention recently which receives large-scale data in a streaming manner to update the hash functions on-the-fly. Its key challenge lies in the difficulty of balancing the learning timeliness and model accuracy. To this end most works follow a supervised setting i.e. using class labels to boost the hashing performance which defects in two aspects First strong constraints e.g. orthogonal or similarity preserving are used which however are typically relaxed and lead to large accuracy drop. Second large amounts of training batches are required to learn the up-to-date hash functions which largely increase the learning complexity. To handle the above challenges a novel supervised online hashing scheme termed Hadamard Matrix Guided Online Hashing (HMOH) is proposed in this paper. Our key innovation lies in introducing Hadamard matrix which is an orthogonal binary matrix built via Sylvester method. In particular to release the need of strong constraints we regard each column of Hadamard matrix as the target code for each class label which by nature satisfies several desired properties of hashing codes. To accelerate the online training LSH is first adopted to align the lengths of target code and to-be-learned binary code. We then treat the learning of hash functions as a set of binary classification problems to fit the assigned target code. Finally extensive experiments demonstrate the superior accuracy and efficiency of the proposed method over various state-of-the-art methods. Codes are available at httpsgithub.com/lmbxmu/mycode.
