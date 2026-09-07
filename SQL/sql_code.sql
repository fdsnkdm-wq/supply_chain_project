CREATE TABLE IF NOT EXISTS dim_product (
    product_key INTEGER PRIMARY KEY,
    product_card_id INTEGER NOT NULL UNIQUE,
    product_name VARCHAR(255),
    product_price NUMERIC(10,2),
    product_status INTEGER,
    category_id INTEGER,
    category_name VARCHAR(255),
    department_id INTEGER,
    department_name VARCHAR(255)
);

-- dim_customer
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_key        INTEGER PRIMARY KEY,
    customer_id          INTEGER NOT NULL UNIQUE,
    customer_fname        VARCHAR(100),
    customer_lname        VARCHAR(100),
    customer_segment      VARCHAR(50),
    customer_city         VARCHAR(100),
    customer_state        VARCHAR(100),
    customer_country       VARCHAR(100),
    customer_street        VARCHAR(255),
    customer_zipcode       VARCHAR(20)
);

-- dim_geography
CREATE TABLE IF NOT EXISTS dim_geography (
    geography_key        INTEGER PRIMARY KEY,
    order_city             VARCHAR(100),
    order_state             VARCHAR(100),
    order_country            VARCHAR(100),
    order_region             VARCHAR(100),
    market                    VARCHAR(100),
    latitude                  NUMERIC(9,6),
    longitude                 NUMERIC(9,6)
);

-- dim_shipping
CREATE TABLE IF NOT EXISTS dim_shipping (
    shipping_key          INTEGER PRIMARY KEY,
    shipping_mode            VARCHAR(50),
    delivery_status           VARCHAR(50),
    late_delivery_risk         INTEGER,
    order_status                VARCHAR(50),
    type                          VARCHAR(50)
);

-- dim_date
CREATE TABLE IF NOT EXISTS dim_date (
    date_key              INTEGER PRIMARY KEY,
    full_date               DATE NOT NULL UNIQUE,
    year                     INTEGER,
    month                    INTEGER,
    week                     INTEGER,
    day_of_week               VARCHAR(20)
);

-- fact_order_items
CREATE TABLE IF NOT EXISTS fact_order_items (
    order_item_id            INTEGER PRIMARY KEY,
    order_id                   INTEGER NOT NULL,
    customer_key                INTEGER REFERENCES dim_customer(customer_key),
    product_key                  INTEGER REFERENCES dim_product(product_key),
    geography_key                 INTEGER REFERENCES dim_geography(geography_key),
    shipping_key                   INTEGER REFERENCES dim_shipping(shipping_key),
    order_date_key                  INTEGER REFERENCES dim_date(date_key),
    shipping_date_key                INTEGER REFERENCES dim_date(date_key),
    benefit_per_order                  NUMERIC(10,2),
    sales_per_customer                   NUMERIC(10,2),
    order_item_discount                    NUMERIC(10,2),
    order_item_discount_rate                 NUMERIC(5,4),
    order_item_product_price                   NUMERIC(10,2),
    order_item_profit_ratio                      NUMERIC(6,4),
    order_item_quantity                            INTEGER,
    sales                                             NUMERIC(10,2),
    order_item_total                                    NUMERIC(10,2),
    order_profit_per_order                                NUMERIC(10,2),
    days_for_shipping_real                                  INTEGER,
    days_for_shipment_scheduled                               INTEGER
);