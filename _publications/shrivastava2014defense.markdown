---
layout: publication
title: In Defense Of Minhash Over Simhash
authors: Shrivastava Anshumali, Li Ping
conference: "Arxiv"
year: 2014
bibkey: shrivastava2014defense
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1407.4416"}
tags: ['ARXIV', 'Independent', 'LSH']
---
<p>MinHash and SimHash are the two widely adopted Locality Sensitive
Hashing (LSH) algorithms for large-scale data processing applications.
Deciding which LSH to use for a particular problem at hand is an
important question, which has no clear answer in the existing
literature. In this study, we provide a theoretical answer (validated by
experiments) that MinHash virtually always outperforms SimHash when the
data are binary, as common in practice such as search. The collision
probability of MinHash is a function of resemblance similarity (<span
class="math inline">\(\mathcal{R}\)</span>), while the collision
probability of SimHash is a function of cosine similarity (<span
class="math inline">\(\mathcal{S}\)</span>). To provide a common basis
for comparison, we evaluate retrieval results in terms of <span
class="math inline">\(\mathcal{S}\)</span> for both MinHash and SimHash.
This evaluation is valid as we can prove that MinHash is a valid LSH
with respect to <span class="math inline">\(\mathcal{S}\)</span>, by
using a general inequality <span class="math inline">\(\mathcal{S}^2\leq
\mathcal{R}\leq \frac{\mathcal{S}}{2-\mathcal{S}}\)</span>. Our worst
case analysis can show that MinHash significantly outperforms SimHash in
high similarity region. Interestingly, our intensive experiments reveal
that MinHash is also substantially better than SimHash even in datasets
where most of the data points are not too similar to each other. This is
partly because, in practical data, often <span
class="math inline">\(\mathcal{R}\geq
\frac{\mathcal{S}}{z-\mathcal{S}}\)</span> holds where <span
class="math inline">\(z\)</span> is only slightly larger than 2 (e.g.,
<span class="math inline">\(z\leq 2.1\)</span>). Our restricted worst
case analysis by assuming <span
class="math inline">\(\frac{\mathcal{S}}{z-\mathcal{S}}\leq
\mathcal{R}\leq
\frac{\mathcal{S}}{2-\mathcal{S}}\)</span> shows that MinHash indeed
significantly outperforms SimHash even in low similarity region. We
believe the results in this paper will provide valuable guidelines for
search in practice, especially when the data are sparse.</p>
