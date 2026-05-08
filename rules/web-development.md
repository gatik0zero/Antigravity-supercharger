---
trigger: glob
globs: ["*.html", "*.css", "*.js", "*.jsx", "*.tsx", "*.vue", "*.svelte"]
---

# Web Development Rules

## HTML
- Use semantic HTML5 elements (`header`, `nav`, `main`, `article`, `section`, `footer`)
- Every page must have exactly one `<h1>` with proper heading hierarchy
- Include `alt` text on all images
- Add `lang` attribute to `<html>` tag
- Use `<button>` for actions, `<a>` for navigation

## CSS
- Mobile-first responsive design (min-width media queries)
- Use CSS custom properties for theming (colors, spacing, typography)
- Avoid `!important` — fix specificity issues instead
- Use flexbox/grid over float-based layouts
- Ensure text contrast meets WCAG AA (4.5:1 ratio minimum)
- Add smooth transitions for interactive elements (150-300ms)

## JavaScript
- Use modern ES6+ features (const/let, arrow functions, template literals, destructuring)
- Prefer `async/await` over `.then()` chains
- Use event delegation for dynamic elements
- Debounce/throttle expensive event handlers (scroll, resize, input)
- Lazy-load images and heavy resources

## Performance
- Minimize DOM manipulation — batch updates
- Use `requestAnimationFrame` for animations
- Compress images (WebP preferred)
- Defer non-critical JavaScript
- Target < 3s initial load time

## Accessibility (a11y)
- All interactive elements must be keyboard-accessible
- Use ARIA labels when semantic HTML isn't sufficient
- Ensure focus indicators are visible
- Test with screen reader flow in mind
- Provide skip-to-content links for navigation-heavy pages

## SEO
- Descriptive `<title>` tags per page
- Meta descriptions (150-160 characters)
- Proper Open Graph and Twitter Card tags
- Structured data (JSON-LD) where applicable
- Clean URL structure
