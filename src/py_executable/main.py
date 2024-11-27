import click
import pandas as pd


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def file_processor(input_file, output_file):
    """
    A CLI application to process input csv file and write output to another csv file

    input_file: Path to an existing csv file
    output_file: Path to save the processed csv file
    """
    try:
        data = pd.read_csv(input_file)
        click.echo(f"file {input_file} read successfully with rows: {len(data)}")

        data['processed'] = True

        data.to_csv(output_file, index=False)
        click.echo(f"processed file saved to: {output_file}")

    except Exception as e:
        click.echo(f"Error processing file: {e}", err=True)


if __name__ == "__main__":
    file_processor()