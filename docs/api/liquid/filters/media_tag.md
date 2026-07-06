---
title: 'Liquid filters: media_tag'
description: Generates an appropriate HTML tag for a given media object.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/media_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/media_tag.md'
api_name: liquid
---

# media\_​tag

```oobleck
media | media_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an appropriate HTML tag for a given media object.

##### Code

```liquid
{% for media in product.media %}
  {{- media | media_tag }}
{% endfor %}
```

##### Data

```json
{
  "product": {
    "media": []
  }
}
```

##### Output

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>

<video playsinline="playsinline" controls="controls" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_small.jpg?v=1655255324"></video>
```

### image\_size

```oobleck
media | media_tag: image_size: string
```

Specify the dimensions of the media's poster image in pixels.

##### Code

```liquid
{% for media in product.media %}
  {{- media | media_tag: image_size: '400x' }}
{% endfor %}
```

##### Data

```json
{
  "product": {
    "media": []
  }
}
```

##### Output

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" image_size="400x" src="https://www.youtube.com/embed/vj01PAffOac?controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>

<video playsinline="playsinline" controls="controls" preload="metadata" aria-label="Potion beats" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_400x.jpg?v=1655255324"><source src="//polinas-potent-potions.myshopify.com/cdn/shop/videos/c/vp/4edc28a708b7405093a927cebe794f1a/4edc28a708b7405093a927cebe794f1a.HD-1080p-7.2Mbps.mp4?v=0" type="video/mp4"><img src="//polinas-potent-potions.myshopify.com/cdn/shop/products/4edc28a708b7405093a927cebe794f1a.thumbnail.0000000_400x.jpg?v=1655255324"></video>
```
