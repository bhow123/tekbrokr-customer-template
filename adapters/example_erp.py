"""Example customer-specific connector. Copy, rename, and point tekbrokr.toml at it:
adapter = "adapters.example_erp:ExampleErpConnector"
If it would help other customers too, move it into a shared adapter package instead."""

import os
from datetime import date
from typing import Any, Dict, Iterable

from tekbrokr_enterprise.interfaces import Connector


class ExampleErpConnector(Connector):
    def fetch(self, day: date) -> Iterable[Dict[str, Any]]:
        token = os.environ["ERP_API_TOKEN"]  # from the environment, never from git
        raise NotImplementedError(f"call the ERP API for {day} using {self.settings.get('base_url')}")
