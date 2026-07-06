---
title: 'Liquid objects: transaction'
description: A transaction associated with a checkout or order.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/transaction'
  md: 'https://shopify.dev/docs/api/liquid/objects/transaction.md'
api_name: liquid
---

# transaction

A transaction associated with a checkout or order.

## Properties

* * **amount**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The amount of the transaction in the currency's subunit.

    The amount is in the customer's local (presentment) currency.

    For currencies without subunits, such as JPY and KRW, tenths and hundredths of a unit are appended. For example, 1000 Japanese yen is output as 100000.

    **Tip:** Use \<a href="/docs/api/liquid/filters/money-filters">money filters\</a> to output a formatted amount.

  * **buyer\_​pending\_​payment\_​instructions**

    array of [pending\_payment\_instruction\_input](https://shopify.dev/docs/api/liquid/objects/pending_payment_instruction_input)

  * A list of `pending_payment_instruction_input` header-value pairs, with payment method-specific details. The customer can use these details to complete their purchase offline.

    If the payment method doesn’t support pending payment instructions, then an empty array is returned.

    | Supported payment method | Expected Values |
    | - | - |
    | ShopifyPayments - Multibanco | \[{header="Entity", value="12345"}, {header="Reference", value="999999999"}] |

  * **buyer\_​pending\_​payment\_​notice**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A notice that contains instructions for the customer on how to complete their payment. The messages are specific to the payment method used.

  * **created\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp of when the transaction was created.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **gateway**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [handleized](https://shopify.dev/docs/api/liquid/basics#modifying-handles) name of the payment provider used for the transaction.

  * **gateway\_​display\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the payment provider used for the transaction.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the transaction.

  * **kind**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The type of transaction.

    | Possible values | Description |
    | - | - |
    | authorization | The reserving of money that the customer has agreed to pay. |
    | capture | The transfer of the money that was reserved during the `authorization` step. |
    | sale | A combination of `authorization` and `capture` in one step. |
    | void | The cancellation of a pending `authorization` or `capture`. |
    | refund | The partial, or full, refund of captured funds. |

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the transaction.

  * **payment\_​details**

    [transaction\_payment\_details](https://shopify.dev/docs/api/liquid/objects/transaction_payment_details)

  * The transaction payment details.

  * **receipt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Information from the payment provider about the payment receipt.

    This includes things like whether the payment was a test, or an authorization code if there was one.

  * **show\_​buyer\_​pending\_​payment\_​instructions?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Whether the transaction is pending, and whether additional customer info is required to process the payment.

  * **status**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The status of the transaction.

    | Possible values |
    | - |
    | success |
    | pending |
    | failure |
    | error |

  * **status\_​label**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The status of the transaction, translated based on the current locale.

##### Example

```json
{
  "amount": "380.25",
  "created_at": "2022-06-15 19:13:14 -0400",
  "gateway": "shopify_payments",
  "gateway_display_name": "Shopify payments",
  "id": 5432242176065,
  "kind": "sale",
  "name": "c29944051400769.",
  "payment_details": {
    "credit_card_number": "•••• •••• •••• 4242",
    "credit_card_company": "Visa",
    "credit_card_last_four_digits": "4242",
    "receiver_info": null
  },
  "receipt": "#☠1☢\n---\nid: pi_3LB5Oh2m9fH5ulsO18aKrXyL\nobject: payment_intent\namount: 38025\namount_capturable: 0\namount_received: 38025\ncanceled_at: \ncancellation_reason: \ncapture_method: automatic\ncharges:\n  object: list\n  data:\n  - id: ch_3LB5Oh2m9fH5ulsO1KncBePo\n    object: charge\n    amount: 38025\n    application_fee: fee_1LB5Oi2m9fH5ulsOrVcBjr4k\n    balance_transaction:\n      id: txn_3LB5Oh2m9fH5ulsO1JtjGSxy\n      object: balance_transaction\n      exchange_rate: \n    captured: true\n    created: 1655334796\n    currency: cad\n    failure_code: \n    failure_message: \n    fraud_details: {}\n    livemode: false\n    metadata:\n      shop_id: '56174706753'\n      shop_name: Polina's Potent Potions\n      transaction_fee_total_amount: '791'\n      transaction_fee_tax_amount: '0'\n      payments_charge_id: '2076986474561'\n      order_transaction_id: '5432242176065'\n      manual_entry: 'false'\n      order_id: c29944051400769.1\n      email: cornelius.potionmaker@gmail.com\n    outcome:\n      network_status: approved_by_network\n      reason: \n      risk_level: normal\n      risk_score: 15\n      seller_message: Payment complete.\n      type: authorized\n    paid: true\n    payment_intent: pi_3LB5Oh2m9fH5ulsO18aKrXyL\n    payment_method: pm_1LB5Oh2m9fH5ulsOk67EqrsK\n    payment_method_details:\n      card:\n        brand: visa\n        checks:\n          address_line1_check: pass\n          address_postal_code_check: pass\n          cvc_check: pass\n        country: US\n        description: Visa Classic\n        ds_transaction_id: \n        exp_month: 1\n        exp_year: 2029\n        fingerprint: KE6OIQsc8EspGDeW\n        funding: credit\n        iin: '424242'\n        installments: \n        issuer: Stripe Payments UK Limited\n        last4: '4242'\n        mandate: \n        moto: \n        network: visa\n        network_token: \n        network_transaction_id: '541168454791087'\n        three_d_secure: \n        wallet: \n      type: card\n    refunded: false\n    source: \n    status: succeeded\n    mit_params:\n      network_transaction_id: '541168454791087'\n  has_more: false\n  total_count: 1\n  url: \"/v1/charges?payment_intent=pi_3LB5Oh2m9fH5ulsO18aKrXyL\"\nconfirmation_method: manual\ncreated: 1655334795\ncurrency: cad\nlast_payment_error: \nlivemode: false\nmetadata:\n  shop_id: '56174706753'\n  shop_name: Polina's Potent Potions\n  transaction_fee_total_amount: '791'\n  transaction_fee_tax_amount: '0'\n  payments_charge_id: '2076986474561'\n  order_transaction_id: '5432242176065'\n  manual_entry: 'false'\n  order_id: c29944051400769.1\n  email: cornelius.potionmaker@gmail.com\nnext_action: \npayment_method: pm_1LB5Oh2m9fH5ulsOk67EqrsK\npayment_method_types:\n- card\nsource: \nstatus: succeeded\n",
  "show_buyer_pending_payment_instructions?": null,
  "status": "success",
  "status_label": "Success"
}
```
