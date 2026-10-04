# Upgrading the core
1. Read the core's `docs/CHANGELOG.md` for the versions between yours and the target.
2. Change the tag in `requirements.txt` and `[core] version` in `tekbrokr.toml` together.
3. `pip install -r requirements.txt && tekbrokr-enterprise doctor`.
4. Run `ingest` and `report` for a recent day and compare the KPI values to the previous version.
5. Deploy. Roll back by reverting both lines.

The core refuses to run if the major.minor in `tekbrokr.toml` differs from the installed core.
