---
title: 'Liquid filters: json'
description: 'Converts a string, or object, into JSON format.'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/json'
  md: 'https://shopify.dev/docs/api/liquid/filters/json.md'
api_name: liquid
---

# json

```oobleck
variable | json
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a string, or object, into JSON format.

***

**Tip:** When using the JSON output in JavaScript, you don\&#39;t need to wrap it in quotes because the \<code>json\</code> filter includes them. The \<code>json\</code> filter also escapes any quotes inside the output.

***

#### Product inventory

When applied to a [`product` object](https://shopify.dev/docs/api/liquid/objects/product) on any Shopify store created after December 5, 2017, the `json` filter doesn't output values for the `inventory_quantity` and `inventory_policy` properties of any associated [variants](https://shopify.dev/docs/api/liquid/objects/variant). These properties are excluded to help prevent bots and crawlers from retrieving inventory quantities for stores to which they aren't granted access.

If you need inventory information, you can access it through individual variants.

##### Code

```liquid
{{ product | json }}
```

##### Output

```html
{"id":6792602320961,"title":"Crocodile tears","handle":"crocodile-tears","description":"","published_at":"2022-04-22T11:55:58-04:00","created_at":"2022-04-22T11:55:56-04:00","vendor":"Polina's Potent Potions","type":"","tags":["Salty"],"price":5600,"price_min":5600,"price_max":5600,"available":false,"price_varies":false,"compare_at_price":null,"compare_at_price_min":0,"compare_at_price_max":0,"compare_at_price_varies":false,"variants":[{"id":39888242344001,"title":"Default Title","option1":"Default Title","option2":null,"option3":null,"sku":"","requires_shipping":true,"taxable":true,"featured_image":null,"available":false,"name":"Crocodile tears","public_title":null,"options":["Default Title"],"price":5600,"weight":0,"compare_at_price":null,"inventory_management":"shopify","barcode":"","requires_selling_plan":false,"selling_plan_allocations":[],"quantity_rule":{"min":1,"max":null,"increment":1}}],"images":["\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958"],"featured_image":"\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958","options":["Title"],"media":[{"alt":null,"id":21772501975105,"position":1,"preview_image":{"aspect_ratio":1.5,"height":2974,"width":4460,"src":"\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958"},"aspect_ratio":1.5,"height":2974,"media_type":"image","src":"\/\/polinas-potent-potions.myshopify.com\/cdn\/shop\/products\/amber-beard-oil-bottle.jpg?v=1650642958","width":4460}],"requires_selling_plan":false,"selling_plan_groups":[],"content":""}
```
