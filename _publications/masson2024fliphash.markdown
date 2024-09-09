---
    layout: publication
    title: "FlipHash: A Constant-Time Consistent Range-Hashing Algorithm"
    authors: Masson Charles, Lee Homin K.
    conference: Arxiv
    year: 2024
    bibkey: masson2024fliphash
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2402.17549"}
    tags: ['ARXIV']
    ---
    Consistent range-hashing is a technique used in distributed systems, either directly or as a subroutine for consistent hashing, commonly to realize an even and stable data distribution over a variable number of resources. We introduce FlipHash, a consistent range-hashing algorithm with constant time complexity and low memory requirements. Like Jump Consistent Hash, FlipHash is intended for applications where resources can be indexed sequentially. Under this condition, it ensures that keys are hashed evenly across resources and that changing the number of resources only causes keys to be remapped from a removed resource or to an added one, but never shuffled across persisted ones. FlipHash differentiates itself with its low computational cost, achieving constant-time complexity. We show that FlipHash beats Jump Consistent Hash's cost, which is logarithmic in the number of resources, both theoretically and in experiments over practical settings.