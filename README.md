# Customer repo (from tekbrokr-customer-template)

Holds only what is specific to this customer: `tekbrokr.toml`, custom adapters in `adapters/`,
and the handover docs. The standard functionality comes from the pinned `tekbrokr-enterprise`
core. **Do not copy core code into this repo.** If the core is missing something, fix it in the core.

## Onboarding a new customer
1. Create the repo from this template (private). Set `[customer] id` and `[brand]`.
2. Choose adapters for connectors, object store, warehouse and auth (`docs/ADAPTERS` in the core
   explains how to write one). Keep customer-only adapters in `adapters/`.
3. Copy `.env.example` to `.env`, then set real values; store them in the deployment platform's
   secret store. Generate `PSEUDONYM_KEY` once and never rotate it.
4. Define the customer's KPIs and targets in `tekbrokr.toml`. Agree each definition with the customer.
5. `tekbrokr-enterprise doctor`, then `ingest --day <yesterday>`, then `report`.
6. Schedule `ingest` followed by `report` daily. Alert on a non-zero exit code.
7. Fill in `docs/HANDOVER.md` and run the handover session (see it for the checklist).

## Try it locally
```
pip install -r requirements.txt   # or: pip install -e ../tekbrokr_enterprise
export ADMIN_TOKEN=dev PSEUDONYM_KEY=$(python -c "import secrets;print(secrets.token_hex(32))")
tekbrokr-enterprise doctor
tekbrokr-enterprise ingest --day 2026-10-01
tekbrokr-enterprise report --day 2026-10-01
```

## Upgrading the core
See `docs/UPGRADING.md`.
