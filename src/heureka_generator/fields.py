"""Field definitions for Heureka Offer Feed XML specification."""

from .models import ArchetypeType, Field, FieldCollection, FieldType


def create_required_fields() -> list[Field]:
    """Create all required field definitions."""
    return [
        Field(
            name="ITEM_ID",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Unique product identifier within the e-shop. Maximum 36 characters. Allowed characters: a-z, A-Z, 0-9, underscore, hyphen.",
            required=True,
            max_length=36,
            pattern=r"[a-zA-Z0-9_-]{1,36}",
            examples=[{"value": "product_123"}],
        ),
        Field(
            name="PRODUCTNAME",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Basic product name that includes all mandatory category-specific information. Maximum 200 characters.",
            required=True,
            max_length=200,
            examples=[{"value": "Samsung Galaxy S24"}],
        ),
        Field(
            name="URL",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Unique product page URL that displays price and add-to-cart option. Maximum 300 characters. Must be unique for each product variant.",
            required=True,
            max_length=300,
            pattern=r"https?://[^\s]{1,290}",
            examples=[{"value": "https://example.com/product/123"}],
        ),
        Field(
            name="IMGURL",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Primary product image URL. Maximum 255 characters. Must start with http:// or https://.",
            required=True,
            max_length=255,
            pattern=r"https?://[^\s]{1,245}",
            examples=[{"value": "https://example.com/images/product.jpg"}],
        ),
        Field(
            name="PRICE_VAT",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Final product price including VAT in Czech Koruna (CZK). Maximum 2 decimal places. Supports formats: 25000, 25000.50, 25000,50.",
            required=True,
            pattern=r"\d+([.,]\d{1,2})?",
            examples=[{"value": "25000"}, {"value": "25000.50"}],
        ),
        Field(
            name="CATEGORYTEXT",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description='Product category path. Must start with "Heureka.cz |" followed by category hierarchy. Maximum 255 characters.',
            required=True,
            max_length=255,
            pattern=r"Heureka\.cz \|.*",
            examples=[{"value": "Heureka.cz | Electronics | Mobile Phones"}],
        ),
        Field(
            name="DELIVERY_DATE",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Expected delivery time. Can be number of days (1-999) or specific date in YYYY-MM-DD format.",
            required=True,
            pattern=r"\d{1,3}|\d{4}-\d{2}-\d{2}",
            examples=[{"value": "5"}, {"value": "2024-12-25"}],
        ),
        Field(
            name="IMGURL_ALTERNATIVE",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Additional product images. Maximum 10 alternative images. Each URL maximum 255 characters.",
            required=False,
            multiple=True,
            max_occurs=10,
            max_length=255,
            pattern=r"https?://[^\s]{1,245}",
            examples=[{"value": "https://example.com/images/product2.jpg"}],
        ),
    ]


