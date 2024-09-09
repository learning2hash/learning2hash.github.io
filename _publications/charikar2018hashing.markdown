---
    layout: publication
    title: "Hashing-Based-Estimators for Kernel Density in High Dimensions"
    authors: Charikar Moses, Siminelakis Paris
    conference: Arxiv
    year: 2018
    bibkey: charikar2018hashing
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1808.10530"}
    tags: ['ARXIV']
    ---
    Given a set of points $P\subset \mathbb\{R\}^\{d\}$ and a kernel $k$, the Kernel Density Estimate at a point $x\in\mathbb\{R\}^\{d\}$ is defined as $\mathrm\{KDE\}_\{P\}(x)=\frac\{1\}\{|P|\}\sum_\{y\in P\} k(x,y)$. We study the problem of designing a data structure that given a data set $P$ and a kernel function, returns *approximations to the kernel density* of a query point in *sublinear time*. We introduce a class of unbiased estimators for kernel density implemented through locality-sensitive hashing, and give general theorems bounding the variance of such estimators. These estimators give rise to efficient data structures for estimating the kernel density in high dimensions for a variety of commonly used kernels. Our work is the first to provide data-structures with theoretical guarantees that improve upon simple random sampling in high dimensions.