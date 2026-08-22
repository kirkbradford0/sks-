# PORTABLE HERMES FIELD KIT

Status: PROPOSED / BUILD NEXT
Owner: Kirk + Sparky/Codex + Hermes
Purpose: make Hermes portable across interchangeable Windows/Linux hosts so the machine is an airframe, not the identity.

## Command model

- Kirk = human command authority.
- Sparky/Codex = planning, engineering, review, deployment support.
- Hermes = persistent field runtime.
- SKS = source of truth for mission state, assignments, evidence, and handoff.
- Host computers = replaceable airframes.

## Core rule

Do not create separate personality-bound installs such as Hermes Alpha or Hermes Bravo.

Maintain one canonical Hermes field image on an external SSD. On startup it should:

1. identify the current host;
2. load host-local credentials without copying secrets into SKS;
3. pull/read current SKS mission state;
4. run a health check;
5. announce its host callsign and capabilities;
6. accept the role currently assigned by SKS;
7. execute within that role;
8. write a redacted status/evidence packet back to SKS;
9. preserve a handoff/rollback point before shutdown or migration.

## Swappable-airframe doctrine

A dead or unavailable computer should not kill the operation. Move the external field kit to another compatible host, boot the same runtime, identify the new host, restore mission state, and continue.

The identity belongs to the runtime + SKS state, not the physical computer.

## Initial host roles

Roles are assignments, not permanent identities.

- ALPHA: scout / intake / browser or research lane.
- BRAVO: build / coding / local execution lane.
- HOME: backup / recovery / overflow lane.

SKS may reassign these roles when a host is offline, overloaded, or better suited to another task.

## Sheepdog behavior

The field kit should act as a bounded sheepdog:

- detect whether expected agents/runtimes are actually alive;
- do not claim work is active without a real session/process;
- surface stalled work and orphaned tasks;
- route work to an available compatible host;
- preserve task lineage and evidence;
- never move credentials or secrets through public repositories;
- require human review for credentials, billing, legal, production release, or other high-risk mutations.

## Portable-kit target layout

```text
/HERMES_FIELD_KIT
  /runtime
  /bootstrap
  /health
  /adapters
  /skills
  /cache
  /logs-redacted
  /handoff
  /host-profiles
  README.md
```

Secrets should remain outside this portable source tree or be stored in an encrypted host/local secret store. SKS receives references and redacted status only.

## Build order

1. Define supported host baseline and external-drive filesystem.
2. Create bootstrap script that detects host + OS + dependencies.
3. Add Hermes health check and version check.
4. Add SKS pull/read startup step.
5. Add local credential adapter.
6. Add role assignment loader.
7. Add redacted status packet writer.
8. Test migration from one shop machine to a second machine.
9. Document failure/recovery procedure.
10. Only then automate broader sheepdog routing.

## Definition of done

The field kit passes when the same external drive can move between two approved hosts and, without rebuilding Hermes from scratch, can identify the new machine, start the runtime, read current SKS state, load only that host's authorized secrets, perform a health check, accept an SKS role, and produce a valid redacted status packet.

## Security gate

Never place API keys, Supabase service-role keys, OAuth tokens, SSH private keys, machine passwords, or other credentials in SKS or SKS Skills. Repository visibility must be verified before any sensitive operational material is committed.
