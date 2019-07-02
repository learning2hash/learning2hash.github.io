---
layout: default
title: A Primer on Machine Learning Models for Hashing-Based Approximate Nearevst Neighbour Search
comments: true
---

# A Living Literature Review of Learning-to-Hash for Nearest Neighbour Search

### Learning-to-Hash: Overview

With [Jeff Dean's](https://twitter.com/jeffdean/status/1063679694283857920?lang=en) recent keynote at [NeurIPS 2018](https://nips.cc/Conferences/2018), learned [index structures](https://dl.acm.org/citation.cfm?id=3196909) of which learning-to-hash is an important sub-field, are gaining much more prominence in the research literature. We have put together this website to help researchers learn about, share and more easily discover recent work in the field. Learning2hash is a *living literature review* that allows you explore the navigate the models in the field following a [taxonomy](\base-taxonomy) based on the fundamental properties of each model. New models can be added to this website by anyone simply by making a GitHub pull request [see *Contributing* below](contributing.html). Select ["All Papers"](https://learning2hash.github.io/papers.html) on the right-hand menu to get started.

### Background

*[Nearest neighbour search](https://en.wikipedia.org/wiki/Nearest_neighbor_search)* is the problem of finding the most similar data-points to a query in a large database of data-points, and is a fundamental operation that has found wide applicability in many fields, from Bioinformatics, through to Natural Language Processing (NLP) and Computer Vision. Some interesting applications include:

* [Detecting Fraudulent Taxi Rides](https://eng.uber.com/lsh/): Uber has applied LSH to detect rides that are similar based on their spatial properties.
* [Audio Fingerprinting](https://santhoshhari.github.io/Locality-Sensitive-Hashing/) Matching a query snippet of audio to a large database (think Shazam!) can be achieved efficiently by using learning-to-hash methods.
* [Genomics](https://www.ncbi.nlm.nih.gov/pubmed/26006009): Locality sensitive hashing (LSH) is used by Biologists to assemble large genomes and to find genes with similar expression in genomic databases.
* [Image Retrieval](https://ai.google/research/pubs/pub34634): Google applies locality sensitive hashing (LSH) alongside [PageRank](https://en.wikipedia.org/wiki/PageRank) to index planet-scale collections of images.
* [Malware Detection](https://media.kaspersky.com/en/enterprise-security/Kaspersky-Lab-Whitepaper-Machine-Learning.pdf): Developers of anti-viral software use hashcode learning models to quickly match a possibly malign code snippet to a database of known viruses.

A simple way of finding similar data-points would simply be to search through the entire dataset comparing each database data-point to the query data-point, a method known as brute-force search. Unfortunately, for most datasets of practical interest, particularly in the age of big-data and deep learning, this brute-force search (O(N)) is too computationally demanding (excessive compute time) and more efficient search methods are required.

[Learning2hash](https://learning2hash.github.io/papers.html) provides a set of curated, community-driven links to a host of *approximate nearest neighbour search* (ANN) models that permit sublinear-time (O(log N), where N are the number of data-points in the dataset) retrieval of nearest neighbours. Hashing models work by generating similar binary hashcodes for semantically similar data-points (illustrated by the diagram below). These similarity preserving hashcodes can then be used to index the data-points (images, documents etc) into the buckets of a hashtable. Similar data-points should ideally end up in the same bucket of the hash table if we happen to have an effective hash function. This whole process is illustrated in the diagram below:

![Locality Sensitive Hashing (LSH)](/public/media/hashing.png?raw=true "Locality Sensitive 
Hashing (LSH)")

Given a query (e.g. the image of the tiger in the example above), we can search for similar data-points by generating a hashcode for the query and only comparing the query data-point to the data-points that collide with it in the same hashtable bucket (or buckets if we have multiple independent hashtables). The principle here is that the number of data-points in the colliding hash table bucket(s) should be much less than the total number of data-points in the entire dataset, yielding a query time that is substantially improved over a simple brute-force search. The only downside to these models is they might not return the closest nearest neighbour(s) every time (that is, we forgo a degree of accuracy), which is usually an acceptable trade-off in practice. 

Much more introductory material on hashing and learning-to-hash can be found in [*Resources*](resources.html).

This literature review gives a particular focus on recently proposed approximate nearest neighbour search models that improve retrieval effectiveness by learning *task specific* hashcodes that are sensitive to the distribution of the data. All the papers listed in this review website suggest new methods for learning the hash functions to generate more effective similarity preserving hashcodes.

### Contributing

Learning-to-hash is a vibrant research field and is rapidly evolving, particularly with the recent surge in interest in deep neural network-based models. The purpose of this website is to augment static literature reviews with a dynamic website that can be updated by any interested researcher with newly published work in the field, including links to relevant code and datasets. To add a new paper to the website simply create a markdown file and open a pull request in GitHub by following [these instructions for contributing](contributing.html).

{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = https://learning2hash.github.io/index.html;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = learning2hash/index; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://https-learning2hash-github-io-index-html.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
{% endif %}
