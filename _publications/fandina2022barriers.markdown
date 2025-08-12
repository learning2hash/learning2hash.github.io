---
layout: publication
title: Barriers For Faster Dimensionality Reduction
authors: "Ora Nova Fandina, Mikael M\xF8ller H\xF8gsgaard, Kasper Green Larsen"
conference: Arxiv
year: 2023
bibkey: fandina2022barriers
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.03304'}]
tags: []
short_authors: "Ora Nova Fandina, Mikael M\xF8ller H\xF8gsgaard, Kasper Green Larsen"
---
The Johnson-Lindenstrauss transform allows one to embed a dataset of \\(n\\)
points in \\(\mathbb\{R\}^d\\) into \\(\mathbb\{R\}^m,\\) while preserving the pairwise
distance between any pair of points up to a factor \\((1 \pm \epsilon)\\),
provided that \\(m = Ω(\epsilon^\{-2\} \lg n)\\). The transform has found an
overwhelming number of algorithmic applications, allowing to speed up
algorithms and reducing memory consumption at the price of a small loss in
accuracy. A central line of research on such transforms, focus on developing
fast embedding algorithms, with the classic example being the Fast JL transform
by Ailon and Chazelle. All known such algorithms have an embedding time of
\\(Ω(d \lg d)\\), but no lower bounds rule out a clean \\(O(d)\\) embedding time.
In this work, we establish the first non-trivial lower bounds (of magnitude
\\(Ω(m \lg m)\\)) for a large class of embedding algorithms, including in
particular most known upper bounds.