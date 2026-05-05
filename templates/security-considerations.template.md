# Security Considerations

## Source Security-Relevant Behavior
- [ ] [authentication flow, authorization check, input filtering, secret handling, etc.]

## Authentication / Authorization
- [ ] Authentication mechanism: [placeholder]
- [ ] Authorization model: [placeholder]
- [ ] Tenant or ownership rules: [placeholder]

## Data Exposure Risks
- [ ] [PII / secrets / internal data / over-sharing risk]
- [ ] [transport or storage exposure risk]

## Input Validation
- [ ] [validation rule]
- [ ] [missing validation concern]

## Output Encoding
- [ ] [XSS / injection / serialization concern]
- [ ] [safe encoding or escaping requirement]

## Secrets / Credentials
- [ ] [secret source or handling concern]
- [ ] [rotation / storage / redaction note]

## External Integrations
- [ ] [API, webhook, email, storage, payment, or third-party dependency]
- [ ] [trust / failure / retry note]

## File Uploads / Downloads
- [ ] [upload restriction or download access rule]
- [ ] [content-type / size / path traversal note]

## Webhooks / Callbacks
- [ ] [signature / verification / idempotency requirement]
- [ ] [replay protection or callback validation note]

## Background Jobs
- [ ] [job data sensitivity]
- [ ] [retry / dead-letter / idempotency note]

## Abuse Cases
- [ ] [rate limiting / enumeration / brute force / replay / abuse concern]

## Required Security Review
- [ ] Validate the reconstructed behavior against the target security model.
- [ ] Confirm sensitive data handling before planning.
- [ ] Verify trust boundaries after architecture mapping.

## Recommended Next Command
- `/speckit.security-review.audit` before planning
- `/speckit.security-review.branch` only after implementation branch changes exist
