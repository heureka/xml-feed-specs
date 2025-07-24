# Heureka Offer Feed XML Documentation

Welcome to the comprehensive documentation for the Heureka Offer Feed XML specification. This documentation is automatically generated from validated field definitions to ensure accuracy and consistency.

## Overview

**Version:** 1.0<br>
**Total Fields:** 26<br>
**Required Fields:** 8<br>

Heureka Offer Feed XML format allows e-shops to submit product information to Heureka.cz for
price comparison and shopping services.

## Quick Start

The XML feed follows this basic structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SHOP>
  <SHOPITEM>
    <!-- Required fields -->
    <ITEM_ID>product_123</ITEM_ID>
    <PRODUCTNAME>Samsung Galaxy S24</PRODUCTNAME>
    <URL>https://example.com/product/123</URL>
    <PRICE_VAT>25000</PRICE_VAT>
    <CATEGORYTEXT>Heureka.cz | Electronics | Mobile Phones</CATEGORYTEXT>

    <!-- Complex conditional field examples -->
    <PARAM>
      <VAL>128GB</VAL>
      <PARAM_NAME>Storage</PARAM_NAME>
    </PARAM>
    <PARAM/> <!-- Empty parameter -->

    <DELIVERY>
      <DELIVERY_ID>PPL</DELIVERY_ID>
      <DELIVERY_PRICE>99</DELIVERY_PRICE>
    </DELIVERY>

    <!-- Attribute-based field example -->
    <GIFT ID="gift_123">Free wireless headphones</GIFT>

    <!-- Other optional fields... -->
  </SHOPITEM>
</SHOP>
```

## Complete Field Reference

| Field Name | Display Name | Type | Architecture | Required | Description |
|------------|--------------|------|--------------|----------|-------------|
| [`ITEM_ID`](fields/item_id.md) | Item Id | string | simple | ✓ | Unique product identifier within the e-shop. Maximum 36 characters. Allowed char... |
| [`PRODUCTNAME`](fields/productname.md) | Productname | string | simple | ✓ | Basic product name that includes all mandatory category-specific information. Ma... |
| [`URL`](fields/url.md) | Url | string | simple | ✓ | Unique product page URL that displays price and add-to-cart option. Maximum 300... |
| [`IMGURL`](fields/imgurl.md) | Imgurl | string | simple | ✓ | Primary product image URL. Maximum 255 characters. Must start with http:// or ht... |
| [`PRICE_VAT`](fields/price_vat.md) | Price Vat | string | simple | ✓ | Final product price including VAT in Czech Koruna (CZK). Maximum 2 decimal place... |
| [`CATEGORYTEXT`](fields/categorytext.md) | Categorytext | string | simple | ✓ | Product category path. Must start with "Heureka.cz |" followed by category hiera... |
| [`DELIVERY_DATE`](fields/delivery_date.md) | Delivery Date | string | simple | ✓ | Expected delivery time. Can be number of days (1-999) or specific date in YYYY-M... |
| [`IMGURL_ALTERNATIVE`](fields/imgurl_alternative.md) | Imgurl Alternative | string | simple | ○ | Additional product images. Maximum 10 alternative images. Each URL maximum 255 c... |
| [`PRODUCT`](fields/product.md) | Product | string | simple | ○ | Alternative product identifier or code. Optional field for additional product re... |
| [`DESCRIPTION`](fields/description.md) | Description | string | simple | ○ | Detailed product description with features, specifications, and benefits. |
| [`VAT`](fields/vat.md) | Vat | string | simple | ○ | VAT rate percentage applied to the product (e.g., "21" for 21% VAT). |
| [`MANUFACTURER`](fields/manufacturer.md) | Manufacturer | string | simple | ○ | Product manufacturer or brand name. Used for filtering and brand-specific search... |
| [`EAN`](fields/ean.md) | Ean | string | simple | ○ | European Article Number (EAN-13) barcode. Must be exactly 13 digits. |
| [`ISBN`](fields/isbn.md) | Isbn | string | simple | ○ | International Standard Book Number. Accepts ISBN-10 (10 digits with possible X)... |
| [`ITEM_TYPE`](fields/item_type.md) | Item Type | string | simple | ○ | Type or classification of the product item for categorization purposes. |
| [`MANUFACTURER_POSTAL_ADDRESS`](fields/manufacturer_postal_address.md) | Manufacturer Postal Address | string | simple | ○ | Manufacturer's physical postal address for legal and contact purposes. |
| [`MANUFACTURER_ELECTRONIC_ADDRESS`](fields/manufacturer_electronic_address.md) | Manufacturer Electronic Address | string | simple | ○ | Manufacturer's electronic contact (email address or website URL) for support and... |
| [`HEUREKA_CPC`](fields/heureka_cpc.md) | Heureka Cpc | decimal | simple | ○ | Heureka Cost Per Click bid amount. Must be a positive decimal number greater tha... |
| [`ITEMGROUP_ID`](fields/itemgroup_id.md) | Itemgroup Id | string | simple | ○ | Group identifier for product variants (color, size, pattern variations). Maximum... |
| [`ACCESSORY`](fields/accessory.md) | Accessory | string | simple | ○ | Related accessory product ITEM_ID. Maximum 10 accessories can be specified for c... |
| [`SPECIAL_SERVICE`](fields/special_service.md) | Special Service | string | simple | ○ | Special service offered with the product (e.g., installation, setup, training).... |
| [`DELIVERY`](fields/delivery.md) | Delivery | string | complex_conditional | ✓ | Shipping method information. Maximum 100 different shipping methods. Must contai... |
| [`PARAM`](fields/param.md) | Param | string | complex_conditional | ○ | Product parameter with name-value pair. Must contain both VAL and PARAM_NAME ele... |
| [`EXTENDED_WARRANTY`](fields/extended_warranty.md) | Extended Warranty | string | complex_conditional | ○ | Extended warranty option. Must contain both VAL (warranty period) and DESC (warr... |
| [`SALES_VOUCHER`](fields/sales_voucher.md) | Sales Voucher | string | complex_conditional | ○ | Sales voucher or discount code. Must contain both CODE and DESC elements when pr... |
| [`GIFT`](fields/gift.md) | Gift | string | attribute_based | ○ | Gift item with description and ID. Content describes the gift (max 250 character... |

---

*This documentation is automatically generated from the field definitions. For questions or issues, please contact the development team.*