def create_optional_fields() -> list[Field]:
    """Create commonly used optional field definitions."""
    return [
        Field(
            name="PRODUCT",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Alternative product identifier or code. Optional field for additional product reference.",
            required=False,
            examples=[{"value": "GALAXY-S24-256GB"}],
        ),
        Field(
            name="DESCRIPTION",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Detailed product description with features, specifications, and benefits.",
            required=False,
            examples=[{"value": "Premium smartphone with advanced camera system and fast processor."}],
        ),
        Field(
            name="VAT",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="VAT rate percentage applied to the product (e.g., \"21\" for 21% VAT).",
            required=False,
            examples=[{"value": "21"}],
        ),
        Field(
            name="MANUFACTURER",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Product manufacturer or brand name. Used for filtering and brand-specific searches.",
            required=False,
            examples=[{"value": "Samsung"}],
        ),
        Field(
            name="EAN",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="European Article Number (EAN-13) barcode. Must be exactly 13 digits.",
            required=False,
            pattern=r"\d{13}",
            examples=[{"value": "1234567890123"}],
        ),
        Field(
            name="ISBN",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="International Standard Book Number. Accepts ISBN-10 (10 digits with possible X) or ISBN-13 (13 digits) format.",
            required=False,
            pattern=r"\d{9}[\dX]|\d{13}",
            examples=[{"value": "9781234567890"}, {"value": "123456789X"}],
        ),
        Field(
            name="ITEM_TYPE",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Type or classification of the product item for categorization purposes.",
            required=False,
            examples=[{"value": "electronics"}],
        ),
        Field(
            name="MANUFACTURER_POSTAL_ADDRESS",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Manufacturer's physical postal address for legal and contact purposes.",
            required=False,
            examples=[{"value": "123 Manufacturing St, Industrial City, 12345"}],
        ),
        Field(
            name="MANUFACTURER_ELECTRONIC_ADDRESS",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Manufacturer's electronic contact (email address or website URL) for support and inquiries.",
            required=False,
            examples=[{"value": "support@manufacturer.com"}, {"value": "https://manufacturer.com"}],
        ),
        Field(
            name="HEUREKA_CPC",
            field_type=FieldType.DECIMAL,
            archetype=ArchetypeType.SIMPLE,
            description="Heureka Cost Per Click bid amount. Must be a positive decimal number greater than 0.",
            required=False,
            min_value=0.01,
            examples=[{"value": "5.50"}, {"value": "12.00"}],
        ),
        Field(
            name="ITEMGROUP_ID",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Group identifier for product variants (color, size, pattern variations). Maximum 36 characters. Links related product variants together.",
            required=False,
            max_length=36,
            pattern=r"[a-zA-Z0-9_-]{1,36}",
            examples=[{"value": "GALAXY-S24-GROUP"}],
        ),
        Field(
            name="ACCESSORY",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Related accessory product ITEM_ID. Maximum 10 accessories can be specified for cross-selling.",
            required=False,
            multiple=True,
            max_occurs=10,
            max_length=36,
            pattern=r"[a-zA-Z0-9_-]{1,36}",
            examples=[{"value": "CASE_123"}, {"value": "CHARGER_456"}],
        ),
        Field(
            name="SPECIAL_SERVICE",
            field_type=FieldType.STRING,
            archetype=ArchetypeType.SIMPLE,
            description="Special service offered with the product (e.g., installation, setup, training). Maximum 5 services, each up to 128 characters.",
            required=False,
            multiple=True,
            max_occurs=5,
            max_length=128,
            examples=[{"value": "Free installation"}, {"value": "Extended warranty setup"}],
        ),
    ]


def create_delivery_field() -> Field:
    """Create DELIVERY complex conditional field."""
    delivery_id_field = Field(
        name="DELIVERY_ID",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Predefined carrier code from the approved delivery methods list.",
        required=True,
        enum_values=[
            "CESKA_POSTA",
            "CESKA_POSTA_DOPORUCENA_ZASILKA",
            "CSAD_LOGISTIK_OSTRAVA",
            "DPD",
            "DHL",
            "DSV",
            "FOFR",
            "GEBRUDER_WEISS",
            "GEIS",
            "GLS",
            "HDS",
            "PPL",
            "SEEGMULLER",
            "TNT",
            "TOPTRANS",
            "UPS",
            "FEDEX",
            "RABEN_LOGISTICS",
            "ZASILKOVNA_NA_ADRESU",
            "123KURIER",
            "WEDO_HOME",
            "RHENUS_LOGISTICS",
            "MESSENGER",
            "ZASILKOVNA",
            "DPD_PICKUP",
            "BALIKOVNA_DEPOTAPI",
            "WEDO_POINT",
            "CESKA_POSTA_NAPOSTU",
            "PPL_PARCELSHOP",
            "GLS_PARCELSHOP",
            "ALZAPOINT",
            "DPD_BOX",
            "Z_BOX",
            "WEDO_BOX",
            "PPL_PARCELBOX",
            "BALIKOVNA_BOX",
            "ALZABOX",
            "ONLINE",
            "VLASTNI_PREPRAVA",
        ],
        examples=[{"value": "PPL"}],
    )

    delivery_price_field = Field(
        name="DELIVERY_PRICE",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Delivery price for prepayment orders. Numeric value with optional decimal places.",
        required=True,
        pattern=r"\d+([.,]\d{1,2})?",
        examples=[{"value": "99.5"}],
    )

    delivery_price_cod_field = Field(
        name="DELIVERY_PRICE_COD",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Delivery price for cash on delivery orders. Optional field.",
        required=False,
        pattern=r"\d+([.,]\d{1,2})?",
        examples=[{"value": "149"}],
    )

    return Field(
        name="DELIVERY",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.COMPLEX_CONDITIONAL,
        description="Shipping method information. Maximum 100 different shipping methods. Must contain DELIVERY_ID and DELIVERY_PRICE when present.",
        required=True,
        multiple=True,
        max_occurs=100,
        conditional_validation="Must be either empty or contain both DELIVERY_ID and DELIVERY_PRICE",
        child_elements=[
            delivery_id_field,
            delivery_price_field,
            delivery_price_cod_field,
        ],
    )


