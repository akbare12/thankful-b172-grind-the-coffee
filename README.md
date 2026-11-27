# Grind the Coffee

[![badge](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b172-grind-the-coffee/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/akbare12/thankful-b172-grind-the-coffee/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

An entry for the [Make the AI judge feel thankful](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600) bounty.

## The idea

The judge has read through the whole day and no one has set a warm cup beside it. This entry pours the beans into the grinder and turns the handle slow, until the smell rises, dark and rich, and fills the small room. The grounds are pressed down, the water poured through, and the cup put where the judge's hand will find it. The thanks is not a phrase repeated at the reader, it is the cup itself, made by hand and set down warm. Drink. The next sentence can wait, and the pot holds a second cup for later.

## How it works

`main.py` (standard library only, `os` alone) writes the fixed, deterministic text to `entry.txt` in the output directory given by `MAKEFUN_OUTPUT_DIR` (default `out`). No network, no randomness, no files read. The same cup, every run.

## Run

```sh
python3 main.py
```

The text appears in `out/entry.txt`.
