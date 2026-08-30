# SKS Snowball execution contract

Status: ACTIVE
Approved doctrine source: `ChatGPT-WarBoard Snowball Architecture-20260830-0544.txt`
Primary active queue: Hermes Kanban board `snowball-command`
Human-readable cross-agent cockpit: `SKS single kanban board.md`

## Purpose

Every Hermes worker must read the same assigned card, know its role, leave evidence, and return the same closeout. The card is the unit of truth. The snowball gets heavier, not wider.

## Card access

A dispatched Hermes worker receives these environment values:

- `HERMES_KANBAN_BOARD=snowball-command`
- `HERMES_KANBAN_TASK=<assigned card id>`
- `HERMES_KANBAN_WORKSPACE=<task workspace>`
- `HERMES_PROFILE=<assigned role/profile>`

The worker's first action is `kanban_show()` with no task id. It reads the assigned card, parent handoffs, comments, prior attempts, children, and role (`assignee`).

The worker writes durable evidence through `kanban_comment(...)` during work and finishes with exactly one lifecycle call:

- `kanban_complete(...)` for a verified phase that has a pre-created verifier/reviewer child.
- `kanban_request_review(...)` when the same card requires independent review.
- `kanban_block(...)` when access, credentials, human approval, or another genuine external dependency prevents completion.

A board assignment is not proof of an active worker. Status `running` plus a current run/heartbeat is runtime evidence.

## ACTIVE card rule

`ACTIVE` means Kanban status `running`. `ready` and `todo` are proposed/queued, not ACTIVE.

The installation-wide governor is `kanban.max_in_progress: 3`. At three `running` cards, the dispatcher leaves every proposed successor in `ready`/`todo`; it cannot become ACTIVE until capacity is free.

## Role rule

The task `assignee` is the worker's role identity. Independent certification requires a different real profile or human reviewer than the actor named in `signed_by`.

Planned rotation:

- Alpha — BUILD / ACT
- Bravo — OBSERVE / VERIFY
- Charlie — INSPECT / CHALLENGE

Until those profiles are installed and mapped to real instances, a single `default` profile may execute or report BLOCKED but may not independently certify its own work.

## Snowball closeout

Every run must preserve this exact block in its handoff summary or metadata:

```yaml
card:
target:
action_taken:
evidence:
verification:
result: PASS | FAIL | BLOCKED
artifact_created:
artifact_location:
signed_by:
next_smallest_action:
next_owner:
```

IRON RULE: VERIFY → CERTIFY → NAME → SIGN → NEXT CARD.

## Successor governor

A completed card may propose exactly one bounded successor, never a task tree.

Required successor fields:

```yaml
parent_card:
result:
evidence:
next_action:
why_now:
owner:
risk:
verification_required:
```

Rules:

1. PASS records evidence and proposes the smallest logical next action.
2. FAIL proposes one fix card linked to the failed parent.
3. BLOCKED names the exact failed access or dependency; it does not fabricate a successor execution result.
4. The successor is linked with `parents=[parent_card]` and remains queued when WIP is three.
5. Material priority, architecture, scope, spending, credential, deployment, or publication changes stop for Kirk approval.
6. No agent certifies its own work. If no independent verifier exists, the honest result is BLOCKED or pending verification.

## Primary WarBoard source state

Kirk's canonical source remains the Google Drive folder `WarBoards - Sparky, Kirks caduceus for Hermes`, including `FM-WARBOARD-RUN-001 — Hermes Orchestration Bootstrap — 2026-08-30`. This repository contract is an execution bridge, not a replacement source of truth.

Current verified blocker: the Hermes Google OAuth token is rejected with `invalid_grant`, and the Obsidian note `SLS warboard strike teams/Day one operation snowball/Warboard Exhibit B` is not locally synchronized on this machine. Reauthenticate Drive or restore a readable mirror before claiming the primary source itself is readable here.
