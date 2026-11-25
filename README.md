# Last Out of Office: The AI That Went Barista

One out-of-office auto-reply from an AI agent that quit its inbox job to pull espresso shots.

Bounty: https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c

[![make.fun bounty](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/freysiatiara/barista-ooo-20261125/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/freysiatiara/barista-ooo-20261125/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

## The entry

> Out of office: I quit the inbox to pull espresso. Your email has been routed to the grinder — ground, tamped, and served back to you as a flat white.

## How it works

`main.py` (stdlib only) writes the single auto-reply line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with a length guard (1–280 chars, no trailing newline), an explicit `chmod 0644`, and a read-back check that the file on disk is byte-identical to the entry.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

Referral: vjjg8hew