def create_param_field() -> Field:
    """Create PARAM complex conditional field."""
    val_field = Field(
        name="VAL",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Parameter value. Must be non-empty.",
        required=True,
        min_length=1,
        examples=[{"value": "128GB"}],
    )

    param_name_field = Field(
        name="PARAM_NAME",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Parameter name/label. Must be non-empty.",
        required=True,
        min_length=1,
        examples=[{"value": "Storage"}],
    )

    return Field(
        name="PARAM",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.COMPLEX_CONDITIONAL,
        description="Product parameter with name-value pair. Must contain both VAL and PARAM_NAME elements when present.",
        required=False,
        multiple=True,
        conditional_validation="Must be either empty or contain both VAL and PARAM_NAME",
        child_elements=[val_field, param_name_field],
    )


def create_extended_warranty_field() -> Field:
    """Create EXTENDED_WARRANTY complex conditional field."""
    val_field = Field(
        name="VAL",
        field_type=FieldType.INTEGER,
        archetype=ArchetypeType.SIMPLE,
        description="Extended warranty period in months. Must be a positive integer.",
        required=True,
        min_value=1,
        examples=[{"value": "24"}],
    )

    desc_field = Field(
        name="DESC",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Extended warranty description. Maximum 128 characters, required.",
        required=True,
        max_length=128,
        min_length=1,
        examples=[{"value": "Extended warranty covering all parts and labor"}],
    )

    return Field(
        name="EXTENDED_WARRANTY",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.COMPLEX_CONDITIONAL,
        description="Extended warranty option. Must contain both VAL (warranty period) and DESC (warranty description) when present.",
        required=False,
        multiple=True,
        conditional_validation="Must be either empty or contain both VAL and DESC",
        child_elements=[val_field, desc_field],
    )


def create_sales_voucher_field() -> Field:
    """Create SALES_VOUCHER complex conditional field."""
    code_field = Field(
        name="CODE",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Voucher code. Maximum 24 characters, required.",
        required=True,
        max_length=24,
        min_length=1,
        examples=[{"value": "SAVE20"}],
    )

    desc_field = Field(
        name="DESC",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Voucher description. Maximum 128 characters, required.",
        required=True,
        max_length=128,
        min_length=1,
        examples=[{"value": "20% discount on electronics"}],
    )

    return Field(
        name="SALES_VOUCHER",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.COMPLEX_CONDITIONAL,
        description="Sales voucher or discount code. Must contain both CODE and DESC elements when present.",
        required=False,
        multiple=True,
        conditional_validation="Must be either empty or contain both CODE and DESC",
        child_elements=[code_field, desc_field],
    )


def create_gift_field() -> Field:
    """Create GIFT attribute-based field."""
    id_attribute = Field(
        name="ID",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.SIMPLE,
        description="Gift product identifier referencing another ITEM_ID.",
        required=False,
        max_length=36,
        pattern=r"[a-zA-Z0-9_-]{1,36}",
        examples=[{"value": "gift_123"}],
    )

    return Field(
        name="GIFT",
        field_type=FieldType.STRING,
        archetype=ArchetypeType.ATTRIBUTE_BASED,
        description="Gift item with description and ID. Content describes the gift (max 250 characters), ID attribute references the gift product.",
        required=False,
        multiple=True,
        has_text_content=True,
        content_max_length=250,
        attributes=[id_attribute],
        examples=[{"value": "Free wireless headphones"}],
    )


def create_field_collection() -> FieldCollection:
    """Create complete field collection."""
    fields = []

    # Add required fields
    fields.extend(create_required_fields())

    # Add optional simple fields
    fields.extend(create_optional_fields())

    # Add complex conditional fields
    fields.append(create_delivery_field())
    fields.append(create_param_field())
    fields.append(create_extended_warranty_field())
    fields.append(create_sales_voucher_field())

    # Add attribute-based fields
    fields.append(create_gift_field())

    return FieldCollection(
        fields=fields,
        version="1.0",
        description="Heureka Offer Feed XML format allows e-shops to submit product information to Heureka.cz for price comparison and shopping services.",
    )
