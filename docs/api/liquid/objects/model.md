---
title: 'Liquid objects: model'
description: A 3D model uploaded as product media.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/model'
  md: 'https://shopify.dev/docs/api/liquid/objects/model.md'
api_name: liquid
---

# model

A 3D model uploaded as product media.

***

**Tip:** Use the \<a href="/docs/api/liquid/filters/model\_viewer\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">model\<wbr/>\_viewer\<wbr/>\_tag\</span>\</code> filter\</a> to output a \<a href="https://modelviewer.dev">Google model viewer component\</a> for the model.

***

## Properties

* * **alt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The alt text of the model.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the model.

  * **media\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The media type of the model. Always returns `model`.

    ExampleFilter for media of a specific type

    You can use the `media_type` property with the [`where` filter](https://shopify.dev/docs/api/liquid/filters/where) to filter the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media) for all media of a desired type.

    ##### Code

    ```liquid
    {% assign models = product.media | where: 'media_type', 'model' %}

    {% for model in models %}
      {{- model | model_viewer_tag }}
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

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The position of the model in the [`product.media`](https://shopify.dev/docs/api/liquid/objects/product#product-media) array.

  * **preview\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * A preview image for the model.

  * **sources**

    array of [model\_source](https://shopify.dev/docs/api/liquid/objects/model_source)

  * The source files for the model.

##### Example

```json
{
  "alt": "Potion bottle",
  "id": 22064203137089,
  "media_type": "model",
  "position": 1,
  "preview_image": {},
  "sources": []
}
```
