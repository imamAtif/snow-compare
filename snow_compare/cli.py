import typer
from rich.console import Console
from snow_compare.sql_builder import (
    build_duplicate_keys_sql,
    build_duplicate_multiple_keys_sql,
    build_missing_keys_both_tables_sql,
    build_missing_keys_left_table_sql,
    build_missing_keys_right_table_sql,
    build_row_count_sql,
    build_distinct_count_sql,
)

app = typer.Typer(help="Snowflake Table row count Comparison SQL Generator")


@app.callback()
def main() -> None:
    """
    Snowflake Table row count Comparison SQL Generator.
    """
    pass


@app.command("row-count")
def row_count(
    left: str = typer.Option(..., "--left", "-l", help="Left table name"),
    right: str = typer.Option(..., "--right", "-r", help="Right table name"),
) -> None:
    """
    generate SQL query to compare row counts of two tables.
    """
    sql_query = build_row_count_sql(left, right)
    console = Console()
    console.print(sql_query, style="bold green")


@app.command("distinct-count")
def distinct_count(
    left: str = typer.Option(..., "--left", "-l", help="Left table name"),
    right: str = typer.Option(..., "--right", "-r", help="Right table name"),
    key: str = typer.Option(..., "--key", "-k", help="Key column name"),
) -> None:
    """
    generate SQL query to compare distinct key counts of two tables.
    """
    sql_query = build_distinct_count_sql(left, right, key)
    console = Console()
    console.print(sql_query, style="bold green")


@app.command("missing-keys-right")
def missing_keys_right(
    left: str = typer.Option(..., "--left", "-l", help="Left table name"),
    right: str = typer.Option(..., "--right", "-r", help="Right table name"),
    key: str = typer.Option(..., "--key", "-k", help="Key column name"),
) -> None:
    """
    generate SQL query to find missing keys in the right table compared to the left table.
    """
    sql_query = build_missing_keys_right_table_sql(left, right, key)
    console = Console()
    console.print(sql_query, style="bold green")


@app.command("missing-keys-left")
def missing_keys_left(
    left: str = typer.Option(..., "--left", "-l", help="Left table name"),
    right: str = typer.Option(..., "--right", "-r", help="Right table name"),
    key: str = typer.Option(..., "--key", "-k", help="Key column name"),
) -> None:
    """
    generate SQL query to find missing keys in the left table compared to the right table.
    """
    sql_query = build_missing_keys_left_table_sql(left, right, key)
    console = Console()
    console.print(sql_query, style="bold green")


@app.command("missing-keys-both")
def missing_keys_both(
    left: str = typer.Option(..., "--left", "-l", help="Left table name"),
    right: str = typer.Option(..., "--right", "-r", help="Right table name"),
    key: str = typer.Option(..., "--key", "-k", help="Key column name"),
) -> None:
    """
    generate SQL query to find missing keys in both tables.
    """
    sql_query = build_missing_keys_both_tables_sql(left, right, key)
    console = Console()
    console.print(sql_query, style="bold green")


@app.command("duplicate-keys")
def duplicate_keys(
    table: str = typer.Option(..., "--table", "-t", help="Table name"),
    key: str = typer.Option(..., "--key", "-k", help="Key column name"),
) -> None:
    """
    generate SQL query to find duplicate keys in a table.
    """
    sql_query = build_duplicate_keys_sql(table, key)
    console = Console()
    console.print(sql_query, style="bold green")


@app.command("duplicate-multiple-keys")
def duplicate_multiple_keys(
    table: str = typer.Option(..., "--table", "-t", help="Table name"),
    keys: list = typer.Option(..., "--keys", "-k", help="Key column names"),
) -> None:
    """
    generate SQL query to find duplicate keys in a table.
    """
    sql_query = build_duplicate_multiple_keys_sql(table, keys)
    console = Console()
    console.print(sql_query, style="bold green")
