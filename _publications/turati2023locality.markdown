---
    layout: publication
    title: "Locality-Sensitive Hashing Does Not Guarantee Privacy! Attacks on Google's FLoC and the MinHash Hierarchy System"
    authors: Turati Florian  ETH Zurich, Cotrini Carlos  ETH Zurich, Kubicek Karel  ETH Zurich, Basin David  ETH Zurich
    conference: Arxiv
    year: 2023
    bibkey: turati2023locality
    additional_links:
       - {name: "DOI", url: "10.56553/popets-2023-0101"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2302.13635"}
    tags: ['Graph', 'Arxiv']
    ---
    Recently proposed systems aim at achieving privacy using locality-sensitive hashing. We show how these approaches fail by presenting attacks against two such systems: Google's FLoC proposal for privacy-preserving targeted advertising and the MinHash Hierarchy, a system for processing mobile users' traffic behavior in a privacy-preserving way. Our attacks refute the pre-image resistance, anonymity, and privacy guarantees claimed for these systems. In the case of FLoC, we show how to deanonymize users using Sybil attacks and to reconstruct 10% or more of the browsing history for 30% of its users using Generative Adversarial Networks. We achieve this only analyzing the hashes used by FLoC. For MinHash, we precisely identify the movement of a subset of individuals and, on average, we can limit users' movement to just 10% of the possible geographic area, again using just the hashes. In addition, we refute their differential privacy claims.