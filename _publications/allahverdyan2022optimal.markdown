---
layout: publication
title: Optimal Alphabet For Single Text Compression
authors: Armen E. Allahverdyan, Andranik Khachatryan
conference: Information Sciences
year: 2022
bibkey: allahverdyan2022optimal
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.05234'}]
tags: []
short_authors: Armen E. Allahverdyan, Andranik Khachatryan
---
A text written using symbols from a given alphabet can be compressed using
the Huffman code, which minimizes the length of the encoded text. It is
necessary, however, to employ a text-specific codebook, i.e. the
symbol-codeword dictionary, to decode the original text. Thus, the compression
performance should be evaluated by the full code length, i.e. the length of the
encoded text plus the length of the codebook. We studied several alphabets for
compressing texts -- letters, n-grams of letters, syllables, words, and
phrases. If only sufficiently short texts are retained, an alphabet of letters
or two-grams of letters is optimal. For the majority of Project Gutenberg
texts, the best alphabet (the one that minimizes the full code length) is given
by syllables or words, depending on the representation of the codebook. Letter
3 and 4-grams, having on average comparable length to syllables/words, perform
noticeably worse than syllables or words. Word 2-grams also are never the best
alphabet, on the account of having a very large codebook. We also show that the
codebook representation is important -- switching from a naive representation
to a compact one significantly improves the matters for alphabets with large
number of symbols, most notably the words.
  Thus, meaning-expressing elements of the language (syllables or words)
provide the best compression alphabet.