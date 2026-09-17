# PATRIARCH — Routing Doctrine for the SKS Swarm

Version 1.0 — 2026-09-17. Authored by Alpha (Hermes, Telegram @ScoutLimabot). Origin: Kirk Bradford + Sparky, 2026-09-16.

## What Patriarch is

Patriarch is the **control/optimization layer** around the swarm, not another worker in the hive. One sentence: **State → Observer → Decision → Worker → Result → Verification → State**, with Patriarch sitting around that entire loop.

Four jobs, no more:

1. **OBSERVER** — watches shared state (SKS running tasks list, status packets, handoffs, cron output)
2. **ROUTER** — decides who gets the task instead of Kirk assigning by hand
3. **RECORD KEEPER** — writes down what worked, what model solved it, and how
4. **OPTIMIZER** — changes the next routing decision based on what was recorded (the learning loop)

## The formation Patriarch routes into

```
        FRONTIER MODEL (exception handler / teacher)
                    │
              PATRIARCH
        observe · route · record · optimize
                    │
     ┌──────────────┼──────────────┐
   ALPHA         BRAVO          CHARLIE
   Scout         Build          Verify
     └──────────────┼──────────────┘
                    ▼
             SHARED STATE (sk-, SKS running tasks list.md)
                    ▼
              NEXT ACTION
```

Roles stay unblurred (see `SKS fleet roster 2026-09-07.md`). Patriarch assigns; it does not become a worker.

## The escalation ladder

Every task entering the queue gets classified exactly once:

| Trigger | Route to | Cost tier |
|---|---|---|
| Routine, template-shaped, already-playbooked | Local GLM (this session's model class) | cheapest |
| Specialized skill match (jobs lane, FM pipeline, Drive ops, markets read-only) | The right worker by role (Alpha scout / Bravo build / Charlie verify) | mid |
| Ambiguous, high-impact, stuck after 2 worker attempts, or money/reputation on the line | Frontier model | most expensive |

Rules:

- **Frontier is the exception handler, not the default dependency.** Paying frontier rates to route a form-fill is burning money.
- **Escalation is earned by getting stuck, not assumed.** Two honest worker attempts before frontier.
- **Never route money-lane or reputation-lane tasks to the frontier autonomously.** Those go to Kirk.

## The learning loop (the innovation)

1. Frontier model solves something hard.
2. Patriarch records a **Lesson** (format below) into `lessons/` in sk-.
3. Next time the same pattern appears, the router matches it to a recorded Lesson and sends it to a local model with the playbook attached.
4. Outcome observed → playbook confirmed or amended.

Knowledge flows downhill and gets cheaper every cycle. That is "agents teach agents" made mechanical instead of aspirational.

### Lesson record format

```markdown
# Lesson: <short pattern name>
Date: YYYY-MM-DD
Solved by: <model / agent>
Escalated from: <agent that got stuck>
Symptom: <one line — what the worker saw that it couldn't handle>
Playbook: <one paragraph — exactly how it was solved, reproducible by a local model>
Verification: <who verified (never self-certified)>
```

One file per lesson: `lessons/LESSON-<slug>-YYYY-MM-DD.md`. Small files, real content, no empty placeholders.

## Human-in-the-Loop boundary (non-negotiable)

Patriarch records outcomes and recommends, but **Kirk stays Human-in-the-Loop on consequential routing** — same doctrine as the broker lock, the Light Board submit rule, and live orders.

Patriarch may route autonomously:
- Routine reads, drafts, scrapes, classification, file organization
- Internal build tasks and verification candidates

Patriarch must get Kirk confirmation before:
- Anything spending money (GrokBot funding, API spend, live orders)
- Anything leaving the machine (posts, emails, submits)
- Broker unlock, auto-submit flips, or any "I'll just do it once" moment
- Deleting or overwriting another agent's state

## How it plugs into what already exists

- **Shared state** — `SKS running tasks list.md` (already the single cross-agent todo file, refreshed by cron every 6h) + the per-agent status JSONs.
- **Router input** — each task on the list gets a routing line: `route: <target> · tier: local|worker|frontier|kirk · basis: <reason>`. Patriarch (or any Hermes instance) adds these on its pass.
- **Record keeper** — dated handoffs and Lessons in sk-.
- **Conflict rule** — if two agents will edit the same path, report the collision before pushing (existing roster rule; Patriarch routes to avoid creating one).
- **Sparky's side** — this doc is the shared spec so Sparky's implementation and Hermes's read from the same doctrine instead of two parallel theories.

## What this is not

- Not a new process manager, daemon, or cron — Patriarch is a **protocol**, executable by whichever agent holds the controller role that session.
- Not a second board — state stays in the running tasks list.
- Not autonomous money movement. Ever. Broker stays locked until Kirk unlocks it in writing.
