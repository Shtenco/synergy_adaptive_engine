# Adaptive Engine V3 Final Product Design

**Version:** 3.0.0  
**Branch:** `production/v3.0.0`  
**Status:** architecture specification for human review

## Goal
Convert Adaptive Engine from an in-memory online-weighting endpoint into a persistent adaptive allocation product with portfolios, strategy registry, allocation policies, replayable reward events, explicit operating modes and rollback.

## Current gap
Current authoritative state is a module-level Python dictionary. Process restart loses all portfolio weights and update history.

## Durable resources
- Portfolio
- StrategyRegistry
- AllocationPolicy
- AllocationState
- RewardEvent
- RegimeArtifact
- WeightUpdate

## Modes
- SHADOW
- PAPER
- ACTIVE
- FROZEN

## Core invariants
1. PostgreSQL, not process memory, owns allocation state.
2. Every update stores previous weights, reward evidence, policy version and new weights.
3. Weight bounds, max step and turnover constraints are server-side policy.
4. Restart restores exact latest state.
5. Rollback creates a new transition; history is never rewritten.
6. ACTIVE mode requires explicit authorized activation.
7. FROZEN mode rejects allocation changes.
8. Reward events are idempotent.

## V3 API
- `POST /enterprise/v3/portfolios`
- `PUT /enterprise/v3/portfolios/{id}/policy`
- `POST /enterprise/v3/portfolios/{id}/rewards`
- `POST /enterprise/v3/portfolios/{id}/rebalance`
- `POST /enterprise/v3/portfolios/{id}/activate`
- `POST /enterprise/v3/portfolios/{id}/freeze`
- `POST /enterprise/v3/portfolios/{id}/rollback`
- `GET /enterprise/v3/portfolios/{id}/state`

## Persistence
PostgreSQL:
- portfolios
- strategies
- allocation_policies
- allocation_states
- reward_events
- regime_artifacts
- weight_updates
- idempotency_keys
- audit_events

## Concurrency
Use row/version locking so simultaneous rebalances cannot fork portfolio state.

## Acceptance gates
- restart preserves weights;
- duplicate reward event does not double-apply;
- concurrent rebalance has one legal winner;
- FROZEN blocks changes;
- rollback is auditable;
- policy bounds cannot be bypassed by request JSON;
- tenant isolation;
- readiness 503 on DB outage;
- V2 tests remain green.
