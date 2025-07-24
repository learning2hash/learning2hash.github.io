---
layout: publication
title: Minwise-independent Permutations With Insertion And Deletion Of Features
authors: Rameshwar Pratap, Raghav Kulkarni
conference: Lecture Notes in Computer Science
year: 2023
bibkey: pratap2023minwise
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.11240'}]
tags: ["Datasets", "Evaluation", "Locality Sensitive Hashing"]
short_authors: Rameshwar Pratap, Raghav Kulkarni
---
In their seminal work, Broder \textit\{et. al.\}~\citep\{BroderCFM98\} introduces
the \\(\mathrm\{minHash\}\\) algorithm that computes a low-dimensional sketch of
high-dimensional binary data that closely approximates pairwise Jaccard
similarity. Since its invention, \\(\mathrm\{minHash\}\\) has been commonly used by
practitioners in various big data applications. Further, the data is dynamic in
many real-life scenarios, and their feature sets evolve over time. We consider
the case when features are dynamically inserted and deleted in the dataset. We
note that a naive solution to this problem is to repeatedly recompute
\\(\mathrm\{minHash\}\\) with respect to the updated dimension. However, this is an
expensive task as it requires generating fresh random permutations. To the best
of our knowledge, no systematic study of \\(\mathrm\{minHash\}\\) is recorded in the
context of dynamic insertion and deletion of features. In this work, we
initiate this study and suggest algorithms that make the \\(\mathrm\{minHash\}\\)
sketches adaptable to the dynamic insertion and deletion of features. We show a
rigorous theoretical analysis of our algorithms and complement it with
extensive experiments on several real-world datasets. Empirically we observe a
significant speed-up in the running time while simultaneously offering
comparable performance with respect to running \\(\mathrm\{minHash\}\\) from scratch.
Our proposal is efficient, accurate, and easy to implement in practice.