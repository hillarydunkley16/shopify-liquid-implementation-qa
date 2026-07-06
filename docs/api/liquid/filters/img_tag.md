---
title: 'Liquid filters: img_tag'
description: Generates an HTML `<img>` tag for a given image URL.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/img_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/img_tag.md'
api_name: liquid
---

# img\_​tag

```oobleck
string | img_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<img>` tag for a given image URL.

You can also use the `img_tag` filter on the following objects:

* [`article`](https://shopify.dev/docs/api/liquid/objects/article)
* [`collection`](https://shopify.dev/docs/api/liquid/objects/collection)
* [`image`](https://shopify.dev/docs/api/liquid/objects/image)
* [`line_item`](https://shopify.dev/docs/api/liquid/objects/line_item)
* [`product`](https://shopify.dev/docs/api/liquid/objects/product)
* [`variant`](https://shopify.dev/docs/api/liquid/objects/variant)

**Deprecated:**

The `img_tag` filter has been replaced by [`image_tag`](https://shopify.dev/docs/api/liquid/filters/image_tag).

##### Code

```liquid
{{ product | img_tag }}
```

##### Output

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744" alt="" />
```

### Optional parameters

```oobleck
variable | img_tag: string, string, string
```

The `img_tag` filter accepts 3 unnamed parameters, separated by commas, to specify the `alt` and `class` attributes, and the [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size) of the image. Because the parameters are read in that order, you must include a value for each parameter before the last parameter you want to specify. If you don't want to include a parameter that precedes one that you do want to include, then you can set the value to an empty string.

***

**Note:** The \<code>size\</code> attribute of the \<code>\<span class="PreventFireFoxApplyingGapToWBR">img\<wbr/>\_tag\</span>\</code> filter can\&#39;t be used in conjunction with the \<a href="/docs/api/liquid/filters/img\_url">\<code>\<span class="PreventFireFoxApplyingGapToWBR">img\<wbr/>\_url\</span>\</code> filter\</a>. If both are used, then the \<code>\<span class="PreventFireFoxApplyingGapToWBR">img\<wbr/>\_url\</span>\</code> filter will override the \<code>size\</code> parameter of the \<code>\<span class="PreventFireFoxApplyingGapToWBR">img\<wbr/>\_tag\</span>\</code> filter.

***

##### Code

```liquid
{{ product | img_tag: 'image alt text', '', '450x450' }}
```

##### Output

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_450x450.jpg?v=1683744744" alt="image alt text" class="" />
```
