# Security Policy

## Supported versions

This repository is primarily an educational project. Security fixes are applied to the latest version on the default branch.

## Reporting a vulnerability

Please do not disclose a suspected vulnerability in a public issue.

Report the problem privately to the repository maintainer through GitHub's private vulnerability reporting feature when available. Include:

- the affected file, component, or dependency;
- steps required to reproduce the issue;
- the potential impact;
- any suggested mitigation;
- whether the issue affects example code, package utilities, CI, or documentation.

Do not include credentials, private datasets, access tokens, or personal information in the report.

## Scope

Relevant reports include:

- unsafe handling of user-supplied paths or files;
- dependency vulnerabilities affecting normal project use;
- accidental exposure of secrets or private data;
- insecure examples that could encourage unsafe production deployment;
- CI or packaging configurations that allow unintended code execution.

Model accuracy, algorithm limitations, false positives, and false negatives are normally correctness or documentation issues rather than security vulnerabilities. These may be reported through the regular issue tracker without confidential data.

## Response expectations

The maintainer will review a complete report, assess severity, and determine an appropriate fix or documentation update. Please allow reasonable time for investigation before any public disclosure.
