---
title: 'Liquid filters: img_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for an image.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/img_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/img_url.md'
api_name: liquid
---

# img\_​url

```oobleck
variable | img_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an image.

You can use the `img_url` filter on the following objects:

* [`article`](https://shopify.dev/docs/api/liquid/objects/article)
* [`collection`](https://shopify.dev/docs/api/liquid/objects/collection)
* [`image`](https://shopify.dev/docs/api/liquid/objects/image)
* [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
* [`product`](https://shopify.dev/docs/api/liquid/objects/product)
* [`variant`](https://shopify.dev/docs/api/liquid/objects/variant)

**Deprecated:**

The `img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

##### Code

```liquid
{{ product | img_url }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

### size

```oobleck
variable | img_url: string
```

The size parameter allows you to specify the dimensions of the image up to a maximum of 5760 x 5760 px. You can specify only the width, only the height, or both, and you can also use the following named sizes:

| Name | Dimensions |
| - | - |
| `pico` | `16x16 px` |
| `icon` | `32x32 px` |
| `thumb` | `50x50 px` |
| `small` | `100x100 px` |
| `compact` | `160x160 px` |
| `medium` | `240x240 px` |
| `large` | `480x480 px` |
| `grande` | `600x600 px` |
| `original` `master` | `1024x1024 px` |

##### Code

```liquid
{{ product | img_url: '480x' }}

{{ product | img_url: 'x480' }}

{{ product | img_url: '480x480' }}

{{ product | img_url: 'large' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_480x.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_480x480.jpg?v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_large.jpg?v=1683744744
```

### crop

```oobleck
variable | img_url: crop: string
```

The `crop` parameter allows you to specify which part of the image to show if the specified dimensions result in an aspect ratio that differs from the original. You can use the following values:

* `top`
* `center`
* `bottom`
* `left`
* `right`

The default value is `center`.

##### Code

```liquid
{{ product | img_url: crop: 'bottom' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

### format

```oobleck
variable | img_url: format: string
```

Specify which file format to use for the image. The valid formats are `pjpg` and `jpg`.

It's not practical to convert a lossy image format, like `jpg`, to a lossless image format, like `png`, so this filter does only the following conversions:

* `png` to `jpg`
* `png` to `pjpg`
* `jpg` to `pjpg`

***

**Note:** Shopify automatically detects which image formats are supported by the client (e.g. \<code>\<span class="PreventFireFoxApplyingGapToWBR">Web\<wbr/>P\</span>\</code>, \<code>AVIF\</code>, etc.) and selects a file format for optimal quality and file size. When a format is specified, Shopify takes into account the features (e.g. progressive, alpha channel) of the specified file format when making the final automatic format selection. To learn more, visit \<a href="https://cdn.shopify.com/">https://cdn.shopify.com/\</a>.

***

##### Code

```liquid
{{ product | img_url: format: 'pjpg' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

### scale

```oobleck
variable | img_url: scale: number
```

Specify the pixel density of the image. The valid densities are 2 and 3.

##### Code

```liquid
{{ product | img_url: scale: 2 }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```
