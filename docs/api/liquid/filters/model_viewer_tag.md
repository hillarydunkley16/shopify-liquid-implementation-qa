---
title: 'Liquid filters: model_viewer_tag'
description: >-
  Generates a [Google model viewer component](https://modelviewer.dev/) for a
  given 3D model.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/model_viewer_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/model_viewer_tag.md'
api_name: liquid
---

# model\_​viewer\_​tag

```oobleck
media | model_viewer_tag
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates a [Google model viewer component](https://modelviewer.dev/) for a given 3D model.

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag }}
  {% endif %}
{% endfor %}
```

##### Data

```json
{
  "product": {
    "media": [
      {
        "media_type": "model"
      }
    ]
  }
}
```

##### Output

```html
<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_small.jpg?v=1655189057"></model-viewer>
```

### Model viewer attributes

```oobleck
media | model_viewer_tag: attribute: string
```

By default, the model viewer component has the following attributes:

| Attribute | Value |
| - | - |
| `alt` | `[alt-text]` - The media's alt text. |
| `poster` | `[preview-image-url]` - The media's preview image URL. |
| `camera-controls` | N/A - Allows for controls via mouse/touch. |

You can override these attributes, or any [supported model viewer component attributes](https://modelviewer.dev/docs/index.html#stagingandcameras-attributes) by adding a parameter that matches the attribute name, and the desired value.

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag: interaction-policy: 'allow-when-focused' }}
  {% endif %}
{% endfor %}
```

##### Data

```json
{
  "product": {
    "media": [
      {
        "media_type": "model"
      }
    ]
  }
}
```

##### Output

```html
<model-viewer interaction-policy="allow-when-focused" src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_small.jpg?v=1655189057"></model-viewer>
```

### image\_size

```oobleck
media | model_viewer_tag: image_size: string
```

Specify the dimensions of the model's poster image in pixels.

##### Code

```liquid
{% for media in product.media %}
  {% if media.media_type == 'model' %}
    {{ media | model_viewer_tag: image_size: '400x' }}
  {% endif %}
{% endfor %}
```

##### Data

```json
{
  "product": {
    "media": [
      {
        "media_type": "model"
      }
    ]
  }
}
```

##### Output

```html
<model-viewer src="//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0" camera-controls="true" style="--poster-color: transparent;" data-shopify-feature="1.12" alt="Potion bottle" poster="//polinas-potent-potions.myshopify.com/cdn/shop/products/WaterBottle_400x.jpg?v=1655189057"></model-viewer>
```
