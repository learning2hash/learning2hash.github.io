---
layout: default
title: A Primer on Machine Learning Models for Hashing-Based Approximate Nearest Neighbour Search
comments: true
---
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>

# A Living Literature Review of Learning-to-Hash for Nearest Neighbour Search

<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/learning2hash/learning2hash.github.io" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star learning2hash/learning2hash.github.io on GitHub">Star</a>
<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/learning2hash" data-size="large" data-show-count="true" aria-label="Follow @learning2hash on GitHub">Follow @learning2hash</a>
<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<li class="linkedin">
      <a href="https://www.linkedin.com/shareArticle?mini=true&url={{ page.url | replace:'index.html','' | prepend: site.baseurl | prepend: site.url | uri_escape}}&title={{ page.title | default:"" | uri_escape}}" target="_blank">
        {% include social/share-icon-linkedin.svg %}
      </a>
    </li>

### Learning-to-Hash: Overview

With [Jeff Dean's](https://twitter.com/jeffdean/status/1063679694283857920?lang=en) recent keynote at [NeurIPS 2018](https://nips.cc/Conferences/2018), learned [index structures](https://dl.acm.org/citation.cfm?id=3196909) of which learning-to-hash (hash function learning) is an important sub-field, are gaining much more prominence in the research literature and in [industry](http://www.sysml.cc/doc/2018/43.pdf). [SageDB](https://ai.google/research/pubs/pub47669) sketches the vision of a future in which a data processing system will be highly tuned to the distribution of the data via machine learning bringing about significant savings in storage, memory and time. 

To address these exciting advances in hash function learning, we have put together this website to help researchers learn about, share and more easily discover recent work in the field. Learning2hash is a *living literature review* that allows the reader to explore models in the field following a [taxonomy](\base-taxonomy) based on the fundamental model properties. New models can be added to this website by anyone simply by making a GitHub pull request [see *Contributing* below](contributing.html). Select ["All Papers"](https://learning2hash.github.io/papers.html) on the right-hand menu to get started.

### Browse Papers by Tag

{% assign rawtags = Array.new %}
{% for publication in site.publications %}
  {% assign ttags = publication.tags  %}  
  {% assign rawtags = rawtags | concat: ttags %}  
{% endfor %}
{% assign rawtags = rawtags | uniq | sort %}
{% for tag in rawtags %}<tag><a href="/tags.html#{{ tag }}">{{ tag }}</a></tag> {% endfor %}

### Background

*[Nearest neighbour search](https://en.wikipedia.org/wiki/Nearest_neighbor_search)* is the problem of finding the most similar data-points to a query in a large database of data-points, and is a fundamental operation that has found wide applicability in many fields, from Bioinformatics, through to Natural Language Processing (NLP) and Computer Vision. Some interesting application areas include:

* [Detecting and Tracking Interesting Events on Social Media](https://www.aclweb.org/anthology/P14-5007): a real-time system incorporating LSH to detect and track interesting [social media events](http://seanjmoran.com/pdfs/sigir16_embeddings.pdf) over time.
* [Earthquake Hunting with Efficient Time Series Similarity Search](https://dawn.cs.stanford.edu/2018/09/05/quake/): detecting earthquakes by comparing segments of seismic activity time series. Some nice lessons learnt [here](http://www.vldb.org/pvldb/vol11/p1674-rong.pdf) about applying LSH in real-world applications.
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
