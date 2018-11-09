from google.cloud import bigquery

def export_items_to_bigquery():
    # Instantiates a client
    bigquery_client = bigquery.Client()

    # Prepares a reference to the dataset
    dataset_ref = bigquery_client.dataset('PlotPositions')

    table_ref = dataset_ref.table('LogPositions')
    table = bigquery_client.get_table(table_ref)  # API call

    rows_to_insert = [
        ('525', '-74.0941958', '4.6038614', '2018-11-07 16:53:53'),
    ]
    errors = bigquery_client.insert_rows(table, rows_to_insert)  # API request
    assert errors == []

export_items_to_bigquery()