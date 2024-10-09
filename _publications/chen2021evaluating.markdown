---
layout: publication
title: Evaluating Large Language Models Trained On Code
authors: Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob Mcgrew, Dario Amodei, Sam Mccandlish, Ilya Sutskever, Wojciech Zaremba
conference: "Arxiv"
year: 2021
bibkey: chen2021evaluating
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2107.03374v2"}
tags: ['ARXIV']
---
We introduce Codex a GPT language model fine-tuned on publicly available code from GitHub and study its Python code-writing capabilities. A distinct production version of Codex powers GitHub Copilot. On HumanEval a new evaluation set we release to measure functional correctness for synthesizing programs from docstrings our model solves 28.837; of the problems while GPT-3 solves 037; and GPT-J solves 11.437;. Furthermore we find that repeated sampling from the model is a surprisingly effective strategy for producing working solutions to difficult prompts. Using this method we solve 70.237; of our problems with 100 samples per problem. Careful investigation of our model reveals its limitations including difficulty with docstrings describing long chains of operations and with binding operations to variables. Finally we discuss the potential broader impacts of deploying powerful code generation technologies covering safety security and economics.
