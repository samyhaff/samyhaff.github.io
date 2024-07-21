+++
title = "Obsidian: a private and flexible note-taking tool"
date = 2024-07-21

[taxonomies]
categories = ["programming", "tools"]
+++

Here I will write about my journey using Obsidian to organize my thoughts and notes.

<!-- more -->

## Why Obsidian?

I used to write my notes using Apple Notes, which allowed to sync them across my devices and was easy to use, with the features I needed.
However, I wanted to have more control over my notes, to be able to load them in any editor and automate some tasks.
This is why I decided to switch to [Obsidian](https://obsidian.md), as it stood out to me as the best tool choice for my needs, for the following reasons:

* Notes are nothing more than markdown files
* The notes are stored locally and can be synced with a cloud service of choice
* It is free
* It has a large community and many plugins available
* It has available on all major platforms
* It is highly configurable and can be customized to fit my needs
* It has a powerful search and linking system that allows for the creation of a personal knowledge base

So far, my only complaint is that the apps are not open source, but I am satisfied with the fact that my notes are fully under my control.

## My Gym Log setup

This particular project is the reason I wanted to move away from Apple Notes. I am used to writing down the weights I lift for each exercise in order to track my progress and
select the right weights. I wanted to be able to quickly log my weights during my workout and have them automatically update a note to keep track of my progress
and workout schedule.

This setup relies on two community plugins:

* The [dataview](https://blacksmithgu.github.io/obsidian-dataview/) plugin allows for a live indexing and querying of notes
* The [QuickAdd](https://github.com/chhoumann/quickadd) which allows for the quick creation of notes from templates.

So, I created a `Upper body` and a `Lower body` templates, along with the two corresponding QuickAdd options, which I use to create a new unique note for each workout, with the title being
the date of the workout. For example, this is what the `Upper body` template looks like:

```markdown
#upper
dumbbells-bench::
lat-pulldown::
shoulder-raises::
lat-raises::
biceps-curl::
triceps-pushdown::
row::
hammer-curl::
```

I also have a `gym` note where I keep track of the weights I lift for each exercise. I use the following query to display the last four upper body workout weights in a table:

```sql
TABLE
dumbbells-bench AS Bench, lat-pulldown AS "Lat pulldown", shoulder-raises as "Shoulder raises", lat-raises AS "Lat raises", biceps-curl AS "Biceps curl", hammer-curl AS "Hammer curl", triceps-pushdown AS "Triceps pushdown", row as "Row"
FROM #upper and "gym"
LIMIT 4
```

And this one to display a calendar:

```sql
CALENDAR file.ctime
FROM #upper AND "gym"
```

I plan on extending this to include a graph of my progress, by either finding a plugin that can do this or writing my own script to generate the graph from the markdown files.

## Resources

- [Hack your brain with Obsidian.md](https://www.youtube.com/watch?v=DbsAQSIKQXk)
- [dataview documentation](https://blacksmithgu.github.io/obsidian-dataview/)
