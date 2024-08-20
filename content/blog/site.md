+++
title = "About this site"
date = 2024-06-30

[taxonomies]
categories = ["Tools"]

[extra]
math = true
+++

This page descrbibes how this site is built. It is a static site generated with [Zola](https://www.getzola.org/). The source code is available on
[GitHub](https://github.com/samyhaff/samyhaff.github.io/tree/master).

<!-- more -->

## Zola

Zola is a static site generator written in Rust. It is fast and consists in a single binary. I chose it because of its simplicity, as I was looking for a minimalistic solution to build my site.
It uses the [Tera](https://keats.github.io/tera/) templating engine and the [Sass](https://sass-lang.com/) CSS preprocessor.
Content is written in Markdown and can be organized in sections and categories.

## Theme

At first, the theme for this site was based on the [after-dark](https://github.com/getzola/after-dark) theme. I made some modifications to the colors and allowed for some additional text to the
index page in my [fork](https://github.com/samyhaff/after-dark). Themes are simply added as git submodules in the `themes` directory.
However, I ended up switching to the [serene](https://github.com/isunjn/serene/blob/latest/USAGE.md) theme which I found to be more aligned with my vision for the site.
It supports dark mode, templates allowing for both a blog and a project page, and $\LaTeX$ rendering using [KaTeX](https://katex.org/).

## Deployment

The site is deployed on [GitHub Pages](https://pages.github.com/). The `gh-pages` branch of the repo is used to host the built site. The `master` branch contains the source code.
The site is built and deployed using the [zola-deploy-action](https://github.com/shalzz/zola-deploy-action) GitHub action.

## Workflow

New content is created by adding a new Markdown file in the `content` directory. The file contains a front matter with the title and date of the post, as well as any taxonomies.
Changes can be previewed locally by running `zola serve` which starts a local server and listens for any changes in the source file, before pushing the changes to the `master` branch
and having the GitHub action build and deploy the site.

## Inspirations

I want sites to be simple, fast to load and free from unnecessary javascript and tracking. I was inspired by various personal and academic sites, as well as:

* [Advent of Code](https://adventofcode.com/)
* [Hackernews](https://news.ycombinator.com/)
* [Luke Smith's site](https://lukesmith.xyz/)
* [Gilles Castel's site](https://castel.dev)
* [Lil'log](https://lilianweng.github.io)
