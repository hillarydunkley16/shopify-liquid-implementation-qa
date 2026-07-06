---
title: 'Liquid filters: external_video_tag'
description: >-
  Generates an HTML `<iframe>` tag containing the player for a given external
  video. The input for the `external_video_tag`

  filter can be either a [`media` object](/docs/api/liquid/objects/media) or
  [`external_video_url`](/docs/api/liquid/filters/external_video_url).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/external_video_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/external_video_tag.md'
api_name: liquid
---

# external\_​video\_​tag

```oobleck
variable | external_video_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<iframe>` tag containing the player for a given external video. The input for the `external_video_tag` filter can be either a [`media` object](https://shopify.dev/docs/api/liquid/objects/media) or [`external_video_url`](https://shopify.dev/docs/api/liquid/filters/external_video_url).

If [alt text is set on the video](https://help.shopify.com/en/manual/products/product-media/add-alt-text), then it's included in the `title` attribute of the `<iframe>`. If no alt text is set, then the `title` attribute is set to the product title.

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'external_video' %}
    {% if media.host == 'youtube' %}
      {{ media | external_video_url: color: 'white' | external_video_tag }}
    {% elsif media.host == 'vimeo' %}
      {{ media | external_video_url: loop: '1', muted: '1' | external_video_tag }}
    {% endif %}
  {% endif %}
{% endfor %}
```

##### Data

```json
{
  "product": {
    "media": [
      {
        "media_type": "external_video"
      },
      {
        "media_type": "video"
      }
    ]
  }
}
```

##### Output

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```

### HTML attributes

```oobleck
variable | external_video_tag: attribute: string
```

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attributes) by adding a parameter that matches the attribute name, and the desired value.

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'external_video' %}
    {% if media.host == 'youtube' %}
      {{ media | external_video_url: color: 'white' | external_video_tag: class:'youtube-video' }}
    {% endif %}
  {% endif %}
{% endfor %}
```

##### Data

```json
{
  "product": {
    "media": [
      {
        "media_type": "external_video"
      },
      {
        "media_type": "video"
      }
    ]
  }
}
```

##### Output

```html
<iframe frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen" class="youtube-video" src="https://www.youtube.com/embed/vj01PAffOac?color=white&amp;controls=1&amp;enablejsapi=1&amp;modestbranding=1&amp;origin=https%3A%2F%2Fpolinas-potent-potions.myshopify.com&amp;playsinline=1&amp;rel=0" title="Potion beats"></iframe>
```
