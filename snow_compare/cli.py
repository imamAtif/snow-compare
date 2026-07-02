import typer
from rich.console import Console
from snow_compare.sql_builder import build_row_count_sql, build_distinct_count_sql

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
