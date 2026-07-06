---
title: 'Liquid filters: image_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for an image.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/image_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/image_url.md'
api_name: liquid
---

# image\_​url

```oobleck
variable | image_url: width: number, height: number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an image.

You can use the `image_url` filter on the following objects, as well as their `src` property:

* [`article`](https://shopify.dev/docs/api/liquid/objects/article)
* [`collection`](https://shopify.dev/docs/api/liquid/objects/collection)
* [`image`](https://shopify.dev/docs/api/liquid/objects/image)
* [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
* [`product`](https://shopify.dev/docs/api/liquid/objects/product)
* [`variant`](https://shopify.dev/docs/api/liquid/objects/variant)
* [`country`](https://shopify.dev/docs/api/liquid/objects/country)

***

**Caution:** You need to specify either a \<a href="/docs/api/liquid/filters/image\_url#image\_url-width">\<code>width\</code>\</a> or \<a href="/docs/api/liquid/filters/image\_url#image\_url-height">\<code>height\</code>\</a> parameter. If neither are specified, then an error is returned.

***

***

**Note:** Regardless of the specified dimensions, an image can never be resized to be larger than its original dimensions.

***

##### Code

```liquid
{{ product | image_url: width: 450 }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450
```

### width

```oobleck
variable | image_url: width: number
```

Specify the width of the image up to a maximum of `5760px`. If only the width is specified, then the height is automatically calculated based on the image's dimensions.

##### Code

```liquid
{{ product | image_url: width: 450 }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?v=1683744744&width=450
```

### height

```oobleck
variable | image_url: height: number
```

Specify the height of the image up to a maximum of `5760px`. If only the height is specified, then the width is automatically calculated based on the image's dimensions.

##### Code

```liquid
{{ product | image_url: height: 450 }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=450&v=1683744744
```

### crop

```oobleck
variable | image_url: crop: string
```

Specify which part of the image to show if the specified dimensions result in an aspect ratio that differs from the original. You can use the following values:

* `top`
* `center`
* `bottom`
* `left`
* `right`
* `region`

The default value is `center`.

When using the `region` crop mode, the starting point for the crop is defined by `crop_left` and `crop_top` and extends to the `crop_width` and `crop_height`. Optionally, to resize the region extracted by the crop, use the `width` and `height` parameters.

***

**Note:** Country flags are SVG images and can only be cropped if a value for \<code>format\</code> is also provided.

***

##### Code

```liquid
{{ product | image_url: width: 400, height: 400, crop: 'bottom' }}

{{ product | image_url: crop: 'region', crop_left: 32, crop_top: 32, crop_width: 512, crop_height: 512 }}

{{ product | image_url: crop: 'region', width: 100, height: 100, crop_left: 32, crop_top: 32, crop_width: 512, crop_height: 512 }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=bottom&height=400&v=1683744744&width=400

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop_height=512&crop_left=32&crop_top=32&crop_width=512&v=1683744744

//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?crop=region&crop_height=512&crop_left=32&crop_top=32&crop_width=512&height=100&v=1683744744&width=100
```

### format

```oobleck
variable | image_url: format: string
```

Specify which file format to use for the image. The valid formats are `pjpg` and `jpg`.

It's not practical to convert a lossy image format, like `jpg`, to a lossless image format, like `png`, so Shopify can do only the following conversions:

* `png` to `jpg`
* `png` to `pjpg`
* `jpg` to `pjpg`

***

**Note:** Shopify automatically detects which image formats are supported by the client (e.g. \<code>\<span class="PreventFireFoxApplyingGapToWBR">Web\<wbr/>P\</span>\</code>, \<code>AVIF\</code>, etc.) and selects a file format for optimal quality and file size. When a format is specified, Shopify takes into account the features (e.g. progressive, alpha channel) of the specified file format when making the final automatic format selection. To learn more, visit \<a href="https://cdn.shopify.com/">https://cdn.shopify.com/\</a>.

***

##### Code

```liquid
{{ product | image_url: width: 450, format: 'pjpg' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?format=pjpg&v=1683744744&width=450
```

### pad\_color

```oobleck
variable | image_url: pad_color: string
```

Specify a color to pad the image if the specified dimensions result in an aspect ratio that differs from the original. The color must be in hexadecimal format (`hex3` or `hex6`).

##### Code

```liquid
{{ product | image_url: width: 400, height: 400, pad_color: '000' }}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new.jpg?height=400&pad_color=000&v=1683744744&width=400
```
