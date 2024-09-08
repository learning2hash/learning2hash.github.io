---
    layout: publication
    title: "I/O-Efficient Similarity Join"
    authors: Pagh Rasmus, Pham Ninh, Silvestri Francesco, Stöckel Morten
    conference: Arxiv
    year: 2015
    bibkey: pagh2015io
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1507.00552"}
    tags: ['Arxiv', 'LSH']
    ---
    We present an I/O-efficient algorithm for computing similarity joins based on locality-sensitive hashing (LSH). In contrast to the filtering methods commonly suggested our method has provable sub-quadratic dependency on the data size. Further, in contrast to straightforward implementations of known LSH-based algorithms on external memory, our approach is able to take significant advantage of the available internal memory: Whereas the time complexity of classical algorithms includes a factor of $N^\rho$, where $\rho$ is a parameter of the LSH used, the I/O complexity of our algorithm merely includes a factor $(N/M)^\rho$, where $N$ is the data size and $M$ is the size of internal memory. Our algorithm is randomized and outputs the correct result with high probability. It is a simple, recursive, cache-oblivious procedure, and we believe that it will be useful also in other computational settings such as parallel computation.