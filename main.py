import psycopg2
from psycopg2._psycopg import cursor


if __name__ == '__main__':
    with psycopg2.connect("dbname=postgres user=postgres host=localhost port=7543") as conn:
        cursor: cursor
        with conn.cursor() as cursor:
            try:
                cursor.execute("""
                BEGIN;
                CREATE TABLE IF NOT EXISTS city
                (
                    id   serial PRIMARY KEY,
                    name varchar(255)
                );
                CREATE TABLE IF NOT EXISTS tenants
                (
                    id   serial PRIMARY KEY,
                    name varchar(255)
                );
                CREATE TABLE IF NOT EXISTS app_user
                (
                    id   serial,
                    name varchar(255),
                    city_id INT NOT NULL,
                    tenant_id INT NOT NULL,
                    PRIMARY KEY (id, tenant_id),
                    FOREIGN KEY (tenant_id) REFERENCES tenants (id),
                    FOREIGN KEY (city_id) REFERENCES city (id)
                );
                select create_reference_table('city');
                select create_distributed_table('tenants', 'id');
                select create_distributed_table('app_user', 'tenant_id');
                ROLLBACK;
                """)
            except psycopg2.Error as e:
                print("Error", e)

            print("OK")
