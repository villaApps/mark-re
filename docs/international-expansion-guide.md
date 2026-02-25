# International Expansion Guide

## Adding a New Market

1. Create market folder in `apps/scrapers/markets/{code}/`
2. Implement scraper using `@register_scraper('{code}')`
3. Add market config to `config/feature-flags.json`
4. Add SAM parameters for region
5. Create tests in `tests/markets/{code}/`

## Compliance Checklist
- [ ] Data residency requirements
- [ ] Local tax rules
- [ ] Legal entity requirements
- [ ] Auction regulations
