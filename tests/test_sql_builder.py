from snow_compare.sql_builder import (
    build_duplicate_keys_sql,
    build_duplicate_multiple_keys_sql,
    build_missing_keys_both_tables_sql,
    build_missing_keys_left_table_sql,
    build_missing_keys_right_table_sql,
    build_row_count_sql,
    build_distinct_count_sql,
)


def test_build_row_count_sql_contains_left_and_right_tables():
    sql = build_row_count_sql(
        left_table="DB.SCHEMA.LEFT_TABLE",
        right_table="DB.SCHEMA.RIGHT_TABLE",
    )

    assert "DB.SCHEMA.LEFT_TABLE" in sql
    assert "DB.SCHEMA.RIGHT_TABLE" in sql
    assert "COUNT(*) as row_count" in sql
    assert "UNION ALL" in sql


def test_build_distinct_count_sql_contains_left_right_and_key():
    sql = build_distinct_count_sql(
        left_table="DB.SCHEMA.LEFT_TABLE",
        right_table="DB.SCHEMA.RIGHT_TABLE",
        key="GUID",
    )

    assert "DB.SCHEMA.LEFT_TABLE" in sql
    assert "DB.SCHEMA.RIGHT_TABLE" in sql
    assert "GUID" in sql
    assert "COUNT(DISTINCT GUID) AS distinct_key_count" in sql
    assert "UNION ALL" in sql


def test_build_missing_keys_right_table_sql_contains_left_right_and_key():
    sql = build_missing_keys_right_table_sql(
        left_table="DB.SCHEMA.LEFT_TABLE",
        right_table="DB.SCHEMA.RIGHT_TABLE",
        key="GUID",
    )

    assert "DB.SCHEMA.LEFT_TABLE" in sql
    assert "DB.SCHEMA.RIGHT_TABLE" in sql
    assert "GUID" in sql
    assert "LEFT JOIN" in sql
    assert "WHERE r.GUID IS NULL" in sql


def test_build_missing_keys_left_table_sql_contains_left_right_and_key():
    sql = build_missing_keys_left_table_sql(
        left_table="DB.SCHEMA.LEFT_TABLE",
        right_table="DB.SCHEMA.RIGHT_TABLE",
        key="GUID",
    )

    assert "DB.SCHEMA.LEFT_TABLE" in sql
    assert "DB.SCHEMA.RIGHT_TABLE" in sql
    assert "GUID" in sql
    assert "LEFT JOIN" in sql
    assert "WHERE l.GUID IS NULL" in sql


def test_build_missing_keys_both_tables_sql_contains_left_right_and_key():
    sql = build_missing_keys_both_tables_sql(
        left_table="DB.SCHEMA.LEFT_TABLE",
        right_table="DB.SCHEMA.RIGHT_TABLE",
        key="GUID",
    )

    assert "DB.SCHEMA.LEFT_TABLE" in sql
    assert "DB.SCHEMA.RIGHT_TABLE" in sql
    assert "GUID" in sql
    assert "LEFT JOIN" in sql
    assert "WHERE r.GUID IS NULL" in sql
    assert "WHERE l.GUID IS NULL" in sql
    assert "UNION ALL" in sql


def test_build_duplicate_keys_sql_contains_table_and_key():
    sql = build_duplicate_keys_sql(
        table="DB.SCHEMA.TABLE",
        key="GUID",
    )

    assert "DB.SCHEMA.TABLE" in sql
    assert "GUID" in sql
    assert "GROUP BY GUID" in sql
    assert "HAVING COUNT(*) > 1" in sql


def test_build_duplicate_multiple_keys_sql_contains_table_and_keys():
    sql = build_duplicate_multiple_keys_sql(
        table="DB.SCHEMA.TABLE",
        keys=["GUID", "NAME"],
    )

    assert "DB.SCHEMA.TABLE" in sql
    assert "GUID" in sql
    assert "NAME" in sql
    assert "GROUP BY GUID, NAME" in sql
    assert "HAVING COUNT(*) > 1" in sql
