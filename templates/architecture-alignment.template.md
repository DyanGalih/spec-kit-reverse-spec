## Target Stack
- Stack: [placeholder]
- Runtime / framework: [placeholder]
- Persistence / messaging / deployment details: [placeholder]

## Source Components
- [ ] Controller / route / page / CLI / job
- [ ] Service / use case / domain logic
- [ ] Model / schema / migration
- [ ] Integration / adapter / listener
- [ ] Test or doc evidence

## Target Components
- [ ] UI / presentation layer
- [ ] API layer
- [ ] application or domain service layer
- [ ] persistence adapter
- [ ] integration adapter
- [ ] background worker or queue consumer

## Layer Mapping
| Source Layer / Component | Target Layer / Component | Notes |
| --- | --- | --- |
| [placeholder] | [placeholder] | [placeholder] |
| [placeholder] | [placeholder] | [placeholder] |

## Business Logic Placement
- [ ] Business rules stay in the target domain/application layer
- [ ] Framework-specific code remains at the edges
- [ ] Cross-cutting concerns are isolated
- Notes: [placeholder]

## Validation Boundary
- [ ] Input validation happens before domain mutation
- [ ] Invalid requests fail fast with actionable errors
- [ ] Validation responsibilities are explicit
- Notes: [placeholder]

## Persistence Boundary
- [ ] Persistence is isolated behind a repository / adapter / gateway
- [ ] Read and write concerns are clear
- [ ] Transaction or consistency assumptions are recorded
- Notes: [placeholder]

## API / Contract Boundary
- [ ] Public API surface is explicit
- [ ] Request / response shapes are stable
- [ ] Backward-compatibility concerns are recorded
- Notes: [placeholder]

## Async / Background Boundary
- [ ] Long-running work is moved out of request paths
- [ ] Queues / workers / schedulers are mapped explicitly
- [ ] Retries / idempotency assumptions are recorded
- Notes: [placeholder]

## Integration Boundary
- [ ] External services are identified
- [ ] Adapter ownership is clear
- [ ] Side effects are documented
- Notes: [placeholder]

## Security / Trust Boundary
- [ ] Trust boundaries are explicit
- [ ] Authentication / authorization assumptions are recorded
- [ ] Sensitive data handling is noted
- [ ] Security-relevant drift is highlighted
- Notes: [placeholder]

## Architecture Guard Checklist
- [ ] Target components are consistent with the constitution
- [ ] Business logic is not leaking into controllers or UI handlers
- [ ] Persistence and integration boundaries are explicit
- [ ] Async work is not hidden inside request code
- [ ] Security and trust boundaries are documented
- [ ] Required refactors are listed before planning

## Known Drift From Source
- [ ] [difference between source behavior and intended target architecture]
- [ ] [legacy coupling that should not be copied]

## Required Refactor Before Planning
- [ ] [refactor item]
- [ ] [refactor item]
