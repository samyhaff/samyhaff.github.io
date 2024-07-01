+++
title = "Learning about LLMs"
date = 2024-06-29

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
