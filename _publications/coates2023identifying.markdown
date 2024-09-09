---
layout: publication
title: "Identifying document similarity using a fast estimation of the Levenshtein Distance based on compression and signatures"
authors: Coates Peter, Breitinger Frank
conference: Arxiv
year: 2023
bibkey: coates2023identifying
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2307.11496"}
tags: ['ARXIV']
---
Identifying document similarity has many applications, e.g., source code analysis or plagiarism detection. However, identifying similarities is not trivial and can be time complex. For instance, the Levenshtein Distance is a common metric to define the similarity between two documents but has quadratic runtime which makes it impractical for large documents where large starts with a few hundred kilobytes. In this paper, we present a novel concept that allows estimating the Levenshtein Distance: the algorithm first compresses documents to signatures (similar to hash values) using a user-defined compression ratio. Signatures can then be compared against each other (some constrains apply) where the outcome is the estimated Levenshtein Distance. Our evaluation shows promising results in terms of runtime efficiency and accuracy. In addition, we introduce a significance score allowing examiners to set a threshold and identify related documents.