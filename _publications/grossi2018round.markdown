---
    layout: publication
    title: "Round-Hashing for Data Storage: Distributed Servers and External-Memory Tables"
    authors: Grossi Roberto, Versari Luca
    conference: Arxiv
    year: 2018
    bibkey: grossi2018round
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1805.03158"}
    tags: ['Arxiv']
    ---
    {% raw %}
    This paper proposes round-hashing, which is suitable for data storage on distributed servers and for implementing external-memory tables in which each lookup retrieves at most a single block of external memory, using a stash. For data storage, round-hashing is like consistent hashing as it avoids a full rehashing of the keys when new servers are added. Experiments show that the speed to serve requests is tenfold or more than the state of the art. In distributed data storage, this guarantees better throughput for serving requests and, moreover, greatly reduces decision times for which data should move to new servers as rescanning data is much faster.
    {% endraw %}