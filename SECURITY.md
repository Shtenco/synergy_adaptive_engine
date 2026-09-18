# Security policy — SYNERGY Adaptive Engine v2.0.0

## Security invariants
- No production API keys, JWT secrets, DB credentials or broker secrets belong in Git.
- Live execution is disabled by default; `SYNERGY_ALLOW_LIVE_EXECUTION=true` is only one gate and never substitutes for customer approval.
- Production identity should terminate at a customer-controlled OIDC/mTLS/JWKS boundary. The included HS256 path is a reference/test integration.
- Use least-privilege venue credentials; disable withdrawals where supported.
- `X-Request-ID` is correlation evidence, not authentication or a financial idempotency secret.
- Unknown financial side effects must not be blindly retried.
- Risk controls must remain outside mutable strategy/agent logic.

## Data and audit
PostgreSQL is the reference authoritative operational audit store; ClickHouse is an analytical mirror. Define customer retention, encryption, backup, deletion and access policies before production.

## Production checklist
1. Pin release commit and image digest.
2. Use KMS/secret manager; never commit `.env.enterprise`.
3. Terminate TLS at approved ingress/service mesh.
4. Restrict DB and venue network paths.
5. Enable dependency/image/secret scanning.
6. Exercise backup/restore, credential rotation and rollback.
7. Keep live trading disabled until sandbox/paper and bounded canary acceptance passes.

## Disclosure
Do not post credentials, exploits or customer data in public issues. Use GitHub private vulnerability reporting if enabled, otherwise coordinate a private disclosure channel with the owner.

No SOC 2, ISO 27001 or regulatory certification is claimed by this repository.
