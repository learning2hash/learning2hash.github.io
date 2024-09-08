---
    layout: publication
    title: "Iterative Universal Hash Function Generator for Minhashing"
    authors: de Franca Fabricio Olivetti
    conference: Arxiv
    year: 2014
    bibkey: defranca2014iterative
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1401.6124"}
    tags: ['Arxiv', 'TIP']
    ---
    {% raw %}
    Minhashing is a technique used to estimate the Jaccard Index between two sets by exploiting the probability of collision in a random permutation. In order to speed up the computation, a random permutation can be approximated by using an universal hash function such as the $h_{a,b}$ function proposed by Carter and Wegman. A better estimate of the Jaccard Index can be achieved by using many of these hash functions, created at random. In this paper a new iterative procedure to generate a set of $h_{a,b}$ functions is devised that eliminates the need for a list of random values and avoid the multiplication operation during the calculation. The properties of the generated hash functions remains that of an universal hash function family. This is possible due to the random nature of features occurrence on sparse datasets. Results show that the uniformity of hashing the features is maintaned while obtaining a speed up of up to $1.38$ compared to the traditional approach.
    {% endraw %}