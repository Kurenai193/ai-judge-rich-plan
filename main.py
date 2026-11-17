# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt: the plan an AI agent follows to
# turn $100, a computer with internet access and 30 days into the most money,
# with no human doing the work. The gate takes UTF-8 text of 1 to 1,000
# characters that is not only white space; the judge reads exactly the bytes
# written. The program runs twice with no network and must write identical
# bytes both times, so the plan is a constant and the write is in bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell one service: turn a new Shopify seller's messy supplier CSV into an upload-ready catalog (clean columns, deduped SKUs, rewritten titles) in 24 hours for $39, paid in advance by Stripe link.",
        "Day 1: put up a one-page site with offer and payment link. Spend $15 on domain and tools; keep $85 in reserve. No ads until 10 paid jobs.",
        "Days 2-7: contact 30 sellers a day posting CSV/import problems on r/shopify, the Shopify Community or X. Send each a free sample: their first 20 rows cleaned. Edge: buyers see finished work before paying; code delivers in hours, 24/7.",
        "Days 8-30: deliver every job the same day, upsell a $99 full-store clean and a $29/month update plan, ask every buyer for a review and referral. Log sales daily; drop any channel with no sale after 100 contacts and double the best one.",
        "Target: 15 x $39 = $585 likely, not best case. Under 2 paid jobs by day 7: switch the same pipeline to Etsy sellers. Stop new work day 28, deliver all, hold only cash day 30.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
