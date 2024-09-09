---
    layout: publication
    title: "SHREWD: Semantic Hierarchy-based Relational Embeddings for Weakly-supervised Deep Hashing"
    authors: Arponen Heikki, Bishop Tom E
    conference: Arxiv
    year: 2019
    bibkey: arponen2019shrewd
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1908.05602"}
    tags: ['ARXIV', 'Supervised', 'Weakly Supervised']
    ---
    Using class labels to represent class similarity is a typical approach to training deep hashing systems for retrieval; samples from the same or different classes take binary 1 or 0 similarity values. This similarity does not model the full rich knowledge of semantic relations that may be present between data points. In this work we build upon the idea of using semantic hierarchies to form distance metrics between all available sample labels; for example cat to dog has a smaller distance than cat to guitar. We combine this type of semantic distance into a loss function to promote similar distances between the deep neural network embeddings. We also introduce an empirical Kullback-Leibler divergence loss term to promote binarization and uniformity of the embeddings. We test the resulting SHREWD method and demonstrate improvements in hierarchical retrieval scores using compact, binary hash codes instead of real valued ones, and show that in a weakly supervised hashing setting we are able to learn competitively without explicitly relying on class labels, but instead on similarities between labels.