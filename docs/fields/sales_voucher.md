# Sales Voucher

## Overview

**Element Name:** `SALES_VOUCHER`<br>
**Type:** string<br>
**Architecture:** Complex conditional<br>
**Required:** No<br>
**Multiple:** Yes<br>
**Validation Rule:** Must be either empty or contain both CODE and DESC<br>

Sales voucher or discount code. Must contain both CODE and DESC elements when present.

### Child Elements

#### CODE

- **Type:** string
- **Required:** Yes (when parent has content)
- **Description:** Voucher code. Maximum 24 characters, required.

- **Max Length:** 24
- **Examples:** SAVE20

#### DESC

- **Type:** string
- **Required:** Yes (when parent has content)
- **Description:** Voucher description. Maximum 128 characters, required.

- **Max Length:** 128
- **Examples:** 20% discount on electronics


## General Constraints

- **Optional field** - can be omitted
- **Multiple occurrences** allowed

## XML Examples

```xml
<SALES_VOUCHER>
  <CODE>SAVE20</CODE>
  <DESC>20% discount on electronics</DESC>
</SALES_VOUCHER>
```




