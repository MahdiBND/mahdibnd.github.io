# relay.py
import httpx2
from urllib.parse import urlparse
from .getenv import get_relay_url

RELAY = get_relay_url()
RELAY_HOST = urlparse(RELAY).netloc


class RelayTransport(httpx2.AsyncHTTPTransport):
    async def handle_async_request(
        self,
        request: httpx2.Request,
    ) -> httpx2.Response:
        original_url = str(request.url)
        parsed = urlparse(original_url)

        target = f"{parsed.scheme}://{parsed.netloc}"

        path = parsed.path or "/"
        if parsed.query:
            path += "?" + parsed.query

        # Optional debug
        print("\n========== RELAY DEBUG ==========")
        print(f"Original URL : {original_url}")
        print(f"Target       : {target}")
        print(f"Path         : {path}")
        print("=================================\n")

        # Rewrite the request to the relay.
        request.url = httpx2.URL(RELAY)

        # Cloudflare Worker host.
        request.headers["host"] = RELAY_HOST

        # Original destination.
        request.headers["x-relay-target"] = target
        request.headers["x-relay-path"] = path

        return await super().handle_async_request(request)


def create_client(timeout: float = 60.0) -> httpx2.AsyncClient:
    """Create an async HTTP client that routes requests through the relay."""
    return httpx2.AsyncClient(
        transport=RelayTransport(),
        timeout=timeout,
        follow_redirects=True,
    )
