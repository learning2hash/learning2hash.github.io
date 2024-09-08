---
    layout: publication
    title: "Fast Cross-Polytope Locality-Sensitive Hashing"
    authors: Kennedy Christopher, Ward Rachel
    conference: Arxiv
    year: 2016
    bibkey: kennedy2016fast
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1602.06922"}
    tags: ['Arxiv', 'LSH']
    ---
    {% raw %}
    We provide a variant of cross-polytope locality sensitive hashing with respect to angular distance which is provably optimal in asymptotic sensitivity and enjoys $\mathcal{O}(d \ln d )$ hash computation time. Building on a recent result (by Andoni, Indyk, Laarhoven, Razenshteyn, Schmidt, 2015), we show that optimal asymptotic sensitivity for cross-polytope LSH is retained even when the dense Gaussian matrix is replaced by a fast Johnson-Lindenstrauss transform followed by discrete pseudo-rotation, reducing the hash computation time from $\mathcal{O}(d^2)$ to $\mathcal{O}(d \ln d )$. Moreover, our scheme achieves the optimal rate of convergence for sensitivity. By incorporating a low-randomness Johnson-Lindenstrauss transform, our scheme can be modified to require only $\mathcal{O}(\ln^9(d))$ random bits
    {% endraw %}