---
    layout: publication
    title: "JumpBackHash: Say Goodbye to the Modulo Operation to Distribute Keys Uniformly to Buckets"
    authors: Ertl Otmar
    conference: Arxiv
    year: 2024
    bibkey: ertl2024jumpbackhash
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2403.18682"}
    tags: ['Arxiv']
    ---
    The distribution of keys to a given number of buckets is a fundamental task in distributed data processing and storage. A simple, fast, and therefore popular approach is to map the hash values of keys to buckets based on the remainder after dividing by the number of buckets. Unfortunately, these mappings are not stable when the number of buckets changes, which can lead to severe spikes in system resource utilization, such as network or database requests. Consistent hash algorithms can minimize remappings, but are either significantly slower than the modulo-based approach, require floating-point arithmetic, or are based on a family of hash functions rarely available in standard libraries. This paper introduces JumpBackHash, which uses only integer arithmetic and a standard pseudorandom generator. Due to its speed and simple implementation, it can safely replace the modulo-based approach to improve assignment and system stability. A production-ready Java implementation of JumpBackHash has been released as part of the Hash4j open source library.