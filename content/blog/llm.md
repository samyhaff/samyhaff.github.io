+++
title = "Learning about LLMs"
date = 2024-07-01

[taxonomies]
categories = ["NLP", "programming"]
+++

Here I will write about my journey learning about LLMs.

<!-- more -->

## Running LLMs locally

The first thing I was interested in was running pretrained LLMs locally and learning about the tools and libraries available to do so.
I have heard a lot about [llama.cpp](https://github.com/ggerganov/llama.cpp) and [ollama](https://ollama.com) being used to run LLMs on Apple M series chips,
so I wanted to try this out first.

* `llama.cpp` allows for LLM inference in C++ on a variety of hardware and supports many models out of the box.
* `ollama` is built around `llama.cpp`, it is more use-friendly and aims at further optimizing the performance and efficiency of `llama.cpp`. It is the one I chose to use.

Running `ollama serve` starts up a server and `ollama run <model>` runs the specified model.
Different models can be downloaded, imported from [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) files or customized with a prompt.
`GGUF` is a binary format that is used for quick loading and saving of models.
The tool also coffers a REST API to interact with the models and manage them.

### Example usage

This is starting `ollama`, and querying the `llama3` model (downloaded beforehand) with "Why is the sky blue?" as a prompt. The response is returned in JSON format,
with the `response` field containing the generated text.

```bash
ollama serve &
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt":"Why is the sky blue?"
}'
```

If we are only interested in the response, we can use `jq` to extract it:

```bash
 curl -s http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Why is the sky blue?",
  "stream": false
}' | jq '.response'
```

In addition, the reponse also returns a `context` field which can be used to keep a short conversational memory between requests by
[encoding/decoding the history of the conversation](https://stephencowchau.medium.com/ollama-context-at-generate-api-output-what-are-those-numbers-b8cbff140d95).

Now, here is a simple  shell script (vulnerable to JSON injection 🙂) showing how `ollama` can be used to generate text with a prompt:

```bash
#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 \"your prompt here\""
  exit 1
fi

prompt="$1"

response=$(curl -s http://localhost:11434/api/generate -d "{
  \"model\": \"llama3\",
  \"prompt\": \"$prompt\",
  \"stream\": false
}")

echo "$response" | jq '.response'
```

### Example project

Let's use `ollama` to generate git messages.

We can use the following `Modelfile` to create a `llama3` model with a system prompt specifying the goal of the model:

```
FROM llama3

SYSTEM """
Your only goal is to output git commit messages. You will be given git diff outputs and should exclusively return a git commit message which can be piped directly into the git commit command.
Never include notes or remarks on the commit message you generated.
""""
```

The model is then created using `ollama create git -f Modelfile`.

Now we can use the following script to generate git commit messages from staged changes:

```bash
#!/bin/bash

diff_output=$(git diff --cached)

prompt="Write a git commit message given this git diff.\n\nGit Diff:\n${diff_output}"
escaped_prompt=$(echo "$prompt" | jq -Rs .)

response=$(curl -s http://localhost:11434/api/generate -d "{
  \"model\": \"git\",
  \"prompt\": $escaped_prompt,
  \"stream\": false
}")

commit_message=$(echo "$response" | jq -r '.response')
echo "$commit_message" | tee >(pbcopy)
```

## Theory behind LLMs

* [Stanford CS224N](https://web.stanford.edu/class/cs224n/)

### Attention mechanism for RNNs

* [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473)

### Transformer architecture

* [An Introduction to Transformers](https://arxiv.org/abs/2304.10557)
* [Stanford NLP Notes on Self Attention and Transformers](https://web.stanford.edu/class/cs224n/readings/cs224n-self-attention-transformers-2023_draft.pdf)
* [Attention is All You Need](https://arxiv.org/abs/1706.03762)
* [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/)

### Models

* [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) (Encoder-only transformer)
* [Generating Wikipedia by Summarizing Long Sequences](https://arxiv.org/abs/1801.10198) (Decoder-only transformer)
* [Improving Language Understanding by Generative Pretraining](https://gwern.net/doc/www/s3-us-west-2.amazonaws.com/d73fdc5ffa8627bce44dcda2fc012da638ffb158.pdf) (GPT, Decoder-only transformer)
* [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461) (Encoder-decoder transformer)
* [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY)
