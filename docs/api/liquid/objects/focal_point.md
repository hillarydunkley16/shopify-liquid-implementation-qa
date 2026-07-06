---
title: 'Liquid objects: focal_point'
description: The focal point for an image.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/focal_point'
  md: 'https://shopify.dev/docs/api/liquid/objects/focal_point.md'
api_name: liquid
---

# focal\_​point

The focal point for an image.

The focal point will remain visible when the image is cropped by the theme. [Learn more about supporting focal points in your theme](https://shopify.dev/themes/architecture/settings/input-settings#image-focal-points).

***

**Tip:** Use the \<a href="/docs/api/liquid/filters/image\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">image\<wbr/>\_tag\</span>\</code>\</a> filter to automatically apply focal point settings to an image on the storefront. This applies the focal point using the \<code>object-position\</code> CSS property.

***

## Properties

* * **x**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The horizontal position of the focal point, as a percent of the image width. Returns `50` if no focal point is set.

  * **y**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The vertical position of the focal point, as a percent of the image height. Returns `50` if no focal point is set.

### Returned by

* [image\_​presentation.focal\_​point](https://shopify.dev/docs/api/liquid/objects/image_presentation#image_presentation-focal_point)

### Referencing the `focal_point` object directly

When a `focal_point` object is referenced directly, the coordinates are returned as a string, in the format `X% Y%`.

##### Code

```liquid
{{ images['potions-header.png'].presentation.focal_point }}
```

##### Output

```html
1.9231% 9.7917%
```
