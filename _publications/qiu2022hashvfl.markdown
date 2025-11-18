---
layout: publication
title: 'Hashvfl: Defending Against Data Reconstruction Attacks In Vertical Federated
  Learning'
authors: Pengyu Qiu, Xuhong Zhang, Shouling Ji, Chong Fu, Xing Yang, Ting Wang
conference: IEEE Transactions on Information Forensics and Security
year: 2022
bibkey: qiu2022hashvfl
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.00325'}]
tags: ["Evaluation", "Hashing Methods", "Robustness"]
short_authors: Qiu et al.
---
Vertical Federated Learning (VFL) is a trending collaborative machine
learning model training solution. Existing industrial frameworks employ secure
multi-party computation techniques such as homomorphic encryption to ensure
data security and privacy. Despite these efforts, studies have revealed that
data leakage remains a risk in VFL due to the correlations between intermediate
representations and raw data. Neural networks can accurately capture these
correlations, allowing an adversary to reconstruct the data. This emphasizes
the need for continued research into securing VFL systems.
  Our work shows that hashing is a promising solution to counter data
reconstruction attacks. The one-way nature of hashing makes it difficult for an
adversary to recover data from hash codes. However, implementing hashing in VFL
presents new challenges, including vanishing gradients and information loss. To
address these issues, we propose HashVFL, which integrates hashing and
simultaneously achieves learnability, bit balance, and consistency.
  Experimental results indicate that HashVFL effectively maintains task
performance while defending against data reconstruction attacks. It also brings
additional benefits in reducing the degree of label leakage, mitigating
adversarial attacks, and detecting abnormal inputs. We hope our work will
inspire further research into the potential applications of HashVFL.