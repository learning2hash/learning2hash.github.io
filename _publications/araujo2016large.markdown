---
    layout: publication
    title: "Large-Scale Query-by-Image Video Retrieval Using Bloom Filters"
    authors: Araujo Andre, Chaves Jason, Lakshman Haricharan, Angst Roland, Girod Bernd
    conference: Arxiv
    year: 2016
    bibkey: araujo2016large
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1604.07939"}
    tags: ['Video Retrieval', 'Arxiv']
    ---
    {% raw %}
    We consider the problem of using image queries to retrieve videos from a database. Our focus is on large-scale applications, where it is infeasible to index each database video frame independently. Our main contribution is a framework based on Bloom filters, which can be used to index long video segments, enabling efficient image-to-video comparisons. Using this framework, we investigate several retrieval architectures, by considering different types of aggregation and different functions to encode visual information -- these play a crucial role in achieving high performance. Extensive experiments show that the proposed technique improves mean average precision by 24% on a public dataset, while being 4X faster, compared to the previous state-of-the-art.
    {% endraw %}