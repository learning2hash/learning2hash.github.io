---
    layout: publication
    title: "On the Optimal Time/Space Tradeoff for Hash Tables"
    authors: Bender Michael A., Farach-Colton Martín, Kuszmaul John, Kuszmaul William, Liu Mingmou
    conference: Arxiv
    year: 2021
    bibkey: bender2021on
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2111.00602"}
    tags: ['Arxiv']
    ---
    For nearly six decades, the central open question in the study of hash tables has been to determine the optimal achievable tradeoff curve between time and space. State-of-the-art hash tables offer the following guarantee: If keys/values are Theta(log n) bits each, then it is possible to achieve constant-time insertions/deletions/queries while wasting only O(loglog n) bits of space per key when compared to the information-theoretic optimum. Even prior to this bound being achieved, the target of O(loglog n) wasted bits per key was known to be a natural end goal, and was proven to be optimal for a number of closely related problems (e.g., stable hashing, dynamic retrieval, and dynamically-resized filters). This paper shows that O(loglog n) wasted bits per key is not the end of the line for hashing. In fact, for any k \in [log* n], it is possible to achieve O(k)-time insertions/deletions, O(1)-time queries, and O(\log^{(k)} n) wasted bits per key (all with high probability in n). This means that, each time we increase insertion/deletion time by an \emph{additive constant}, we reduce the wasted bits per key \emph{exponentially}. We further show that this tradeoff curve is the best achievable by any of a large class of hash tables, including any hash table designed using the current framework for making constant-time hash tables succinct.