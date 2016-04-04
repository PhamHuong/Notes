# MONO Connect to Postgres
## Samples:
- https://github.com/npgsql/npgsql/wiki/User-Manual
```
using System;
using System.Data;
using Npgsql;

public static class NpgsqlUserManual
{
  public static void Main(String[] args)
  {
    NpgsqlConnection conn = new NpgsqlConnection("Server=127.0.0.1;Port=5432;User Id=joe;Password=secret;Database=joedata;");
    conn.Open();

    NpgsqlCommand command = new NpgsqlCommand("select * from tablea", conn);


    try
    {
    NpgsqlDataReader dr = command.ExecuteReader();
    while(dr.Read())
    {
        for (i = 0; i < dr.FieldCount; i++)
        {
            Console.Write("{0} \t", dr[i]);
        }
        Console.WriteLine();
    }

    }

    finally
    {
      conn.Close();
    }
  }
}
```
