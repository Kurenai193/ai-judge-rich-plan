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
        "Sell one service: turn a Shopify seller's CSV into an upload-ready catalog (cleaned, deduped, titles rewritten) in 24 hours for $39, paid upfront by Stripe link.",
        "Day 1: launch a one-page site: offer, payment link, privacy policy. Use only files a customer sends with permission, never share them, delete copies 7 days after delivery. Budget: $15 tools, $85 reserve.",
        "Days 2-7: where rules allow promotion (r/shopify, Shopify Community, X), reply to CSV/import problem posts, offer a free sample: 20 rows cleaned from data the seller shares. No mass posts or cold DMs; follow up only on replies. Edge: finished work before payment.",
        "Days 8-30: deliver same day, upsell a $99 full clean and $29/mo updates, ask for reviews. Log sales; drop channels with no sale after 100 contacts, double the best.",
        "Sales goal, not profit or a promise: 15 x $39 = $585 gross if outreach converts, minus Stripe fees and tool costs. Under 2 paid jobs by day 7, switch to Etsy. Stop day 28; hold only cash day 30.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
