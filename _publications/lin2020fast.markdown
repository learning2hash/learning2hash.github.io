---
layout: publication
title: "Fast Class-wise Updating for Online Hashing"
authors: Lin Mingbao, Ji Rongrong, Sun Xiaoshuai, Zhang Baochang, Huang Feiyue, Tian Yonghong, Tao Dacheng
conference: Arxiv
year: 2020
bibkey: lin2020fast
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2012.00318"}
tags: ['ARXIV', 'Supervised']
---
Online image hashing has received increasing research attention recently, which processes large-scale data in a streaming fashion to update the hash functions on-the-fly. To this end, most existing works exploit this problem under a supervised setting, i.e., using class labels to boost the hashing performance, which suffers from the defects in both adaptivity and efficiency: First, large amounts of training batches are required to learn up-to-date hash functions, which leads to poor online adaptivity. Second, the training is time-consuming, which contradicts with the core need of online learning. In this paper, a novel supervised online hashing scheme, termed Fast Class-wise Updating for Online Hashing (FCOH), is proposed to address the above two challenges by introducing a novel and efficient inner product operation. To achieve fast online adaptivity, a class-wise updating method is developed to decompose the binary code learning and alternatively renew the hash functions in a class-wise fashion, which well addresses the burden on large amounts of training batches. Quantitatively, such a decomposition further leads to at least 75% storage saving. To further achieve online efficiency, we propose a semi-relaxation optimization, which accelerates the online training by treating different binary constraints independently. Without additional constraints and variables, the time complexity is significantly reduced. Such a scheme is also quantitatively shown to well preserve past information during updating hashing functions. We have quantitatively demonstrated that the collective effort of class-wise updating and semi-relaxation optimization provides a superior performance comparing to various state-of-the-art methods, which is verified through extensive experiments on three widely-used datasets.