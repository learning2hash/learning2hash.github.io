---
layout: publication
title: Learning Distributed Representations With Efficient Softmax Normalization
authors: Lorenzo Dall'Amico, Enrico Maria Belliardo
conference: Transactions on Machine Learning Research 2835-8856 2025
year: 2023
bibkey: dallamico2023learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.17475'}]
tags: ["Datasets", "Evaluation"]
short_authors: Lorenzo Dall'Amico, Enrico Maria Belliardo
---
Learning distributed representations, or embeddings, that encode the relational similarity patterns among objects is a relevant task in machine learning. A popular method to learn the embedding matrices \(X, Y\) is optimizing a loss function of the term \(\{\rm SoftMax\}(XY^T)\). The complexity required to calculate this term, however, runs quadratically with the problem size, making it a computationally heavy solution. In this article, we propose a linear-time heuristic approximation to compute the normalization constants of \(\{\rm SoftMax\}(XY^T)\) for embedding vectors with bounded norms. We show on some pre-trained embedding datasets that the proposed estimation method achieves higher or comparable accuracy with competing methods. From this result, we design an efficient and task-agnostic algorithm that learns the embeddings by optimizing the cross entropy between the softmax and a set of probability distributions given as inputs. The proposed algorithm is interpretable and easily adapted to arbitrary embedding problems. We consider a few use cases and observe similar or higher performances and a lower computational time than similar ``2Vec'' algorithms.