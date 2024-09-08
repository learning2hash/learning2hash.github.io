---
    layout: publication
    title: "A Sparse Johnson-Lindenstrauss Transform using Fast Hashing"
    authors: Houen Jakob Bæk Tejs, Thorup Mikkel
    conference: Arxiv
    year: 2023
    bibkey: houen2023a
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2305.03110"}
    tags: ['Arxiv', 'FOCS']
    ---
    The \emph{Sparse Johnson-Lindenstrauss Transform} of Kane and Nelson (SODA 2012) provides a linear dimensionality-reducing map $A \in \mathbb{R}^{m \times u}$ in $\ell_2$ that preserves distances up to distortion of $1 + \varepsilon$ with probability $1 - \delta$, where $m = O(\varepsilon^{-2} \log 1/\delta)$ and each column of $A$ has $O(\varepsilon m)$ non-zero entries. The previous analyses of the Sparse Johnson-Lindenstrauss Transform all assumed access to a $\Omega(\log 1/\delta)$-wise independent hash function. The main contribution of this paper is a more general analysis of the Sparse Johnson-Lindenstrauss Transform with less assumptions on the hash function. We also show that the \emph{Mixed Tabulation hash function} of Dahlgaard, Knudsen, Rotenberg, and Thorup (FOCS 2015) satisfies the conditions of our analysis, thus giving us the first analysis of a Sparse Johnson-Lindenstrauss Transform that works with a practical hash function.