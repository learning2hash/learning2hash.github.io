---
    layout: publication
    title: "Data-Dependent LSH for the Earth Mover's Distance"
    authors: Jayaram Rajesh, Waingarten Erik, Zhang Tian
    conference: Arxiv
    year: 2024
    bibkey: jayaram2024data
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2403.05041"}
    tags: ['ARXIV', 'LSH']
    ---
    We give new data-dependent locality sensitive hashing schemes (LSH) for the Earth Mover's Distance ($\mathsf\{EMD\}$), and as a result, improve the best approximation for nearest neighbor search under $\mathsf\{EMD\}$ by a quadratic factor. Here, the metric $\mathsf\{EMD\}_s(\mathbb\{R\}^d,\ell_p)$ consists of sets of $s$ vectors in $\mathbb\{R\}^d$, and for any two sets $x,y$ of $s$ vectors the distance $\mathsf\{EMD\}(x,y)$ is the minimum cost of a perfect matching between $x,y$, where the cost of matching two vectors is their $\ell_p$ distance. Previously, Andoni, Indyk, and Krauthgamer gave a (data-independent) locality-sensitive hashing scheme for $\mathsf\{EMD\}_s(\mathbb\{R\}^d,\ell_p)$ when $p \in [1,2]$ with approximation $O(\log^2 s)$. By being data-dependent, we improve the approximation to $\tilde\{O\}(\log s)$. Our main technical contribution is to show that for any distribution $\mu$ supported on the metric $\mathsf\{EMD\}_s(\mathbb\{R\}^d, \ell_p)$, there exists a data-dependent LSH for dense regions of $\mu$ which achieves approximation $\tilde\{O\}(\log s)$, and that the data-independent LSH actually achieves a $\tilde\{O\}(\log s)$-approximation outside of those dense regions. Finally, we show how to "glue" together these two hashing schemes without any additional loss in the approximation. Beyond nearest neighbor search, our data-dependent LSH also gives optimal (distributional) sketches for the Earth Mover's Distance. By known sketching lower bounds, this implies that our LSH is optimal (up to $\mathrm\{poly\}(\log \log s)$ factors) among those that collide close points with constant probability.