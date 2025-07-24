# Extended Warranty

## Overview

**Element Name:** `EXTENDED_WARRANTY`<br>
**Type:** string<br>
**Architecture:** Complex conditional<br>
**Required:** No<br>
**Multiple:** Yes<br>
**Validation Rule:** Must be either empty or contain both VAL and DESC<br>

Extended warranty option. Must contain both VAL (warranty period) and DESC (warranty description)
when present.

### Child Elements

#### VAL

- **Type:** integer
- **Required:** Yes (when parent has content)
- **Description:** Extended warranty period in months. Must be a positive integer.

- **Examples:** 24

#### DESC

- **Type:** string
- **Required:** Yes (when parent has content)
- **Description:** Extended warranty description. Maximum 128 characters, required.

- **Max Length:** 128
- **Examples:** Extended warranty covering all parts and labor


## General Constraints

- **Optional field** - can be omitted
- **Multiple occurrences** allowed

## XML Examples

```xml
<EXTENDED_WARRANTY>
  <VAL>24</VAL>
  <DESC>Extended warranty covering all parts and labor</DESC>
</EXTENDED_WARRANTY>
```




