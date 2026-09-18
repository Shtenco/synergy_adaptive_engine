# Architecture diagrams — SYNERGY Adaptive Engine

## Enterprise boundary
```mermaid
flowchart TB
  Client[Fund / desk client] --> Gateway[Customer gateway\nOIDC / mTLS / rate limits]
  Gateway --> API[FastAPI enterprise boundary]
  API --> Auth[JWT principal + tenant RBAC]
  Auth --> Core[Product core]
  Core --> Result[Decision / research artifact]
  Result --> Audit[AuditEvent + X-Request-ID]
  Audit --> PG[(PostgreSQL)]
  Audit --> CH[(ClickHouse)]
  API --> Metrics[/enterprise/metrics]
  API --> Health[/enterprise/health]
```

## Request sequence
```mermaid
sequenceDiagram
  participant C as Customer
  participant A as Enterprise API
  participant R as RBAC
  participant P as Product core
  participant U as Audit store
  C->>A: POST /enterprise/v1/adaptive/update
  A->>R: verify tenant + role
  alt unauthorized
    R-->>C: 401 / 403
  else authorized
    R->>P: validated request
    P-->>A: deterministic result
    A->>U: record action + request id
    A-->>C: result + request id
  end
```

Failure policy: authentication failures deny; live gate disabled means no live dispatch; retry/circuit-breaker is bounded; unknown financial side effects are never blindly replayed.
