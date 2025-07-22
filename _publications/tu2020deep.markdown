---
layout: publication
title: Deep Cross-modal Hashing via Margin-dynamic-softmax Loss
authors: Tu et al.
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2020
bibkey: tu2020deep
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.03451'}]
tags: ["Hashing-Methods"]
---
Due to their high retrieval efficiency and low storage cost for cross-modal
search task, cross-modal hashing methods have attracted considerable attention.
For the supervised cross-modal hashing methods, how to make the learned hash
codes preserve semantic information sufficiently contained in the label of
datapoints is the key to further enhance the retrieval performance. Hence,
almost all supervised cross-modal hashing methods usually depends on defining a
similarity between datapoints with the label information to guide the hashing
model learning fully or partly. However, the defined similarity between
datapoints can only capture the label information of datapoints partially and
misses abundant semantic information, then hinders the further improvement of
retrieval performance. Thus, in this paper, different from previous works, we
propose a novel cross-modal hashing method without defining the similarity
between datapoints, called Deep Cross-modal Hashing via
\textit\{Margin-dynamic-softmax Loss\} (DCHML). Specifically, DCHML first trains
a proxy hashing network to transform each category information of a dataset
into a semantic discriminative hash code, called proxy hash code. Each proxy
hash code can preserve the semantic information of its corresponding category
well. Next, without defining the similarity between datapoints to supervise the
training process of the modality-specific hashing networks , we propose a novel
\textit\{margin-dynamic-softmax loss\} to directly utilize the proxy hashing
codes as supervised information. Finally, by minimizing the novel
\textit\{margin-dynamic-softmax loss\}, the modality-specific hashing networks
can be trained to generate hash codes which can simultaneously preserve the
cross-modal similarity and abundant semantic information well.