import edgedb


def create_client(username: str, password: str, host: str, port: int):
    client = edgedb.create_client(
        host=host,
        port=port,
        user=username,
        password=password,
        tls_security="insecure",
        timeout=10,
    )
    client = client.with_retry_options(options=edgedb.RetryOptions(attempts=5))
    return client


client = create_client("edgedb", "<password>", "localhost", 10700)
query = """CONFIGURE INSTANCE SET listen_addresses := {'127.0.0.1', '::1'};"""

client.query(query)
