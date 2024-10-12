---
layout: publication
title: Data-dependent LSH For The Earth Movers Distance
authors: Jayaram Rajesh, Waingarten Erik, Zhang Tian
conference: "Arxiv"
year: 2024
bibkey: jayaram2024data
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2403.05041"}
tags: ['ARXIV', 'Independent', 'LSH']
---
We give new data-dependent locality sensitive hashing schemes (LSH) for the Earth Mover's Distance (\\(\mathsf&#123;EMD&#125;\\)), and as a result, improve the best approximation for nearest neighbor search under \\(\mathsf&#123;EMD&#125;\\) by a quadratic factor. Here, the metric \\(\mathsf&#123;EMD&#125;_s(\mathbb&#123;R&#125;^d,\ell_p)\\) consists of sets of \\(s\\) vectors in \\(\mathbb&#123;R&#125;^d\\), and for any two sets \\(x,y\\) of \\(s\\) vectors the distance \\(\mathsf&#123;EMD&#125;(x,y)\\) is the minimum cost of a perfect matching between \\(x,y\\), where the cost of matching two vectors is their \\(\ell_p\\) distance. Previously, Andoni, Indyk, and Krauthgamer gave a (data-independent) locality-sensitive hashing scheme for \\(\mathsf&#123;EMD&#125;_s(\mathbb&#123;R&#125;^d,\ell_p)\\) when \\(p \in [1,2]\\) with approximation \\(O(\log^2 s)\\). By being data-dependent, we improve the approximation to \\(\tilde&#123;O&#125;(\log s)\\). Our main technical contribution is to show that for any distribution \\(\mu\\) supported on the metric \\(\mathsf&#123;EMD&#125;_s(\mathbb&#123;R&#125;^d, \ell_p)\\), there exists a data-dependent LSH for dense regions of \\(\mu\\) which achieves approximation \\(\tilde&#123;O&#125;(\log s)\\), and that the data-independent LSH actually achieves a \\(\tilde&#123;O&#125;(\log s)\\)-approximation outside of those dense regions. Finally, we show how to glue together these two hashing schemes without any additional loss in the approximation. Beyond nearest neighbor search, our data-dependent LSH also gives optimal (distributional) sketches for the Earth Mover's Distance. By known sketching lower bounds, this implies that our LSH is optimal (up to $\mathrm{poly}(\log \log s)$ factors) among those that collide close points with constant probability.
