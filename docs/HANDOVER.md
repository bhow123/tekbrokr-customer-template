# Handover pack (fill in per customer)

The aim is that the business can run this without the contractor.

## Systems
| Item | Value |
|---|---|
| Repo / owner | |
| Deployment platform and scheduler | |
| Connectors and who owns each source system | |
| Object store, warehouse, auth provider | |
| Where secrets live and who can rotate them | |
| `PSEUDONYM_KEY` backup location (never rotate) | |

## KPI register
One row per KPI in `tekbrokr.toml`: name, definition in plain English, business owner, source systems, target and who set it.

## Runbooks
- **A daily run failed:** read the log, find the failing connector, check the source system's credentials, rerun `ingest --day <date>` (safe to repeat).
- **A KPI looks wrong:** run `report` and check the "Data quality" section for reconciliation; compare against the source system for that day.
- **Add a user / change a role:** (auth provider steps)
- **Add a connector:** see the core's `docs/ADAPTERS.md`.
- **Data request (access/deletion):** (customer's procedure; see core `seed/` docs for the UK GDPR one)

## Governance
- Who may change a KPI definition or target, and how it is reviewed (pull request on `tekbrokr.toml`).
- Retention policy for raw data and reports.

## Knowledge transfer checklist
- [ ] Walkthrough of the pipeline and report
- [ ] Customer ran an ingest and report themselves
- [ ] Customer rotated the deployment secrets they own
- [ ] Customer added a KPI by themselves
- [ ] Escalation contacts and support terms agreed
