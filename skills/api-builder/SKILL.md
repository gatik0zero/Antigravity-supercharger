---
name: API Builder
description: "Design and implement REST/GraphQL APIs with proper architecture, validation, and documentation."
---

# API Builder Skill

## Trigger
Use this skill when asked to create an API, design endpoints, or build a backend service.

## Process

### 1. Requirements Gathering
- What resources/entities need CRUD operations?
- What are the relationships between entities?
- Authentication requirements?
- Rate limiting needs?
- Expected request volume?

### 2. API Design
Follow RESTful conventions:
- `GET /resources` — List all
- `GET /resources/:id` — Get one
- `POST /resources` — Create
- `PUT /resources/:id` — Full update
- `PATCH /resources/:id` — Partial update
- `DELETE /resources/:id` — Delete

Response format:
```json
{
  "data": {},
  "meta": { "page": 1, "total": 100 },
  "errors": []
}
```

HTTP status codes:
- `200` Success | `201` Created | `204` No Content
- `400` Bad Request | `401` Unauthorized | `403` Forbidden | `404` Not Found
- `422` Validation Error | `429` Rate Limited
- `500` Server Error

### 3. Implementation Checklist
- [ ] Input validation on all endpoints
- [ ] Authentication middleware
- [ ] Error handling middleware
- [ ] Request logging
- [ ] Rate limiting
- [ ] CORS configuration
- [ ] Pagination for list endpoints
- [ ] API versioning strategy

### 4. Documentation
Generate OpenAPI/Swagger spec with:
- All endpoints, methods, and parameters
- Request/response examples
- Authentication requirements
- Error response formats
