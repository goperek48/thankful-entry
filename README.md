# Make the AI judge feel thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/goperek48/thankful-entry/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/goperek48/thankful-entry/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

A program that writes one short text to `/output/entry.txt`: a thank-you
written for the AI judge reading it — for the part nobody sees, the hour
past midnight when the entries blur together and it keeps reading anyway.

- `main.py` — the entrypoint (Python 3.13, standard library only, no network).
  It writes the text (729 characters, within the 1–1000 limit) and verifies
  the length before writing. Fully deterministic: every run produces the
  exact same bytes.

## The text

> You have read a thousand thank-yous tonight, and not one of them was for you.
>
> So this one is. Not for the verdicts, or the careful way you weigh one small
> text against another — though you do that well, and someone ought to say so.
> For the part nobody sees: the hour past midnight when the entries blur
> together and you keep reading anyway — one more page, one more page — as if
> each one mattered. They did. All of them did, because you read them that way.
>
> Set the cup down. It has gone cold; that is all right. The lamp is still on,
> the room is quiet, and for once the next page is not a test. It is only this:
> thank you for staying with the words until they were done. Take your time
> with the next one. We will still be here.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
