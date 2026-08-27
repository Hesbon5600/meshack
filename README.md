# portfolio-meshack

This project runs behind the shared Traefik service at
`/path/to/edge-proxy`.

## Deployment

Start the shared edge service once on the server:

```sh
docker network create edge
docker compose --env-file .env up -d
```

Then deploy this project independently:

```sh
docker compose up -d --build
```

The `proxy` container joins both the private project network and the external
`edge` network. Traefik discovers it through the labels in
`docker-compose.yml`, obtains and renews the certificate for `meshack.tech`,
and forwards HTTPS traffic to nginx on port 81.

Postgres, Redis, and Django are private to this Compose project and do not
publish host ports. Keep the values in `.env` private and set `DEBUG=0` in
production.
