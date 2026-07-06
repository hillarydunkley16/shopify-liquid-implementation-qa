---
title: 'Liquid filters: stylesheet_tag'
description: >-
  Generates an HTML `<link>` tag for a given resource URL. The tag has the
  following parameters:


  | Attribute | Value |

  | --- | --- |

  | `rel` | `stylesheet` |

  | `type` | `text/css` |

  | `media` | `all` |
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/stylesheet_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/stylesheet_tag.md'
api_name: liquid
---

# stylesheet\_​tag

```oobleck
string | stylesheet_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<link>` tag for a given resource URL. The tag has the following parameters:

| Attribute | Value |
| - | - |
| `rel` | `stylesheet` |
| `type` | `text/css` |
| `media` | `all` |

##### Code

```liquid
{{ 'base.css' | asset_url | stylesheet_tag }}
```

##### Output

```html
<link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/base.css?v=88290808517547527771663872409" rel="stylesheet" type="text/css" media="all" />
```

### preload

```oobleck
stylesheet_url | stylesheet_tag: preload: boolean
```

Specify whether the stylesheet should be preloaded.

When `preload` is set to `true`, a resource hint is sent as a [Link header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) with a `rel` value of [`preload`](https://developer.mozilla.org/en-US/docs/Web/HTML/Link_types/preload).

```liquid
Link: <STYLESHEET_URL>; rel=preload; as=style
```

This option doesn't affect the HTML link tag directly.

You should use the `preload` parameter sparingly. For example, consider preloading only render-blocking stylesheets that are needed for initial functionality of the page, such as above-the-fold content. To learn more about resource hints in Shopify themes, refer to [Performance best practices for Shopify themes](https://shopify.dev/themes/best-practices/performance#preload-key-resources-defer-or-avoid-loading-others).
