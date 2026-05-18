# Security Notes

AutoPatch AI is defensive and review-focused.

## Safe Use

- Scan only repositories you own or have permission to assess.
- Do not upload or commit private dependency manifests from customer systems.
- Do not commit tokens, `.env` files, package registry credentials, or GitHub credentials.
- Treat generated reports as sensitive if they describe private repositories.

## Current Safety Boundary

The MVP uses an offline demo ruleset and does not call GitHub, package registries, or vulnerability APIs. The PR output is a preview only.

## Before Production

- Add authentication and authorization.
- Add repository access controls.
- Add audit logging.
- Add secret redaction for uploaded manifests.
- Add provider timeouts and rate-limit handling.
