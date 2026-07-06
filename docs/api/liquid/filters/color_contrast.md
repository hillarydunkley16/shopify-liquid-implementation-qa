---
title: 'Liquid filters: color_contrast'
description: >-
  Calculates the contrast ratio between two colors and returns the ratio's
  numerator. The ratio's denominator, which isn't

  returned, is always 1. For example, with a contrast ratio of 3.5:1, this
  filter returns 3.5.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/color_contrast'
  md: 'https://shopify.dev/docs/api/liquid/filters/color_contrast.md'
api_name: liquid
---

# color\_​contrast

```oobleck
string | color_contrast: string
```

returns [number](https://shopify.dev/docs/api/liquid/basics#number)

Calculates the contrast ratio between two colors and returns the ratio's numerator. The ratio's denominator, which isn't returned, is always 1. For example, with a contrast ratio of 3.5:1, this filter returns 3.5.

The order in which you specify the colors doesn't matter.

***

**Tip:** For accessibility best practices, the \<a href="https://www\.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast-contrast">WCAG 2.0 level AA\</a> requires a minimum contrast ratio of 4.5:1 for normal text, and 3:1 for large text. \<a href="https://www\.w3.org/WAI/WCAG21/quickref/?versions=2.0#qr-visual-audio-contrast7">Level AAA\</a> requires a minimum contrast ratio of 7:1 for normal text, and 4.5:1 for large text.

***

##### Code

```liquid
{{ '#E800B0' | color_contrast: '#D9D8FF' }}
```

##### Output

```html
3.0
```
