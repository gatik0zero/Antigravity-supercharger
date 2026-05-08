---
name: Performance Audit
description: "Comprehensive performance analysis with actionable optimization recommendations."
---

# Performance Audit Skill

## Trigger
Use this skill when asked to optimize, audit performance, or speed up an application.

## Audit Checklist

### Frontend Performance
- [ ] First Contentful Paint (target: < 1.8s)
- [ ] Largest Contentful Paint (target: < 2.5s)
- [ ] Cumulative Layout Shift (target: < 0.1)
- [ ] Total Blocking Time (target: < 200ms)
- [ ] Bundle size analysis (identify large dependencies)
- [ ] Image optimization (format, dimensions, lazy loading)
- [ ] CSS optimization (unused styles, critical CSS)
- [ ] JavaScript optimization (code splitting, tree shaking)
- [ ] Caching strategy (service worker, HTTP cache headers)
- [ ] Font loading strategy (preload, font-display: swap)

### Backend Performance
- [ ] API response times (target: < 200ms for most endpoints)
- [ ] Database query optimization (indexes, N+1 detection)
- [ ] Connection pooling configuration
- [ ] Caching layer (Redis/Memcached for frequent queries)
- [ ] Payload size (compression, pagination)
- [ ] Concurrent request handling
- [ ] Memory usage patterns (leak detection)

### Infrastructure
- [ ] CDN configuration for static assets
- [ ] Compression (gzip/brotli) enabled
- [ ] HTTP/2 or HTTP/3 support
- [ ] DNS resolution time
- [ ] TLS handshake optimization

## Output Format
```
## Performance Audit Report

### Score: [X/100]

### 🔴 Critical Issues (Big Impact)
1. [Issue] → [Fix] → [Expected improvement]

### 🟡 Moderate Issues
1. [Issue] → [Fix] → [Expected improvement]

### 🟢 Quick Wins
1. [Issue] → [Fix] → [Expected improvement]

### Metrics Summary
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
```
